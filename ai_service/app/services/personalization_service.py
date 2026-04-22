from typing import Dict, Any, Tuple
from app.models.schemas import EntityResponse

class PersonalizationService:
    def enhance_entities(self, entities: EntityResponse, user_profile: Dict[str, Any]) -> Tuple[EntityResponse, bool]:
        if not user_profile:
            return entities, False
            
        personalized = False
        
        # If vibe is missing or mocked, use preferred vibe
        if (entities.vibe is None or "[LLM Repaired]" in entities.vibe) and user_profile.get("preferred_vibe"):
            entities.vibe = user_profile["preferred_vibe"]
            personalized = True
            
        # If budget is missing, use average budget
        if entities.budget is None and user_profile.get("avg_budget"):
            try:
                entities.budget = int(user_profile["avg_budget"])
                personalized = True
            except (ValueError, TypeError):
                pass
            
        # If destination is missing or mocked, use frequent destination
        if (entities.destination is None or "[LLM Repaired]" in entities.destination) and user_profile.get("frequent_destination"):
            entities.destination = user_profile["frequent_destination"]
            personalized = True
            
        return entities, personalized

personalization_service = PersonalizationService()
