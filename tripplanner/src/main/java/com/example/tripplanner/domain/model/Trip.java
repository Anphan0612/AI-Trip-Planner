package com.example.tripplanner.domain.model;

import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Trip {
    private UUID id;
    private User user;
    private String title;
    private String destination;
    private LocalDate startDate;
    private LocalDate endDate;
    private BigDecimal budget;
    private TripStatus status;
    private LocalDateTime createdAt;
    
    @Builder.Default
    private List<Itinerary> itineraries = new ArrayList<>();

    @Builder.Default
    private List<Recommendation> recommendations = new ArrayList<>();
}
