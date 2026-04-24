import random
from typing import Dict, Any, List
from app.services.llm_service import llm_service

class ItineraryService:
    async def generate_itinerary(self, destination: str, duration_days: int, budget: int, vibe: str, group_type: str) -> Dict[str, Any]:
        if not destination or not duration_days or duration_days <= 0:
            return {"days": []}
            
        # Limit to max 10 days to avoid huge outputs
        duration_days = min(duration_days, 10)

        # Call the LLM service to generate the itinerary
        # In a fully integrated system, the LLM service would return the exact JSON structure
        return await llm_service.generate_itinerary(
            destination=destination,
            duration_days=duration_days,
            budget=budget or 0,
            vibe=vibe or "tự do",
            group_type=group_type or "solo"
        )

itinerary_service = ItineraryService()
