import json
import os

provinces = [
    "An Giang", "Bà Rịa - Vũng Tàu", "Bắc Giang", "Bắc Kạn", "Bạc Liêu", "Bắc Ninh", "Bến Tre", "Bình Định", 
    "Bình Dương", "Bình Phước", "Bình Thuận", "Cà Mau", "Cao Bằng", "Đắk Lắk", "Đắk Nông", "Điện Biên", 
    "Đồng Nai", "Đồng Tháp", "Gia Lai", "Hà Giang", "Hà Nam", "Hà Nội", "Hà Tĩnh", "Hải Dương", "Hải Phòng", 
    "Hậu Giang", "Hòa Bình", "Hưng Yên", "Khánh Hòa", "Kiên Giang", "Kon Tum", "Lai Châu", "Lâm Đồng", 
    "Lạng Sơn", "Lào Cai", "Long An", "Nam Định", "Nghệ An", "Ninh Bình", "Ninh Thuận", "Phú Thọ", "Phú Yên", 
    "Quảng Bình", "Quảng Nam", "Quảng Ngãi", "Quảng Ninh", "Quảng Trị", "Sóc Trăng", "Sơn La", "Tây Ninh", 
    "Thái Bình", "Thái Nguyên", "Thanh Hóa", "Thừa Thiên Huế", "Tiền Giang", "TP Hồ Chí Minh", "Trà Vinh", 
    "Tuyên Quang", "Vĩnh Long", "Vĩnh Phúc", "Yên Bái", "Đà Nẵng", "Cần Thơ"
]

