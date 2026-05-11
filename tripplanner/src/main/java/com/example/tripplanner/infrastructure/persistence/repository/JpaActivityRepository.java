package com.example.tripplanner.infrastructure.persistence.repository;
import com.example.tripplanner.infrastructure.persistence.entity.ActivityEntity;

import org.springframework.data.jpa.repository.JpaRepository;
import java.util.UUID;

public interface JpaActivityRepository extends JpaRepository<ActivityEntity, UUID> {
}

