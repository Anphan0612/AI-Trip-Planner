# 05. Containerization

## 1. Giới thiệu
Chương này trình bày quá trình container hóa toàn bộ hệ thống nhằm chuẩn bị cho triển khai thực tế.

---

## 2. Mục tiêu
- Đóng gói hệ thống
- Đảm bảo chạy nhất quán mọi môi trường
- Sẵn sàng CI/CD

---

## 3. Phân tích theo 3 mức

### 3.1 Mức ý tưởng
Container giúp loại bỏ sự phụ thuộc môi trường.

---

### 3.2 Mức luận lý
- Dockerfile cho từng service
- Docker Compose điều phối hệ thống

---

### 3.3 Mức vật lý
- Backend Container
- Frontend Container
- Docker Network nội bộ

---

## 4. Sơ đồ container

```
[Frontend Container]
↓
Docker Network
↓
[Backend Container]
```

---

## 5. Đánh giá
Containerization giúp:
- Dễ triển khai
- Dễ mở rộng
- Phù hợp hệ thống hiện đại
