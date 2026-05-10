package com.example.tripplanner.application.usecase;

import com.example.tripplanner.application.dto.ModerationStatsResponse;
import com.example.tripplanner.domain.model.ShareStatus;
import com.example.tripplanner.infrastructure.persistence.JpaSharedContentRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class GetModerationStatsUseCase {
    private final JpaSharedContentRepository repository;

    @Transactional(readOnly = true)
    public ModerationStatsResponse execute() {
        return ModerationStatsResponse.builder()
                .pendingCount(repository.countByStatus(ShareStatus.PENDING))
                .approvedCount(repository.countByStatus(ShareStatus.PUBLISHED))
                .rejectedCount(repository.countByStatus(ShareStatus.REJECTED))
                .build();
    }
}
