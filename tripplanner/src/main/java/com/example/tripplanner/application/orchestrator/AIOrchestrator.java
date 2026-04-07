package com.example.tripplanner.application.orchestrator;

import com.example.tripplanner.domain.model.AiLog;
import com.example.tripplanner.domain.port.AiLogRepository;
import com.example.tripplanner.domain.port.AiServicePort;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Map;

@Component
@RequiredArgsConstructor
public class AIOrchestrator {

    private final AiServicePort aiServicePort;
    private final AiLogRepository aiLogRepository;

    public String orchestrate(String destination, int days) {
        String prompt = String.format("Generate a %d-day trip plan in JSON for %s. Return ONLY JSON.", days, destination);
        
        Map<String, Object> response = aiServicePort.callAi(prompt);
        
        // Extracting data from raw map
        List<Map<String, Object>> choices = (List<Map<String, Object>>) response.get("choices");
        Map<String, Object> message = (Map<String, Object>) choices.get(0).get("message");
        String content = (String) message.get("content");
        
        Map<String, Object> usage = (Map<String, Object>) response.get("usage");
        Integer promptTokens = (Integer) usage.get("prompt_tokens");
        Integer completionTokens = (Integer) usage.get("completion_tokens");

        AiLog log = AiLog.builder()
            .userInput(String.format("Destination: %s, Days: %d", destination, days))
            .prompt(prompt)
            .response(content)
            .model((String) response.get("model"))
            .promptTokens(promptTokens)
            .completionTokens(completionTokens)
            .totalTokens(promptTokens + completionTokens)
            .status("SUCCESS")
            .build();

        aiLogRepository.save(log);

        return content;
    }
}
