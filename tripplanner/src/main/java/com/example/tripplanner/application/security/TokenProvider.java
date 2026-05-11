package com.example.tripplanner.application.security;

import com.example.tripplanner.domain.model.Role;

import java.util.UUID;

public interface TokenProvider {
    String generateToken(UUID userId, Role role);
}
