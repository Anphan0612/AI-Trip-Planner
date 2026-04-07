package com.example.tripplanner.application.usecase;

import com.example.tripplanner.application.dto.TripRequest;
import com.example.tripplanner.application.dto.TripResponse;
import com.example.tripplanner.application.orchestrator.AIOrchestrator;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class GenerateTripPlanUseCase {

    private final AIOrchestrator orchestrator;

    public TripResponse execute(TripRequest request) {
        String result = orchestrator.orchestrate(request.getDestination(), request.getDays());
        return new TripResponse(result);
    }
}
