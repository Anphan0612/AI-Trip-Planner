package com.example.tripplanner.application.dto;

import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class AiServiceParseRequest {
    private String text;
    private String user_id;
}
