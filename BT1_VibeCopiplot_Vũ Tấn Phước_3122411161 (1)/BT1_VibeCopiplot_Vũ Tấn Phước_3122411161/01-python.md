# 01. Python Backend

## 1. Giới thiệu
Chương này mô tả quá trình xây dựng backend bằng Python, đóng vai trò cung cấp API cho hệ thống.

---

## 2. Phân tích theo 3 mức

### 2.1 Mức ý tưởng
Backend chịu trách nhiệm:
- Xử lý nghiệp vụ
- Quản lý dữ liệu
- Cung cấp API cho frontend

---

### 2.2 Mức luận lý
Công nghệ sử dụng:
- **FastAPI**: framework backend hiện đại
- Kiến trúc:
  - Router: định tuyến API
  - Service: xử lý nghiệp vụ
  - Model: cấu trúc dữ liệu

Chuẩn giao tiếp: RESTful API.

---

### 2.3 Mức vật lý
- Server chạy tại `localhost`
- Port: `8000`
- Dữ liệu trao đổi dạng `JSON`
- Chạy bằng lệnh:
```bash
uvicorn main:app --reload
```

```
Client
  ↓
API Router
  ↓
Business Logic
  ↓
Response (JSON)
```

---
### 4. Đánh giá
- Dễ phát triển
- Thời gian triển khai nhanh
- Phù hợp cho prototype và microservice
