// 2. Validator.java
package com.example.tripplanner.application.validator;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.stereotype.Component;

@Component
public class Validator {

    private final ObjectMapper objectMapper = new ObjectMapper();

    public ValidationResult validate(String json) {
        if (!isValidJson(json)) {
            return new ValidationResult(false, "Invalid JSON format");
        }

        try {
            JsonNode rootNode = objectMapper.readTree(json);

            ValidationResult schemaResult = validateSchema(rootNode);
            if (!schemaResult.isValid()) {
                return schemaResult;
            }

            return validateBusiness(rootNode);
        } catch (Exception e) {
            return new ValidationResult(false, "Invalid JSON parsing: " + e.getMessage());
        }
    }

    private boolean isValidJson(String json) {
        try {
            objectMapper.readTree(json);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    private ValidationResult validateSchema(JsonNode rootNode) {
        if (!rootNode.has("days") || !rootNode.get("days").isArray()) {
            return new ValidationResult(false, "Schema error: 'days' array is missing");
        }

        JsonNode daysNode = rootNode.get("days");
        for (JsonNode dayNode : daysNode) {
            if (!dayNode.has("activities") || !dayNode.get("activities").isArray()) {
                return new ValidationResult(false, "Schema error: 'activities' array is missing in one or more days");
            }
        }

        if (!rootNode.has("totalCost")) {
            return new ValidationResult(false, "Schema error: 'totalCost' is missing");
        }

        return new ValidationResult(true, null);
    }

    private ValidationResult validateBusiness(JsonNode rootNode) {
        JsonNode daysNode = rootNode.get("days");
        if (daysNode.size() == 0) {
            return new ValidationResult(false, "Business error: days array must not be empty");
        }

        for (JsonNode dayNode : daysNode) {
            JsonNode activitiesNode = dayNode.get("activities");
            if (activitiesNode.size() == 0) {
                return new ValidationResult(false, "Business error: each day must have at least 1 activity");
            }
        }

        JsonNode totalCostNode = rootNode.get("totalCost");
        if (!totalCostNode.isNumber() || totalCostNode.asDouble() <= 0) {
            return new ValidationResult(false, "Business error: totalCost must be > 0");
        }

        return new ValidationResult(true, null);
    }
}
