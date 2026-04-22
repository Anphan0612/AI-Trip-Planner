package com.example.tripplanner.infrastructure.persistence;

import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import java.util.UUID;

public interface JpaTripRepository extends JpaRepository<TripEntity, UUID> {
    List<TripEntity> findByUserId(UUID userId);
}
