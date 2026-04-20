package com.example.tripplanner.infrastructure.persistence;

import com.example.tripplanner.domain.model.AiLogStatus;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface JpaAiLogRepository extends JpaRepository<AiLogEntity, Long> {

    long countByStatus(AiLogStatus status);

    Page<AiLogEntity> findByTripId(String tripId, Pageable pageable);

    Page<AiLogEntity> findByTripIdAndStatus(String tripId, AiLogStatus status, Pageable pageable);

    @Query("SELECT AVG(a.totalTokens) FROM AiLogEntity a")
    Double getAverageTotalTokens();

    long countByRetryCountGreaterThan(Integer retryCount);

    @Query("SELECT AVG(a.retryCount) FROM AiLogEntity a")
    Double getAverageRetryCount();

    @Query("SELECT a.validationType as type, COUNT(a) as count FROM AiLogEntity a WHERE a.validationType IS NOT NULL GROUP BY a.validationType")
    List<Object[]> countByValidationType();
}
