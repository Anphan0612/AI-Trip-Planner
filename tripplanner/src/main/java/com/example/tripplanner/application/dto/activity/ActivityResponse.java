package com.example.tripplanner.application.dto.activity;

import com.example.tripplanner.application.dto.trip.*;
import com.example.tripplanner.application.dto.activity.*;
import com.example.tripplanner.application.dto.itinerary.*;
import com.example.tripplanner.application.dto.explore.*;
import com.example.tripplanner.application.dto.community.*;
import com.example.tripplanner.application.dto.auth.*;
import com.example.tripplanner.application.dto.ai.*;



import lombok.Builder;
import lombok.Data;
import java.math.BigDecimal;
import java.time.LocalTime;
import java.util.UUID;

@Data
@Builder
public class ActivityResponse {
    private UUID id;
    private UUID itineraryId;
    private String name;
    private String description;
    private String location;
    private LocalTime startTime;
    private LocalTime endTime;
    private BigDecimal cost;
    private Integer activityOrder;
}

