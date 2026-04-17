package com.example.tripplanner.domain.port;

import com.example.tripplanner.domain.model.AiLog;

import java.util.Map;

public interface AiLogRepository {
    AiLog save(AiLog aiLog);
    long countTotal();
    long countByStatus(String status);
    Double getAverageTotalTokens();
    long countByRetryCountGreaterThan(int retryCount);
    Double getAverageRetryCount();
    Map<String, Long> getValidationErrorCounts();
}
