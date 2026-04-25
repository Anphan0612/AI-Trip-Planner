package com.example.tripplanner.interfaces.controller;

import com.example.tripplanner.application.dto.ParseTripRequest;
import com.example.tripplanner.application.dto.ParseTripResult;
import com.example.tripplanner.application.service.AiProxyService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@Slf4j
@RestController
@RequestMapping("/api/v1/ai")
@RequiredArgsConstructor
public class AiController {

    private final AiProxyService aiProxyService;

    @PostMapping("/parse-trip")
    public ResponseEntity<ParseTripResult> parseTrip(@RequestBody ParseTripRequest request) {
        try {
            ParseTripResult result = aiProxyService.parseTrip(request);
            return ResponseEntity.ok(result);
        } catch (Exception e) {
            log.error("Error during AI trip parsing", e);
            // Return empty result or handle accordingly
            return ResponseEntity.internalServerError().build();
        }
    }
}
