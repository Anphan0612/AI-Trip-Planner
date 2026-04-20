package com.example.tripplanner.domain.model;

import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.util.UUID;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Activity {
    private UUID id;
    private Itinerary itinerary;
    private String name;
    private String description;
    private String location;
    private LocalTime startTime;
    private LocalTime endTime;
    private BigDecimal cost;
    private Integer activityOrder;
    private LocalDateTime createdAt;
}
