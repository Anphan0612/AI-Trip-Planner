package com.example.tripplanner.domain.port;

import java.util.Map;

public interface AiServicePort {
    Map<String, Object> callAi(String prompt);
}
