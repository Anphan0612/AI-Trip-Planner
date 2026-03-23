# 02. JavaScript Frontend

## 1. Giới thiệu
Chương này trình bày quá trình xây dựng frontend bằng JavaScript trong workshop GitHub Copilot Vibe Coding. Frontend đóng vai trò giao diện người dùng, cho phép tương tác với hệ thống backend Python thông qua các API.

---

## 2. Mục tiêu
- Xây dựng giao diện web đơn giản, dễ sử dụng
- Kết nối và trao đổi dữ liệu với backend Python
- Tạo nền tảng để migration sang công nghệ khác

---

## 3. Phân tích theo 3 mức

### 3.1 Mức ý tưởng (Conceptual Level)
Frontend là lớp giao tiếp trực tiếp với người dùng, chịu trách nhiệm:
- Hiển thị dữ liệu
- Thu thập yêu cầu người dùng
- Gửi request đến backend

---

### 3.2 Mức luận lý (Logical Level)
Công nghệ và cấu trúc:
- HTML: cấu trúc giao diện
- CSS: định dạng và bố cục
- JavaScript: xử lý logic phía client
- Fetch API: gọi REST API từ backend

Luồng xử lý:
1. Người dùng thao tác giao diện
2. JavaScript gửi HTTP request
3. Nhận response và cập nhật UI

---

### 3.3 Mức vật lý (Physical Level)
- Chạy trực tiếp trên trình duyệt web
- Không cần server riêng
- Giao tiếp HTTP với backend tại `localhost:8000`

---

## 4. Sơ đồ kiến trúc frontend

```
User
↓
Web Browser
↓
JavaScript UI
↓
Backend API (Python)
```

---

### 5. Đánh giá
Frontend JavaScript có ưu điểm:
- Nhẹ, dễ triển khai
- Phù hợp ứng dụng web nhỏ
- Dễ dàng migration sang nền tảng khác
