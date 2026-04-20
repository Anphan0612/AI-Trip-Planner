package com.example.tripplanner.domain.model;

import lombok.*;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Itinerary {
    private UUID id;
    private Trip trip;
    private Integer dayNumber;
    private LocalDate date;
    private String summary;
    private LocalDateTime createdAt;
    
    @Builder.Default
    private List<Activity> activities = new ArrayList<>();
}
