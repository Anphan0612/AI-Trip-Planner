package com.example.tripplanner.domain.model;

import lombok.*;
import java.time.LocalDateTime;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class AiLog {
    private Long id;
    private String tripId;
    private String userInput;
    private String prompt;
    private String response;
    private String model;
    private Integer promptTokens;
    private Integer completionTokens;
    private Integer totalTokens;
    private AiLogStatus status;
    private Integer retryCount;
    private String errorMessage;
    private ValidationType validationType;
    private Long executionTime;
    private String promptVersion;
    private LocalDateTime createdAt;
}
