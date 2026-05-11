package com.example.tripplanner.application.dto.activity;

import com.example.tripplanner.application.dto.trip.*;
import com.example.tripplanner.application.dto.activity.*;
import com.example.tripplanner.application.dto.itinerary.*;
import com.example.tripplanner.application.dto.explore.*;
import com.example.tripplanner.application.dto.community.*;
import com.example.tripplanner.application.dto.auth.*;
import com.example.tripplanner.application.dto.ai.*;



import jakarta.validation.constraints.*;
import lombok.Data;
import java.math.BigDecimal;
import java.time.LocalTime;

@Data
public class ActivityRequest {

    @NotBlank(message = "name is required")
    @Size(min = 2, max = 200)
    private String name;

    @Size(max = 2000)
    private String description;

    @Size(max = 500)
    private String location;

    @NotNull(message = "startTime is required")
    private LocalTime startTime;

    @NotNull(message = "endTime is required")
    private LocalTime endTime;

    @DecimalMin(value = "0.0", inclusive = true)
    private BigDecimal cost;

    @Min(1)
    private Integer activityOrder;
}

