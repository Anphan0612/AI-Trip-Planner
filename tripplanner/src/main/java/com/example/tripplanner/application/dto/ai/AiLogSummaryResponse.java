package com.example.tripplanner.application.dto.ai;

import com.example.tripplanner.application.dto.trip.*;
import com.example.tripplanner.application.dto.activity.*;
import com.example.tripplanner.application.dto.itinerary.*;
import com.example.tripplanner.application.dto.explore.*;
import com.example.tripplanner.application.dto.community.*;
import com.example.tripplanner.application.dto.auth.*;
import com.example.tripplanner.application.dto.ai.*;



import lombok.Builder;
import lombok.Data;
import java.time.LocalDateTime;

@Data
@Builder
public class AiLogSummaryResponse {
    private Long id;
    private String tripId;
    private String model;
    private String status;
    private Integer totalTokens;
    private Long executionTime;
    private Integer retryCount;
    private LocalDateTime createdAt;
}

