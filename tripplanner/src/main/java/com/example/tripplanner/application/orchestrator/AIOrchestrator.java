// 3. AIOrchestrator.java
package com.example.tripplanner.application.orchestrator;

import com.example.tripplanner.application.validator.ValidationResult;
import com.example.tripplanner.application.validator.Validator;
import com.example.tripplanner.domain.model.AiLog;
import com.example.tripplanner.domain.port.AiLogRepository;
import com.example.tripplanner.domain.port.AiServicePort;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Map;

@Slf4j
@Component
@RequiredArgsConstructor
public class AIOrchestrator {

    private final AiServicePort aiServicePort;
    private final AiLogRepository aiLogRepository;
    private final Validator validator;

    public String orchestrate(String destination, int days) {
        String originalPrompt = String.format("Generate a %d-day trip plan in JSON for %s. Return ONLY JSON.", days, destination);
        String currentPrompt = originalPrompt;
        String finalContent = null;
        String errorMessage = null;

        int totalPromptTokens = 0;
        int totalCompletionTokens = 0;
        String model = null;
        int retryCount = 0;
        boolean isValid = false;
        String firstValidationType = null;
        
        long startTime = System.currentTimeMillis();

        for (int i = 0; i < 3; i++) {
            retryCount = i;
            log.info("--- 🚀 Gọi AI Lần {} ---", (i + 1));
            log.info("📩 Prompt gửi đi: {}", currentPrompt);

            Map<String, Object> response = aiServicePort.callAi(currentPrompt);

            // Extracting data from raw map
            @SuppressWarnings("unchecked")
            List<Map<String, Object>> choices = (List<Map<String, Object>>) response.get("choices");
            @SuppressWarnings("unchecked")
            Map<String, Object> message = (Map<String, Object>) choices.get(0).get("message");
            finalContent = (String) message.get("content");

            @SuppressWarnings("unchecked")
            Map<String, Object> usage = (Map<String, Object>) response.get("usage");
            totalPromptTokens += (Integer) usage.get("prompt_tokens");
            totalCompletionTokens += (Integer) usage.get("completion_tokens");
            model = (String) response.get("model");

            log.info("📦 AI Trả về độ dài nội dung: {} ký tự", finalContent != null ? finalContent.length() : 0);

            ValidationResult validationResult = validator.validate(finalContent);

            if (validationResult.isValid()) {
                long duration = System.currentTimeMillis() - startTime;
                log.info("✅ Validate THÀNH CÔNG! Hợp lệ JSON và Logic. Tokens: {}, Retries: {}, Time: {}ms", 
                         (totalPromptTokens + totalCompletionTokens), retryCount, duration);
                isValid = true;
                break;
            } else {
                errorMessage = validationResult.getErrorMessage();
                
                if (firstValidationType == null) {
                    if (errorMessage.startsWith("Invalid JSON")) firstValidationType = "FORMAT";
                    else if (errorMessage.startsWith("Schema error")) firstValidationType = "SCHEMA";
                    else if (errorMessage.startsWith("Business error")) firstValidationType = "BUSINESS";
                }
                
                log.warn("❌ Validate THẤT BẠI: {} (Retry: {})", errorMessage, retryCount);
                currentPrompt = buildRetryPrompt(errorMessage, finalContent);
                log.info("🔄 Thu thập lỗi, đang Build lại Prompt để Retry...");
            }
        }
        
        long executionTime = System.currentTimeMillis() - startTime;
        
        if (!isValid) {
            log.error("❌ AI Orchestration failed after {} retries. Final Error: {}", retryCount, errorMessage);
        }

        AiLog log = AiLog.builder()
                .userInput(String.format("Destination: %s, Days: %d", destination, days))
                .prompt(originalPrompt)
                .response(finalContent)
                .model(model)
                .promptTokens(totalPromptTokens)
                .completionTokens(totalCompletionTokens)
                .totalTokens(totalPromptTokens + totalCompletionTokens)
                .status(isValid ? "SUCCESS" : "FAILED")
                .retryCount(retryCount)
                .errorMessage(isValid ? null : errorMessage)
                .validationType(firstValidationType)
                .executionTime(executionTime)
                .promptVersion("v1.0")
                .build();

        aiLogRepository.save(log);

        return finalContent;
    }

    private String buildRetryPrompt(String errorMessage, String previousResponse) {
        String instruction = "";
        if (errorMessage.startsWith("Invalid JSON")) {
            instruction = "Fix this JSON and return ONLY valid JSON";
        } else if (errorMessage.startsWith("Schema error")) {
            instruction = "Ensure JSON matches required structure";
        } else if (errorMessage.startsWith("Business error")) {
            instruction = "Ensure each day has activities and cost > 0";
        }

        return String.format("%s. Fix this JSON. Error: %s. JSON: %s", instruction, errorMessage, previousResponse);
    }
}
