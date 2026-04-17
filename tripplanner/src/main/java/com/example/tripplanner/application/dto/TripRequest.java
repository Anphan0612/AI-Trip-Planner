package com.example.tripplanner.application.dto;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class TripRequest {
    @NotBlank(message = "Destination cannot be empty")
    private String destination;
    
    @Min(value = 1, message = "Trip must be at least 1 day")
    private int days;
}
