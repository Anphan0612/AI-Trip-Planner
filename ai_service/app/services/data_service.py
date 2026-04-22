from typing import Dict, Any, List

class DataService:
    def __init__(self):
        # In-memory static dataset
        self.destinations = {
            "Đà Lạt": {
                "name": "Đà Lạt",
                "places": [
                    {"name": "Hồ Xuân Hương", "type": "sightseeing", "vibe": "chill"},
                    {"name": "Langbiang", "type": "adventure", "vibe": "khám phá"},
                    {"name": "Thung Lũng Tình Yêu", "type": "sightseeing", "vibe": "chill"},
                    {"name": "Thác Datanla", "type": "adventure", "vibe": "khám phá"},
                    {"name": "Chợ Đêm Đà Lạt", "type": "nightlife", "vibe": "khám phá"},
                    {"name": "Đồi Chè Cầu Đất", "type": "sightseeing", "vibe": "chill"},
                    {"name": "Quảng Trường Lâm Viên", "type": "sightseeing", "vibe": "chill"}
                ],
                "restaurants": [
                    {"name": "Lẩu Bò Ba Toa", "type": "dinner", "vibe": "chill"},
                    {"name": "Bánh Căn Lệ", "type": "breakfast", "vibe": "khám phá"},
                    {"name": "Tiệm Cà Phê Túi Mơ To", "type": "cafe", "vibe": "chill"}
                ],
                "hotels": [
                    {"name": "Dalat Palace Heritage", "price_level": "high"},
                    {"name": "Colline Hotel", "price_level": "medium"},
                    {"name": "Kimi Homestay", "price_level": "low"},
                    {"name": "Tophill Hostel", "price_level": "low"}
                ]
            },
            "Phú Quốc": {
                "name": "Phú Quốc",
                "places": [
                    {"name": "VinWonders", "type": "amusement", "vibe": "khám phá"},
                    {"name": "Bãi Sao", "type": "beach", "vibe": "nghỉ dưỡng"},
                    {"name": "Grand World", "type": "sightseeing", "vibe": "khám phá"},
                    {"name": "Chợ Đêm Dinh Cậu", "type": "nightlife", "vibe": "khám phá"},
                    {"name": "Hòn Thơm", "type": "beach", "vibe": "nghỉ dưỡng"}
                ],
                "restaurants": [
                    {"name": "Nhà Hàng Ra Khơi", "type": "dinner", "vibe": "chill"},
                    {"name": "Bún Quậy Kiến Xây", "type": "lunch", "vibe": "khám phá"}
                ],
                "hotels": [
                    {"name": "JW Marriott Phu Quoc", "price_level": "high"},
                    {"name": "Sunset Beach Resort", "price_level": "medium"},
                    {"name": "Nadine Phu Quoc", "price_level": "low"}
                ]
            },
            "Nha Trang": {
                "name": "Nha Trang",
                "places": [
                    {"name": "Vinpearl Land", "type": "amusement", "vibe": "khám phá"},
                    {"name": "Hòn Mun", "type": "beach", "vibe": "nghỉ dưỡng"},
                    {"name": "Tháp Bà Ponagar", "type": "sightseeing", "vibe": "khám phá"},
                    {"name": "Viện Hải Dương Học", "type": "sightseeing", "vibe": "khám phá"},
                    {"name": "Chợ Đêm Nha Trang", "type": "nightlife", "vibe": "chill"}
                ],
                "restaurants": [
                    {"name": "Hải Sản Mười Đô", "type": "dinner", "vibe": "khám phá"},
                    {"name": "Bánh Canh Bà Thừa", "type": "lunch", "vibe": "chill"}
                ],
                "hotels": [
                    {"name": "InterContinental Nha Trang", "price_level": "high"},
                    {"name": "Amiana Resort", "price_level": "high"},
                    {"name": "Novotel Nha Trang", "price_level": "medium"},
                    {"name": "Mojzo Inn", "price_level": "low"}
                ]
            }
        }

    def get_destination_data(self, destination: str) -> Dict[str, Any]:
        """Fetch destination data, default to an empty structure if not found."""
        if not destination:
            return None
        # Title case matching (e.g., đà lạt -> Đà Lạt)
        dest_title = destination.title()
        return self.destinations.get(dest_title)

data_service = DataService()
