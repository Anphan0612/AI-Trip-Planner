package com.example.tripplanner.interfaces.controller;

import com.example.tripplanner.application.dto.TripRequest;
import com.example.tripplanner.application.dto.TripResponse;
import com.example.tripplanner.application.usecase.GenerateTripPlanUseCase;

import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/trip")
@RequiredArgsConstructor
public class TripController {

    private final GenerateTripPlanUseCase generateTripPlanUseCase;

    @PostMapping("/generate")
    public TripResponse generate(@Valid@RequestBody TripRequest request) {
        return generateTripPlanUseCase.execute(request);
    }
}
