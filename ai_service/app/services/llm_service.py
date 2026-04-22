import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class LLMService:
    SYSTEM_PROMPT = """You are an AI assistant that completes missing travel information using context.

You are given:
1. Current user input
2. Previously extracted entities
3. User profile (preferences)

Your job:
- Fill missing or unclear fields
- Prefer user profile over guessing
- Do NOT override valid user input
- Keep output realistic

Rules:
- If a field is already valid → keep it
- If missing → try:
  1. conversation context
  2. user profile
- Do NOT hallucinate unknown destinations

Input:

User input:
"{text}"

Current entities:
{entities_json}

User profile:
{user_profile_json}

Return JSON ONLY:
{{
  "destination": string or null,
  "vibe": string or null,
  "budget": number or null,
  "duration_days": number or null,
  "group_type": string or null
}}"""

    ITINERARY_SYSTEM_PROMPT = """You are a travel planner AI.

Generate a realistic travel itinerary based on user preferences.

Constraints:
- Be practical and geographically logical
- Do NOT include impossible travel distances in 1 day
- Keep activities concise
- Use real-world style suggestions

Input:

Destination: {destination}
Duration: {duration_days} days
Budget: {budget} VND
Vibe: {vibe}
Group: {group_type}

Return JSON ONLY:

{{
  "days": [
    {{
      "day": 1,
      "activities": [
        "Morning: ...",
        "Afternoon: ...",
        "Evening: ..."
      ]
    }}
  ]
}}"""

    def __init__(self):
        # Configuration for OpenAI / Groq / OpenRouter
        self.api_key = "stub-api-key"
        self.model = "stub-model"

    def repair_entities(self, text: str, current_entities: Dict[str, Any], user_profile: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Stub method to simulate LLM repairing missing or misunderstood entities.
        In the future, this will call a real LLM API with a prompt containing `text`, `current_entities`, and `user_profile`.
        """
        logger.info(f"LLM Fallback triggered for text: '{text}'")
        
        # Format the actual prompt that would be sent to the LLM
        import json
        entities_json = json.dumps(current_entities, ensure_ascii=False, indent=2)
        user_profile_json = json.dumps(user_profile or {}, ensure_ascii=False, indent=2)
        
        messages = [
        {
            "role": "system",
            "content": """You are an AI assistant that completes missing travel information using context.

            STRICT RULES:
            - Return ONLY valid JSON
            - Do NOT include explanations
            - Do NOT override valid user input
            - Prefer user profile over guessing
            """
        },
        {
            "role": "user",
                    "content": f"""
            User input:
            {text}

            Current entities:
            {entities_json}

            User profile:
            {user_profile_json}
            """
        }
        ]
        logger.info(f"Generated LLM Prompt:\n{messages}")
        
        # Mock behavior: simulate the LLM finding something we missed.
        # In a real scenario, we would parse the JSON response from the LLM here.
        # giả lập output từ LLM
        llm_output = {}

        if not current_entities.get("destination"):
            llm_output["destination"] = "[LLM Repaired] Điểm đến ẩn"

        if not current_entities.get("vibe"):
            llm_output["vibe"] = "[LLM Repaired] Tự do"

        repaired = merge_entities(current_entities, llm_output)

    def generate_itinerary(self, destination: str, duration_days: int, budget: int, vibe: str, group_type: str) -> Dict[str, Any]:
        """
        Stub method to simulate LLM generating an itinerary.
        """
        logger.info(f"LLM Itinerary Generation triggered for {destination}")
        
        actual_prompt = self.ITINERARY_SYSTEM_PROMPT.format(
            destination=destination,
            duration_days=duration_days,
            budget=budget,
            vibe=vibe,
            group_type=group_type
        )
        logger.info(f"Generated LLM Itinerary Prompt:\n{actual_prompt}")
        
        # Mock behavior: Generate a static-like response but fitting the new schema
        days = []
        for d in range(1, duration_days + 1):
            days.append({
                "day": d,
                "activities": [
                    f"Morning: Khám phá địa điểm nổi tiếng tại {destination}",
                    f"Afternoon: Trải nghiệm hoạt động mang phong cách {vibe}",
                    "Evening: Ăn tối và dạo phố tự do"
                ]
            })
            
        return {"days": days}

    def safe_parse(content: str):
        try:
            return json.loads(content)
        except:
            match = re.search(r"\{.*\}", content, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group())
                except:
                    return {}
        return {}

    def merge_entities(original: Dict[str, Any], llm_output: Dict[str, Any]):
        merged = original.copy()

        for key, value in llm_output.items():
            if not merged.get(key) and value:
                merged[key] = value  # chỉ fill missing

        return merged

    def normalize_budget(value):
        if isinstance(value, str):
            v = value.lower().replace(" ", "")
            if "triệu" in v:
                return int(v.replace("triệu", "")) * 1_000_000
            if "tr" in v:
                return int(v.replace("tr", "")) * 1_000_000
        return value


    def normalize_duration(value):
        if isinstance(value, str):
            v = value.lower()
            if "ngày" in v:
                return int(v.split()[0])
        return value

llm_service = LLMService()
