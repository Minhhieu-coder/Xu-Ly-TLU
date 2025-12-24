# Ứng dụng Xử lý Ảnh - Image Processing Application

Ứng dụng xử lý ảnh với giao diện đồ họa (GUI) được xây dựng bằng Python, hỗ trợ các chức năng xử lý ảnh cơ bản và nâng cao.

## Tính năng chính

### 1. Đọc và Lưu Ảnh
- Tải ảnh từ máy tính (hỗ trợ PNG, JPG, JPEG, BMP, GIF)
- Lưu ảnh đã xử lý dưới các định dạng khác nhau

### 2. Chuyển đổi Ảnh
- **Ảnh Xám**: Chuyển đổi ảnh màu sang ảnh xám
- **Ma trận Ảnh Xám**: Hiển thị ma trận giá trị pixel của ảnh xám
- **Ảnh Nhị phân**: Chuyển đổi sang ảnh đen trắng với thanh trượt điều chỉnh ngưỡng (0-255)
- **Tách kênh màu**: Hiển thị riêng từng kênh RGB (Đỏ, Xanh lá, Xanh dương)
- **Kênh Alpha**: Kiểm tra và hiển thị kênh Alpha cho ảnh PNG

### 3. Tính toán Chỉ số Hình ảnh
- **Độ sáng trung bình**: Đo mức độ sáng tổng thể của ảnh
- **Độ tương phản**: Đo sự khác biệt giữa các mức xám (Standard Deviation, RMS, Michelson)
- **Entropy**: Đo lượng thông tin trong ảnh
- **Độ sắc nét**: Đo độ rõ nét của ảnh dựa trên gradient

### 4. Tăng cường Chất lượng Ảnh
- **Ảnh Âm bản**: Đảo ngược các giá trị pixel (s = 255 - r)
- **Biến đổi Logarit**: Tăng cường ảnh thiếu sáng (s = c · log(1 + r))
- **Biến đổi Logarit ngược**: Điều chỉnh ảnh dư sáng (r = e^(s/c) - 1)
- **Biến đổi Gamma**: Điều chỉnh độ sáng với tham số gamma có thể điều chỉnh (s = c · r^γ)

## Cài đặt

### Yêu cầu hệ thống
- Python 3.7 trở lên
- Tkinter (thường đi kèm với Python)

### Cài đặt các thư viện

```bash
pip install -r requirements.txt
```

Hoặc cài đặt thủ công:

```bash
pip install Pillow numpy matplotlib
```

## Sử dụng

### Chạy ứng dụng

```bash
python image_processing_app.py
```

### Hướng dẫn sử dụng

1. **Tải ảnh**: Nhấn nút "📂 Tải Ảnh" để chọn ảnh từ máy tính
2. **Chọn chức năng**: Sử dụng các tab và nút trong khu vực bên trái
   - **Tab "Chuyển đổi"**: Các chức năng chuyển đổi ảnh cơ bản
   - **Tab "Chỉ số"**: Tính toán các chỉ số hình ảnh
   - **Tab "Tăng cường"**: Các chức năng nâng cao chất lượng ảnh
3. **Xem kết quả**: Kết quả hiển thị ở khu vực bên phải
   - **Tab "Hiển thị Ảnh"**: Hiển thị ảnh đã xử lý
   - **Tab "Ma trận / Thông tin"**: Hiển thị ma trận hoặc thông tin chi tiết
4. **Lưu ảnh**: Nhấn nút "💾 Lưu Ảnh" để lưu kết quả

## Cấu trúc Giao diện

### Khu vực 1 (Trái - Trên): Tải và Lưu Ảnh
- Nút tải ảnh
- Nút lưu ảnh
- Hiển thị thông tin ảnh hiện tại

### Khu vực 2 (Trái - Dưới): Chức năng Xử lý
- Tab "Chuyển đổi": Các phép biến đổi ảnh cơ bản
- Tab "Chỉ số": Tính toán các chỉ số hình ảnh
- Tab "Tăng cường": Các chức năng tăng cường chất lượng

### Khu vực 3 (Bên phải): Hiển thị
- Tab "Hiển thị Ảnh": Canvas hiển thị ảnh
- Tab "Ma trận / Thông tin": Hiển thị dữ liệu chi tiết

## Công thức Toán học

### Ảnh Âm bản
```
s = 255 - r
```
Trong đó:
- r: giá trị pixel gốc
- s: giá trị pixel sau biến đổi

### Biến đổi Logarit
```
s = c · log(1 + r)
```
Trong đó:
- c: hằng số tỷ lệ (có thể điều chỉnh)
- Ứng dụng: Tăng cường ảnh thiếu sáng

### Biến đổi Logarit ngược
```
r = e^(s/c) - 1
```
Trong đó:
- c: hằng số tỷ lệ (có thể điều chỉnh)
- Ứng dụng: Điều chỉnh ảnh dư sáng

### Biến đổi Gamma
```
s = c · r^γ
```
Trong đó:
- γ (gamma): tham số điều chỉnh (có thể điều chỉnh từ 0.1 đến 3.0)
- γ < 1: Làm sáng ảnh
- γ = 1: Không thay đổi
- γ > 1: Làm tối ảnh

## Thư viện Sử dụng

- **Tkinter**: Tạo giao diện đồ họa
- **Pillow (PIL)**: Xử lý ảnh
- **NumPy**: Tính toán ma trận và các phép toán số học
- **Matplotlib**: Hỗ trợ hiển thị (tùy chọn)

## Tác giả

Minhhieu-coder

## Giấy phép

MIT License