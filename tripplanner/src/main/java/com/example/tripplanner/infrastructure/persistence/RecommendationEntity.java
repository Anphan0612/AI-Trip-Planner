package com.example.tripplanner.infrastructure.persistence;

import com.example.tripplanner.domain.model.RecommendationType;
import jakarta.persistence.*;
import lombok.*;
import java.util.UUID;

@Entity
@Table(name = "recommendations")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class RecommendationEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(columnDefinition = "CHAR(36)")
    private UUID id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "trip_id", nullable = false)
    @ToString.Exclude
    @EqualsAndHashCode.Exclude
    private TripEntity trip;

    private String name;

    @Enumerated(EnumType.STRING)
    @Column(length = 20)
    private RecommendationType type;

    @Column(columnDefinition = "TEXT")
    private String description;

    private String location;

    @Column(name = "price_level")
    private String priceLevel;
}
