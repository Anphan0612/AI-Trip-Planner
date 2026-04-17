package com.example.tripplanner.infrastructure.persistence;

import com.example.tripplanner.domain.model.AiLog;
import com.example.tripplanner.domain.port.AiLogRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class AiLogRepositoryImpl implements AiLogRepository {
    private final JpaAiLogRepository jpaRepository;

    @Override
    public AiLog save(AiLog aiLog) {
        return jpaRepository.save(aiLog);
    }

    @Override
    public long countTotal() {
        return jpaRepository.count();
    }

    @Override
    public long countByStatus(String status) {
        return jpaRepository.countByStatus(status);
    }

    @Override
    public Double getAverageTotalTokens() {
        return jpaRepository.getAverageTotalTokens();
    }

    @Override
    public long countByRetryCountGreaterThan(int retryCount) {
        return jpaRepository.countByRetryCountGreaterThan(retryCount);
    }

    @Override
    public Double getAverageRetryCount() {
        return jpaRepository.getAverageRetryCount();
    }

    @Override
    public java.util.Map<String, Long> getValidationErrorCounts() {
        java.util.List<Object[]> results = jpaRepository.countByValidationType();
        java.util.Map<String, Long> map = new java.util.HashMap<>();
        for (Object[] result : results) {
            String type = (String) result[0];
            Long count = ((Number) result[1]).longValue();
            map.put(type, count);
        }
        return map;
    }
}
