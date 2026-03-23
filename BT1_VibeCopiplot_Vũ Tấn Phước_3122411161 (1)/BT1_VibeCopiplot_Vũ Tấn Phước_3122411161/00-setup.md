# 00. Development Environment

## 1. Giới thiệu
Chương này trình bày quá trình thiết lập môi trường phát triển cho toàn bộ dự án GitHub Copilot Vibe Coding. Đây là bước nền tảng, quyết định khả năng triển khai, mở rộng và migration hệ thống trong các chương tiếp theo.

---

## 2. Phân tích theo 3 mức

### 2.1 Mức ý tưởng (Conceptual Level)
Môi trường phát triển cần:
- Đồng nhất giữa các thành viên
- Hỗ trợ nhiều ngôn ngữ và nền tảng
- Tích hợp AI hỗ trợ lập trình

Mục tiêu là giúp lập trình viên **tập trung vào tư duy giải quyết bài toán**, thay vì mất thời gian xử lý lỗi môi trường.

---

### 2.2 Mức luận lý (Logical Level)
Các thành phần chính:
- **Git & GitHub**: quản lý mã nguồn, làm việc nhóm
- **GitHub Copilot**: AI hỗ trợ sinh mã và gợi ý giải pháp
- **Visual Studio Code**: IDE chính
- **Ngôn ngữ & SDK**:
  - Python
  - Node.js
  - Java (JDK)
  - .NET SDK

Các thành phần này tương tác với nhau thông qua IDE.

---

### 2.3 Mức vật lý (Physical Level)
- Máy tính cá nhân của từng thành viên
- Hệ điều hành: Windows / Linux / macOS
- Kết nối Internet để sử dụng Copilot
- Cài đặt và kiểm tra bằng CLI:
  - `python --version`
  - `node --version`
  - `java -version`
  - `dotnet --version`

---

## 3. Sơ đồ kiến trúc môi trường
```
Developer
↓
Visual Studio Code
↓
GitHub Copilot
↓
GitHub Repository
```


---

### 4. Đánh giá
Môi trường này đảm bảo:
- Tính linh hoạt
- Dễ mở rộng
- Phù hợp phát triển phần mềm hiện đại


