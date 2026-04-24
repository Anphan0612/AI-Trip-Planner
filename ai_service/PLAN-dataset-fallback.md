# Dataset Fallback Plan

Dự án này là Backend (AI Service) - Tối ưu hóa LLM Token bằng Dataset Matching.

## Mục tiêu (Overview)
- Giảm thiểu việc gọi LLM API (tiết kiệm token, giảm độ trễ) khi câu hỏi của người dùng nằm trong tập dữ liệu (dataset) có sẵn (ví dụ: Đà Lạt, Nha Trang, Phú Quốc).
- Chỉ gọi LLM khi điểm đến không có trong dataset (ví dụ: Sapa, Hà Nội, v.v.).

## Project Type
**BACKEND** (FastAPI / AI Service)

## Success Criteria
1. Nếu user nhập: "Tôi muốn đi Nha Trang":
   - `parse_pipeline` KHÔNG gọi `llm_service.repair_entities`.
   - `itinerary_service` KHÔNG gọi `llm_service.generate_itinerary`. Thay vào đó tự generate từ `data_service.py`.
2. Nếu user nhập: "Tôi muốn đi Sapa":
   - Do Sapa không có trong `data_service.py`, hệ thống VẪN gọi LLM bình thường.

## Task Breakdown

### Task 1: Ngăn chặn LLM Repair Entities khi có Dataset
- **Agent:** `backend-specialist`
- **Skill:** `api-patterns`
- **Input:** Kết quả entity extraction từ `parse_pipeline.py`.
- **Output:** Sửa đổi file `parse_pipeline.py`. Thêm bước check nếu `entities_dict["destination"]` có tồn tại trong `data_service.get_destination_data()`, ép `needs_llm = False`.
- **Verify:** Chạy script test với input "Nha Trang", log hiển thị `needs_llm: False` và không gọi `llm_service`.

### Task 2: Generate Itinerary tự động từ Dataset
- **Agent:** `backend-specialist`
- **Skill:** `api-patterns`
- **Input:** Hàm `generate_itinerary` trong `itinerary_service.py`.
- **Output:** Sửa đổi file `itinerary_service.py`. Nếu `data_service.get_destination_data(destination)` trả về data, viết logic mock tạo danh sách `days` ngẫu nhiên từ `places` và `restaurants`. Nếu không có, gọi `llm_service`.
- **Verify:** Chạy endpoint `/plan-trip` với Nha Trang, trả về lịch trình ngay lập tức không tốn API call.

## Phase X: Verification
- [ ] Test trường hợp CÓ trong dataset (Đà Lạt/Nha Trang/Phú Quốc).
- [ ] Test trường hợp KHÔNG CÓ trong dataset (Sapa).
- [ ] Đảm bảo response định dạng giống nhau ở cả 2 trường hợp.
