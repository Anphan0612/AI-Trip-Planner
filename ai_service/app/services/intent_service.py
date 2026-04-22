from typing import List

class IntentService:
    def __init__(self):
        self.rules = {
            "QUERY_HISTORY": ["tôi đã", "lịch sử", "tháng trước", "năm ngoái", "vừa rồi"],
            "PLAN_TRIP": ["đi", "du lịch", "plan", "lịch trình", "chuyến đi"],
            "FIND_HOTEL": ["khách sạn", "hotel", "chỗ ở", "homestay"]
        }

    def classify(self, text: str) -> str:
        text = text.lower()
        
        for intent, keywords in self.rules.items():
            if any(keyword in text for keyword in keywords):
                return intent
        
        return "UNKNOWN"

intent_service = IntentService()
