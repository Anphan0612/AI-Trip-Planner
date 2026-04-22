package com.example.tripplanner.domain.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.util.UUID;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Recommendation {
    private UUID id;
    private String name;
    private RecommendationType type;
    private String description;
    private String location;
    private String priceLevel; // e.g., "$", "$$", "$$$"
}
