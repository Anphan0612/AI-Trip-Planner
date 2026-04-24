from typing import Dict, Any, List

import json
import os

class DataService:
    def __init__(self):
        # Load from JSON file
        json_path = os.path.join(os.path.dirname(__file__), "vietnam_63_provinces.json")
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                self.destinations = json.load(f)
        except Exception as e:
            print(f"Failed to load dataset: {e}")
            self.destinations = {}

    def get_destination_data(self, destination: str) -> Dict[str, Any]:
        """Fetch destination data, default to an empty structure if not found."""
        if not destination:
            return None
        # Title case matching (e.g., đà lạt -> Đà Lạt)
        dest_title = destination.title()
        return self.destinations.get(dest_title)

data_service = DataService()
