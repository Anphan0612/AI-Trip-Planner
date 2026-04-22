package com.example.tripplanner.domain.model;

import lombok.*;

import java.time.LocalDateTime;
import java.util.UUID;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class User {
    private UUID id;
    private String email;
    private String password;
    private String name;
    private Role role;
    private LocalDateTime createdAt;
}