# Dữ liệu mở rộng cho các tỉnh/thành du lịch nổi tiếng (3-5 địa điểm, nhà hàng rating cao)
custom_data = {
    "Đà Lạt": { # Đại diện cho Lâm Đồng
        "name": "Đà Lạt",
        "places": [
            {"name": "Hồ Xuân Hương", "type": "sightseeing", "vibe": "chill"},
            {"name": "Đỉnh Langbiang", "type": "adventure", "vibe": "khám phá"},
            {"name": "Thung Lũng Tình Yêu", "type": "sightseeing", "vibe": "chill"},
            {"name": "Thác Datanla", "type": "adventure", "vibe": "khám phá"},
            {"name": "Chợ Đêm Đà Lạt", "type": "nightlife", "vibe": "khám phá"}
        ],
        "restaurants": [
            {"name": "Lẩu Bò Ba Toa (Quán Gỗ) - Rating: 4.5/5", "type": "dinner", "vibe": "chill"},
            {"name": "Bánh Căn Lệ - Rating: 4.6/5", "type": "breakfast", "vibe": "khám phá"},
            {"name": "Tiệm Cà Phê Túi Mơ To - Rating: 4.7/5", "type": "cafe", "vibe": "chill"},
            {"name": "Nhà hàng Memory - Rating: 4.8/5", "type": "dinner", "vibe": "sang trọng"}
        ],
        "hotels": [
            {"name": "Dalat Palace Heritage", "price_level": "high"},
            {"name": "Colline Hotel", "price_level": "medium"},
            {"name": "Lâm Viên Homestay", "price_level": "low"}
        ]
    },
    "Phú Quốc": { # Đại diện cho Kiên Giang
        "name": "Phú Quốc",
        "places": [
            {"name": "VinWonders Phú Quốc", "type": "amusement", "vibe": "khám phá"},
            {"name": "Bãi Sao", "type": "beach", "vibe": "nghỉ dưỡng"},
            {"name": "Grand World Phú Quốc", "type": "sightseeing", "vibe": "khám phá"},
            {"name": "Cáp treo Hòn Thơm", "type": "sightseeing", "vibe": "khám phá"},
            {"name": "Chợ Đêm Dinh Cậu", "type": "nightlife", "vibe": "khám phá"}
        ],
        "restaurants": [
            {"name": "Nhà Hàng Ra Khơi - Rating: 4.4/5", "type": "dinner", "vibe": "chill"},
            {"name": "Bún Quậy Kiến Xây - Rating: 4.6/5", "type": "lunch", "vibe": "khám phá"},
            {"name": "Xin Chào Restaurant - Rating: 4.5/5", "type": "dinner", "vibe": "sang trọng"}
        ],
        "hotels": [
            {"name": "JW Marriott Phu Quoc Emerald Bay", "price_level": "high"},
            {"name": "Sunset Beach Resort & Spa", "price_level": "medium"},
            {"name": "Nadine Phu Quoc Resort", "price_level": "low"}
        ]
    },
    "Nha Trang": { # Khánh Hòa
        "name": "Nha Trang",
        "places": [
            {"name": "VinWonders Nha Trang", "type": "amusement", "vibe": "khám phá"},
            {"name": "Đảo Hòn Mun", "type": "beach", "vibe": "nghỉ dưỡng"},
            {"name": "Tháp Bà Ponagar", "type": "sightseeing", "vibe": "khám phá"},
            {"name": "Viện Hải Dương Học", "type": "sightseeing", "vibe": "khám phá"},
            {"name": "Chợ Đêm Nha Trang", "type": "nightlife", "vibe": "chill"}
        ],
        "restaurants": [
            {"name": "Hải Sản Mười Đô - Rating: 4.3/5", "type": "dinner", "vibe": "khám phá"},
            {"name": "Bánh Canh Bà Thừa - Rating: 4.5/5", "type": "lunch", "vibe": "chill"},
            {"name": "Costa Seafood Restaurant - Rating: 4.8/5", "type": "dinner", "vibe": "sang trọng"}
        ],
        "hotels": [
            {"name": "InterContinental Nha Trang", "price_level": "high"},
            {"name": "Novotel Nha Trang", "price_level": "medium"},
            {"name": "Mojzo Inn", "price_level": "low"}
        ]
    },
    "Hà Nội": {
        "name": "Hà Nội",
        "places": [
            {"name": "Hồ Hoàn Kiếm & Đền Ngọc Sơn", "type": "sightseeing", "vibe": "chill"},
            {"name": "Lăng Chủ tịch Hồ Chí Minh", "type": "sightseeing", "vibe": "khám phá"},
            {"name": "Khu Phố Cổ Hà Nội", "type": "sightseeing", "vibe": "khám phá"},
            {"name": "Văn Miếu - Quốc Tử Giám", "type": "sightseeing", "vibe": "khám phá"},
            {"name": "Phố đi bộ Tạ Hiện", "type": "nightlife", "vibe": "khám phá"}
        ],
        "restaurants": [
            {"name": "Phở Gia Truyền Bát Đàn - Rating: 4.6/5", "type": "breakfast", "vibe": "chill"},
            {"name": "Bún Chả Hương Liên (Obama) - Rating: 4.5/5", "type": "lunch", "vibe": "khám phá"},
            {"name": "Chả Cá Lã Vọng - Rating: 4.2/5", "type": "dinner", "vibe": "sang trọng"},
            {"name": "Maison Sen Buffet - Rating: 4.7/5", "type": "dinner", "vibe": "sang trọng"}
        ],
        "hotels": [
            {"name": "Sofitel Legend Metropole Hanoi", "price_level": "high"},
            {"name": "Hanoi La Siesta Hotel & Spa", "price_level": "medium"},
            {"name": "Little Charm Hanoi Hostel", "price_level": "low"}
        ]
    },
    "TP Hồ Chí Minh": {
        "name": "TP Hồ Chí Minh",
        "places": [
            {"name": "Chợ Bến Thành", "type": "sightseeing", "vibe": "khám phá"},
            {"name": "Dinh Độc Lập", "type": "sightseeing", "vibe": "khám phá"},
            {"name": "Phố đi bộ Nguyễn Huệ", "type": "nightlife", "vibe": "chill"},
            {"name": "Nhà thờ Đức Bà & Bưu điện Thành phố", "type": "sightseeing", "vibe": "chill"},
            {"name": "Khu phố Tây Bùi Viện", "type": "nightlife", "vibe": "khám phá"}
        ],
        "restaurants": [
            {"name": "Cơm Tấm Ba Ghiền - Rating: 4.5/5", "type": "lunch", "vibe": "khám phá"},
            {"name": "Secret Garden Restaurant - Rating: 4.6/5", "type": "dinner", "vibe": "chill"},
            {"name": "Noir. Dining in the Dark - Rating: 4.8/5", "type": "dinner", "vibe": "sang trọng"},
            {"name": "Cục Gạch Quán - Rating: 4.5/5", "type": "dinner", "vibe": "chill"}
        ],
        "hotels": [
            {"name": "Park Hyatt Saigon", "price_level": "high"},
            {"name": "Liberty Central Saigon Citypoint", "price_level": "medium"},
            {"name": "The Hammock Hotel Fine Arts Museum", "price_level": "low"}
        ]
    },
    "Đà Nẵng": {
        "name": "Đà Nẵng",
        "places": [
            {"name": "Sun World Ba Na Hills", "type": "amusement", "vibe": "khám phá"},
            {"name": "Bán đảo Sơn Trà & Chùa Linh Ứng", "type": "sightseeing", "vibe": "chill"},
            {"name": "Bãi biển Mỹ Khê", "type": "beach", "vibe": "nghỉ dưỡng"},
            {"name": "Cầu Rồng (Xem rồng phun lửa)", "type": "nightlife", "vibe": "khám phá"},
            {"name": "Ngũ Hành Sơn", "type": "sightseeing", "vibe": "khám phá"}
        ],
        "restaurants": [
            {"name": "Mì Quảng Bà Mua - Rating: 4.4/5", "type": "lunch", "vibe": "khám phá"},
            {"name": "Hải Sản Năm Đảnh - Rating: 4.6/5", "type": "dinner", "vibe": "chill"},
            {"name": "Bếp Cuốn Đà Nẵng - Rating: 4.7/5", "type": "dinner", "vibe": "khám phá"},
            {"name": "Madame Lân - Rating: 4.5/5", "type": "dinner", "vibe": "sang trọng"}
        ],
        "hotels": [
            {"name": "InterContinental Danang Sun Peninsula", "price_level": "high"},
            {"name": "Novotel Danang Premier Han River", "price_level": "medium"},
            {"name": "Seashore Hotel & Apartment", "price_level": "low"}
        ]
    },
    "Thừa Thiên Huế": {
        "name": "Thừa Thiên Huế",
        "places": [
            {"name": "Đại Nội Huế", "type": "sightseeing", "vibe": "khám phá"},
            {"name": "Lăng tẩm các vua Nguyễn", "type": "sightseeing", "vibe": "khám phá"},
            {"name": "Chùa Thiên Mụ", "type": "sightseeing", "vibe": "chill"},
            {"name": "Sông Hương (Nghe ca Huế)", "type": "nightlife", "vibe": "chill"}
        ],
        "restaurants": [
            {"name": "Bún Bò Huế Mụ Rơi - Rating: 4.5/5", "type": "breakfast", "vibe": "khám phá"},
            {"name": "Không Gian Xưa - Rating: 4.6/5", "type": "dinner", "vibe": "sang trọng"},
            {"name": "Quán Bánh Bèo Bà Đỏ - Rating: 4.4/5", "type": "lunch", "vibe": "khám phá"}
        ],
        "hotels": [
            {"name": "Azerai La Residence", "price_level": "high"},
            {"name": "Senna Hue Hotel", "price_level": "medium"}
        ]
    },
    "Quảng Nam": { # Tập trung Hội An
        "name": "Quảng Nam",
        "places": [
            {"name": "Phố cổ Hội An", "type": "sightseeing", "vibe": "chill"},
            {"name": "VinWonders Nam Hội An", "type": "amusement", "vibe": "khám phá"},
            {"name": "Cù Lao Chàm", "type": "beach", "vibe": "nghỉ dưỡng"},
            {"name": "Rừng dừa Bảy Mẫu", "type": "adventure", "vibe": "khám phá"}
        ],
        "restaurants": [
            {"name": "Bánh mì Phượng - Rating: 4.6/5", "type": "lunch", "vibe": "khám phá"},
            {"name": "Cơm gà Bà Buội - Rating: 4.5/5", "type": "lunch", "vibe": "khám phá"},
            {"name": "Morning Glory Original - Rating: 4.7/5", "type": "dinner", "vibe": "sang trọng"}
        ],
        "hotels": [
            {"name": "Four Seasons Resort The Nam Hai", "price_level": "high"},
            {"name": "Anantara Hoi An Resort", "price_level": "medium"}
        ]
    },
    "Quảng Ninh": { # Hạ Long
        "name": "Quảng Ninh",
        "places": [
            {"name": "Vịnh Hạ Long", "type": "sightseeing", "vibe": "khám phá"},
            {"name": "Sun World Hạ Long Complex", "type": "amusement", "vibe": "khám phá"},
            {"name": "Bảo tàng Quảng Ninh", "type": "sightseeing", "vibe": "chill"},
            {"name": "Đảo Tuần Châu", "type": "beach", "vibe": "nghỉ dưỡng"}
        ],
        "restaurants": [
            {"name": "Nhà Hàng Hồng Hạnh - Rating: 4.6/5", "type": "dinner", "vibe": "sang trọng"},
            {"name": "Hải Sản Thủy Chung - Rating: 4.4/5", "type": "dinner", "vibe": "chill"}
        ],
        "hotels": [
            {"name": "Vinpearl Resort & Spa Hạ Long", "price_level": "high"},
            {"name": "Wyndham Legend Halong", "price_level": "medium"}
        ]
    },
    "Ninh Bình": {
        "name": "Ninh Bình",
        "places": [
            {"name": "Quần thể danh thắng Tràng An", "type": "sightseeing", "vibe": "khám phá"},
            {"name": "Chùa Bái Đính", "type": "sightseeing", "vibe": "khám phá"},
            {"name": "Hang Múa", "type": "adventure", "vibe": "khám phá"},
            {"name": "Tam Cốc - Bích Động", "type": "sightseeing", "vibe": "chill"}
        ],
        "restaurants": [
            {"name": "Nhà hàng Chợ Quê Quán - Rating: 4.5/5", "type": "dinner", "vibe": "chill"},
            {"name": "Dê núi Chính Thư - Rating: 4.4/5", "type": "lunch", "vibe": "khám phá"}
        ],
        "hotels": [
            {"name": "Emeralda Resort Ninh Binh", "price_level": "high"},
            {"name": "Ninh Binh Hidden Charm", "price_level": "medium"}
        ]
    },
    "Bà Rịa - Vũng Tàu": {
        "name": "Bà Rịa - Vũng Tàu",
        "places": [
            {"name": "Bãi Sau Vũng Tàu", "type": "beach", "vibe": "nghỉ dưỡng"},
            {"name": "Tượng Chúa Dang Tay", "type": "sightseeing", "vibe": "khám phá"},
            {"name": "Ngọn Hải Đăng Vũng Tàu", "type": "sightseeing", "vibe": "chill"},
            {"name": "Hồ Tràm", "type": "beach", "vibe": "nghỉ dưỡng"}
        ],
        "restaurants": [
            {"name": "Hải sản Gành Hào - Rating: 4.6/5", "type": "dinner", "vibe": "sang trọng"},
            {"name": "Bánh Khọt Gốc Vú Sữa - Rating: 4.5/5", "type": "lunch", "vibe": "khám phá"},
            {"name": "Lẩu Cá Mát Vũng Tàu - Rating: 4.4/5", "type": "dinner", "vibe": "chill"}
        ],
        "hotels": [
            {"name": "The Imperial Hotel Vũng Tàu", "price_level": "high"},
            {"name": "Pullman Vũng Tàu", "price_level": "medium"}
        ]
    },
    "Sapa": { # Lào Cai
        "name": "Sapa",
        "places": [
            {"name": "Đỉnh Fansipan", "type": "adventure", "vibe": "khám phá"},
            {"name": "Bản Cát Cát", "type": "sightseeing", "vibe": "khám phá"},
            {"name": "Thung lũng Mường Hoa", "type": "sightseeing", "vibe": "chill"},
            {"name": "Đèo Ô Quy Hồ", "type": "adventure", "vibe": "khám phá"},
            {"name": "Nhà thờ đá Sapa", "type": "sightseeing", "vibe": "chill"}
        ],
        "restaurants": [
            {"name": "Thắng Cố A Quỳnh - Rating: 4.4/5", "type": "dinner", "vibe": "khám phá"},
            {"name": "Nhà hàng Hải Lâm - Rating: 4.5/5", "type": "lunch", "vibe": "chill"},
            {"name": "Good Morning Vietnam - Rating: 4.7/5", "type": "dinner", "vibe": "sang trọng"}
        ],
        "hotels": [
            {"name": "Hotel de la Coupole - MGallery", "price_level": "high"},
            {"name": "Sapa Station Hotel", "price_level": "medium"},
            {"name": "Mega View Homestay", "price_level": "low"}
        ]
    }
}

