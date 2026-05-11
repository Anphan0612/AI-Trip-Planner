package com.example.tripplanner.application.dto.trip;

import com.example.tripplanner.application.dto.trip.*;
import com.example.tripplanner.application.dto.activity.*;
import com.example.tripplanner.application.dto.itinerary.*;
import com.example.tripplanner.application.dto.explore.*;
import com.example.tripplanner.application.dto.community.*;
import com.example.tripplanner.application.dto.auth.*;
import com.example.tripplanner.application.dto.ai.*;



import lombok.Builder;
import lombok.Data;
import java.util.List;

@Data
@Builder
public class ParseTripResult {
    private String destination;
    private String origin;
    private String startDate;
    private String endDate;
    private Integer travelers;
    private String budgetTier;
    private List<String> travelStyles;
    private String rawSummary;
}

