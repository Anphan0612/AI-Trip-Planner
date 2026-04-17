package com.example.tripplanner.infrastructure.persistence;

import com.example.tripplanner.domain.model.AiLog;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import org.springframework.data.jpa.repository.Query;
import java.util.List;

@Repository
public interface JpaAiLogRepository extends JpaRepository<AiLog, Long> {
    long countByStatus(String status);

    @Query("SELECT AVG(a.totalTokens) FROM AiLog a")
    Double getAverageTotalTokens();

    long countByRetryCountGreaterThan(Integer retryCount);

    @Query("SELECT AVG(a.retryCount) FROM AiLog a")
    Double getAverageRetryCount();

    @Query("SELECT a.validationType as type, COUNT(a) as count FROM AiLog a WHERE a.validationType IS NOT NULL GROUP BY a.validationType")
    List<Object[]> countByValidationType();
}
