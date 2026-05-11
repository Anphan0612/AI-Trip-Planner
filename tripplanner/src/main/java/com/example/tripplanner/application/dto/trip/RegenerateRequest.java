package com.example.tripplanner.application.dto.trip;

import com.example.tripplanner.application.dto.trip.*;
import com.example.tripplanner.application.dto.activity.*;
import com.example.tripplanner.application.dto.itinerary.*;
import com.example.tripplanner.application.dto.explore.*;
import com.example.tripplanner.application.dto.community.*;
import com.example.tripplanner.application.dto.auth.*;
import com.example.tripplanner.application.dto.ai.*;



import jakarta.validation.constraints.Size;
import lombok.Data;

@Data
public class RegenerateRequest {

    @Size(max = 1000)
    private String feedback;

    private String model;
    private String promptVersion;
    private String language = "Vietnamese";
}

