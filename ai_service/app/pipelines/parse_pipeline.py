import logging
from app.services.entity_extractor import entity_extractor
from app.services.intent_service import intent_service
from app.services.classifier_service import classifier_service
from app.services.confidence_service import confidence_service
from app.services.llm_service import llm_service
from app.services.data_service import data_service
from app.models.schemas import ParseResponse, EntityResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from typing import Dict, Any

class ParsePipeline:
    async def execute(self, text: str, user_profile: Dict[str, Any] = None) -> ParseResponse:
        logger.info(f"--- Processing Query: '{text}' ---")
        
        # 1. Layer 1: Extract Entities (Regex)
        entities_dict = entity_extractor.extract(text)
        logger.info(f"Layer 1 (Regex) Entities: {entities_dict}")
        
        # 2. Classify Intent
        intent = intent_service.classify(text)
        logger.info(f"Intent Classified: {intent}")
        
        # 3. Layer 2: Lightweight Classification
        classification_result = classifier_service.classify(text)
        logger.info(f"Layer 2 (Classifier) Result: {classification_result}")
        
        # Merge Layer 2 results into entities
        if classification_result["vibe"] and not entities_dict.get("vibe"):
            entities_dict["vibe"] = classification_result["vibe"]
        entities_dict["group_type"] = classification_result["group_type"]
        
        # 4. Confidence Check
        confidence, needs_llm = confidence_service.calculate_confidence(
            entities=entities_dict, 
            classifier_score=classification_result["confidence"]
        )
        logger.info(f"Confidence Score: {confidence:.2f} | Needs LLM: {needs_llm}")
        
        # --- DATASET FALLBACK LOGIC ---
        destination = entities_dict.get("destination")
        if destination and data_service.get_destination_data(destination):
            logger.info(f"Destination '{destination}' found in dataset. Bypassing LLM repair.")
            needs_llm = False
        
        source = "regex | hybrid"
        
        # 5. Layer 3: LLM Repair (Fallback)
        if needs_llm:
            entities_dict = await llm_service.repair_entities(text, entities_dict, user_profile)
            source = "hybrid | llm"
            # Even if LLM repairs it, we might keep the confidence score as it was before repair, 
            # or optionally boost it. For now, keep it to show why it fell back.
        
        # 6. Build Response
        return ParseResponse(
            intent=intent,
            entities=EntityResponse(**entities_dict),
            confidence=round(confidence, 2),
            source=source
        )

parse_pipeline = ParsePipeline()
