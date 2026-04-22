from typing import Dict, Any, List

# Global in-memory storage for trip history
# Structure: { "user_id": [ { "destination": "...", "vibe": "...", "budget": 2000000 }, ... ] }
trip_history_db: Dict[str, List[Dict[str, Any]]] = {}

class HistoryService:
    def save_history(self, user_id: str, entities: Any):
        if not user_id:
            return
            
        if user_id not in trip_history_db:
            trip_history_db[user_id] = []
            
        dest = entities.destination if entities.destination and "[LLM Repaired]" not in entities.destination else None
        vibe = entities.vibe if entities.vibe and "[LLM Repaired]" not in entities.vibe else None
        
        try:
            budget = int(entities.budget) if entities.budget is not None else None
        except (ValueError, TypeError):
            budget = None

        history_entry = {
            "destination": dest,
            "vibe": vibe,
            "budget": budget
        }
        
        # Only save if there's some meaningful data
        if any(history_entry.values()):
            trip_history_db[user_id].append(history_entry)
            
    def get_history(self, user_id: str) -> List[Dict[str, Any]]:
        return trip_history_db.get(user_id, [])

history_service = HistoryService()
