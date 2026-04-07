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
}
