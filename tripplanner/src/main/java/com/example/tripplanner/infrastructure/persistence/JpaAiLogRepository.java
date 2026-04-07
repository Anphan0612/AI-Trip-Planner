package com.example.tripplanner.infrastructure.persistence;

import com.example.tripplanner.domain.model.AiLog;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface JpaAiLogRepository extends JpaRepository<AiLog, Long> {
}
