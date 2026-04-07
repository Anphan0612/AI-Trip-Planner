package com.example.tripplanner.domain.port;

import com.example.tripplanner.domain.model.AiLog;

public interface AiLogRepository {
    AiLog save(AiLog aiLog);
}
