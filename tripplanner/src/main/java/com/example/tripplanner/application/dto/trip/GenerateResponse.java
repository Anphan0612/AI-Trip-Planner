package com.example.tripplanner.application.dto.trip;

import com.example.tripplanner.application.dto.trip.*;
import com.example.tripplanner.application.dto.activity.*;
import com.example.tripplanner.application.dto.itinerary.*;
import com.example.tripplanner.application.dto.explore.*;
import com.example.tripplanner.application.dto.community.*;
import com.example.tripplanner.application.dto.auth.*;
import com.example.tripplanner.application.dto.ai.*;



import com.example.tripplanner.domain.model.TripStatus;
import lombok.Builder;
import lombok.Data;
import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;

@Data
@Builder
public class GenerateResponse {
    private UUID tripId;
    private TripStatus status;
    private Long aiLogId;
    private List<ItineraryResponse> itineraries;
    private List<ActivityCandidateResponse> candidates;
    private LocalDateTime generatedAt;
}

