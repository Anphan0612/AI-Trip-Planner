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
public class AiServiceEntityResponse {
    private String destination;
    private Integer duration_days;
    private Integer budget;
    private String vibe;
    private String time;
    private String group_type;
    private Integer travelers;
    private String origin;
    private String start_date;
    private String end_date;
}

