package com.example.tripplanner.application.dto.explore;

import com.example.tripplanner.application.dto.trip.*;
import com.example.tripplanner.application.dto.activity.*;
import com.example.tripplanner.application.dto.itinerary.*;
import com.example.tripplanner.application.dto.explore.*;
import com.example.tripplanner.application.dto.community.*;
import com.example.tripplanner.application.dto.auth.*;
import com.example.tripplanner.application.dto.ai.*;



import com.example.tripplanner.domain.model.RecommendationType;
import lombok.Builder;
import lombok.Data;
import java.util.UUID;

@Data
@Builder
public class RecommendationResponse {
    private UUID id;
    private String name;
    private RecommendationType type;
    private String description;
    private String location;
    private String priceLevel;
}

