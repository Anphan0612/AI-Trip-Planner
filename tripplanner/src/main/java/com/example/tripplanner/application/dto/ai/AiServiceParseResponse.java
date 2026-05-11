package com.example.tripplanner.application.dto.ai;

import com.example.tripplanner.application.dto.trip.*;
import com.example.tripplanner.application.dto.activity.*;
import com.example.tripplanner.application.dto.itinerary.*;
import com.example.tripplanner.application.dto.explore.*;
import com.example.tripplanner.application.dto.community.*;
import com.example.tripplanner.application.dto.auth.*;
import com.example.tripplanner.application.dto.ai.*;



import lombok.Data;

@Data
public class AiServiceParseResponse {
    private String intent;
    private AiServiceEntityResponse entities;
    private Double confidence;
    private String source;
}

