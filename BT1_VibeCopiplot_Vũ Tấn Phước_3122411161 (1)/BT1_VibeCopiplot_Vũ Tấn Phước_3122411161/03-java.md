# 03. Java Migration from Python

## 1. Giới thiệu
Chương này thực hiện migration backend từ Python sang Java nhằm đánh giá tính độc lập công nghệ của hệ thống.

---

## 2. Mục tiêu
- Giữ nguyên nghiệp vụ
- Thay đổi nền tảng triển khai
- So sánh Python và Java backend

---

## 3. Phân tích theo 3 mức

### 3.1 Mức ý tưởng
Migration giúp chứng minh hệ thống không phụ thuộc vào một ngôn ngữ cụ thể.

---

### 3.2 Mức luận lý
- Spring Boot
- Kiến trúc:
  - Controller
  - Service
  - Repository
- API contract không đổi

---

### 3.3 Mức vật lý
- JVM
- Port: `8080`
- Chạy bằng:
```bash
mvn spring-boot:run
```
---

### 4.Sơ đồ migration
```
Client
 ↓
Spring Boot Controller
 ↓
Service
 ↓
Response
```
---

### 5.Đánh giá
Backend Java:
- Ổn định
- Hiệu năng cao
- Phù hợp hệ thống lớn