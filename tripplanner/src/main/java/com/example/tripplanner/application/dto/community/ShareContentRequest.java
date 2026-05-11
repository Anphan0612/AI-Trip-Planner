package com.example.tripplanner.application.dto.community;

import com.example.tripplanner.application.dto.trip.*;
import com.example.tripplanner.application.dto.activity.*;
import com.example.tripplanner.application.dto.itinerary.*;
import com.example.tripplanner.application.dto.explore.*;
import com.example.tripplanner.application.dto.community.*;
import com.example.tripplanner.application.dto.auth.*;
import com.example.tripplanner.application.dto.ai.*;



import com.example.tripplanner.domain.model.ShareType;
import lombok.Data;

import java.util.UUID;

@Data
public class ShareContentRequest {
    private ShareType type;
    private UUID refId; // Activity ID or Trip ID
    private String content; // JSON string for extra data if needed
    private Double rating;
    private String description;
    private Double cost;
    private Integer duration;
}