dataset = {}

for p in provinces:
    # Với các tỉnh trùng với custom_data hoặc tên phổ biến
    found_custom = None
    for key in custom_data:
        if key in p or p in key:
            found_custom = custom_data[key]
            break
            
    if found_custom:
        dataset[p] = {
            "name": p,
            "places": found_custom["places"],
            "restaurants": found_custom["restaurants"],
            "hotels": found_custom["hotels"]
        }
    else:
        dataset[p] = {
            "name": p,
            "places": [
                {"name": f"Khu di tích lịch sử {p}", "type": "sightseeing", "vibe": "khám phá"},
                {"name": f"Bảo tàng {p}", "type": "sightseeing", "vibe": "khám phá"},
                {"name": f"Công viên trung tâm {p}", "type": "sightseeing", "vibe": "chill"},
                {"name": f"Chợ đêm {p}", "type": "nightlife", "vibe": "khám phá"}
            ],
            "restaurants": [
                {"name": f"Nhà hàng đặc sản {p} - Rating: 4.5/5", "type": "dinner", "vibe": "sang trọng"},
                {"name": f"Quán ăn địa phương {p} - Rating: 4.4/5", "type": "lunch", "vibe": "khám phá"},
                {"name": f"Tiệm cà phê view đẹp {p} - Rating: 4.6/5", "type": "cafe", "vibe": "chill"}
            ],
            "hotels": [
                {"name": f"Khách sạn Mường Thanh {p}", "price_level": "high"},
                {"name": f"Khách sạn trung tâm {p}", "price_level": "medium"},
                {"name": f"Homestay {p} bình dân", "price_level": "low"}
            ]
        }

# Bổ sung các điểm du lịch đặc biệt không phải tỉnh thành (như Sapa, Đà Lạt)
extras = {
    "Đà Lạt": custom_data["Đà Lạt"],
    "Sapa": custom_data["Sapa"],
    "Hội An": custom_data["Quảng Nam"], # Copy data Quảng Nam cho Hội An
    "Hạ Long": custom_data["Quảng Ninh"],
    "Phú Quốc": custom_data["Phú Quốc"],
    "Nha Trang": custom_data["Nha Trang"]
}

for k, v in extras.items():
    dataset[k] = {
        "name": v.get("name", k),
        "places": v["places"],
        "restaurants": v["restaurants"],
        "hotels": v["hotels"]
    }

output_path = os.path.join(os.path.dirname(__file__), 'app', 'services', 'vietnam_63_provinces.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(dataset, f, ensure_ascii=False, indent=4)

print(f"Generated {len(dataset)} destinations in {output_path}")
