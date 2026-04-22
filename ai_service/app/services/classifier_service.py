from typing import Dict, Any

class ClassifierService:
    def __init__(self):
        # Keyword mapping for group types
        self.group_keywords = {
            "solo": ["một mình", "solo", "tự túc"],
            "couple": ["cặp đôi", "2 người", "người yêu", "bạn gái", "bạn trai", "vợ chồng", "trăng mật"],
            "family": ["gia đình", "bố mẹ", "con cái", "trẻ em", "vợ con"],
            "friends": ["bạn bè", "nhóm bạn", "hội bạn", "bạn thân"]
        }
        
        # Keyword mapping for vibes
        self.vibe_keywords = {
            "chill": ["chill", "nhẹ nhàng", "thư giãn", "thong thả", "yên tĩnh"],
            "khám phá": ["khám phá", "trải nghiệm", "đi nhiều", "phượt", "phiêu lưu", "bụi"],
            "nghỉ dưỡng": ["nghỉ dưỡng", "resort", "hưởng thụ", "sang chảnh", "luxury"]
        }

    def classify_vibe(self, text: str) -> str:
        text = text.lower()
        for vibe, keywords in self.vibe_keywords.items():
            if any(kw in text for kw in keywords):
                return vibe
        return "unknown"

    def classify_group(self, text: str) -> str:
        text = text.lower()
        for group, keywords in self.group_keywords.items():
            if any(kw in text for kw in keywords):
                return group
        return "unknown"

    def classify(self, text: str) -> Dict[str, Any]:
        """
        Classifies the vibe and group type, and returns a confidence score.
        """
        vibe = self.classify_vibe(text)
        group = self.classify_group(text)
        
        # Simple confidence: 1.0 if both matched, 0.5 if one matched, 0.0 if neither matched.
        score = 0.0
        if vibe != "unknown":
            score += 0.5
        if group != "unknown":
            score += 0.5
            
        return {
            "vibe": vibe if vibe != "unknown" else None,
            "group_type": group if group != "unknown" else None,
            "confidence": score
        }

classifier_service = ClassifierService()
