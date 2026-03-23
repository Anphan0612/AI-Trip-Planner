# 04. .NET Migration from JavaScript

## 1. Giới thiệu
Chương này trình bày quá trình migration frontend từ JavaScript sang nền tảng .NET nhằm đánh giá khả năng phát triển giao diện web bằng công nghệ Microsoft.

---

## 2. Mục tiêu
- Chuyển đổi frontend sang .NET
- Giữ nguyên chức năng nghiệp vụ
- So sánh JavaScript frontend và .NET frontend

---

## 3. Phân tích theo 3 mức

### 3.1 Mức ý tưởng (Conceptual Level)
Migration frontend giúp chứng minh hệ thống không phụ thuộc vào một công nghệ giao diện duy nhất.

---

### 3.2 Mức luận lý (Logical Level)
Công nghệ sử dụng:
- ASP.NET Core
- Mô hình MVC:
  - Model: dữ liệu
  - View: giao diện
  - Controller: điều phối

Luồng xử lý:
1. Người dùng gửi yêu cầu
2. Controller xử lý
3. View hiển thị dữ liệu

---

### 3.3 Mức vật lý (Physical Level)
- .NET Runtime
- Web server Kestrel
- Chạy trên `localhost`

---

## 4. Sơ đồ kiến trúc frontend .NET

```
User
↓
ASP.NET View
↓
Controller
↓
Backend API
```

---

## 5. Đánh giá
Frontend .NET:
- Tích hợp tốt hệ sinh thái Microsoft
- Phù hợp hệ thống doanh nghiệp
- Dễ bảo trì và mở rộng
