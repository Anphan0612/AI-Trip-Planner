from typing import Dict, Any
from collections import Counter
from app.services.history_service import history_service

# Global in-memory storage for user profiles
# Structure: { "user_id": { "preferred_vibe": "...", "avg_budget": 1000000, "frequent_destination": "..." } }
user_profiles_db: Dict[str, Dict[str, Any]] = {}

class UserService:
    def update_profile(self, user_id: str):
        if not user_id:
            return
            
        history = history_service.get_history(user_id)
        if not history:
            return
            
        vibes = [entry["vibe"] for entry in history if entry.get("vibe") and "[LLM Repaired]" not in entry["vibe"]]
        destinations = [entry["destination"] for entry in history if entry.get("destination") and "[LLM Repaired]" not in entry["destination"]]
        budgets = [int(entry["budget"]) for entry in history if entry.get("budget") is not None]
        
        preferred_vibe = Counter(vibes).most_common(1)[0][0] if vibes else None
        frequent_dest = Counter(destinations).most_common(1)[0][0] if destinations else None
        avg_budget = sum(budgets) / len(budgets) if budgets else None
        
        user_profiles_db[user_id] = {
            "preferred_vibe": preferred_vibe,
            "frequent_destination": frequent_dest,
            "avg_budget": avg_budget
        }
        
    def get_profile(self, user_id: str) -> Dict[str, Any]:
        return user_profiles_db.get(user_id, {})

user_service = UserService()
