package com.example.tripplanner.infrastructure.ai;

import com.example.tripplanner.domain.model.AiResponse;
import com.example.tripplanner.domain.port.AiServicePort;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.reactive.function.client.WebClientResponseException;

import java.util.List;
import java.util.Map;

@Slf4j
@Service
@RequiredArgsConstructor
public class OpenRouterAiService implements AiServicePort {

    private final WebClient webClient;

    @Value("${ai-service.url:http://localhost:8000/ai}")
    private String apiUrl;

    @Override
    public AiResponse callAi(String prompt) {
        Map<String, String> requestBody = Map.of("prompt", prompt);

        try {
            ChatResponse raw = webClient.post()
                    .uri(apiUrl + "/chat")
                    .header("Content-Type", "application/json")
                    .bodyValue(requestBody)
                    .retrieve()
                    .bodyToMono(ChatResponse.class)
                    .block();

            if (raw == null || raw.content() == null) {
                throw new AiServiceException("Empty response from ai_service");
            }

            String cleanContent = raw.content().trim();
            if (cleanContent.startsWith("```")) {
                cleanContent = cleanContent.replaceFirst("^```(?:json|JSON)?\\s*", "");
                if (cleanContent.endsWith("```")) {
                    cleanContent = cleanContent.substring(0, cleanContent.length() - 3).trim();
                }
            }

            return new AiResponse(
                    cleanContent,
                    raw.prompt_tokens(),
                    raw.completion_tokens(),
                    raw.model()
            );

        } catch (WebClientResponseException ex) {
            log.error("ai_service HTTP error: status={}, body={}", ex.getStatusCode(), ex.getResponseBodyAsString());
            throw new AiServiceException("ai_service returned error: " + ex.getStatusCode(), ex);
        }
    }

    // ── ai_service response shape ─────────

    record ChatResponse(String content, String model, int prompt_tokens, int completion_tokens) {}
}
