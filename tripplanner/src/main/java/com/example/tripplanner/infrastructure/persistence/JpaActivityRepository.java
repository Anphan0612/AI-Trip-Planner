package com.example.tripplanner.infrastructure.persistence;

import org.springframework.data.jpa.repository.JpaRepository;
import java.util.UUID;

public interface JpaActivityRepository extends JpaRepository<ActivityEntity, UUID> {
}
