from typing import Dict, Any, Tuple

class ConfidenceService:
    def __init__(self):
        # We expect a maximum of 6 fields to be extracted ideally: 
        # destination, duration_days, budget, vibe, time, group_type
        self.expected_fields = 6

    def calculate_confidence(self, entities: Dict[str, Any], classifier_score: float) -> Tuple[float, bool]:
        """
        Calculates the overall confidence score of the extracted entities and classification.
        Returns the overall confidence and a needs_llm flag.
        """
        # Count non-null fields
        non_null_count = sum(1 for value in entities.values() if value is not None)
        
        # Regex score is the ratio of filled fields to expected fields
        regex_score = min(non_null_count / self.expected_fields, 1.0)
        
        # Overall confidence formula
        overall_confidence = (regex_score * 0.6) + (classifier_score * 0.4)
        
        # Flag if LLM is needed
        needs_llm = overall_confidence < 0.65
        
        return overall_confidence, needs_llm

confidence_service = ConfidenceService()
