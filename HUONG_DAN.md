# Hướng dẫn Sử dụng Chi tiết - Image Processing Application

## Giới thiệu

Ứng dụng Xử lý Ảnh là một công cụ toàn diện để thực hiện các thao tác xử lý ảnh cơ bản và nâng cao với giao diện đồ họa thân thiện.

## Cài đặt và Khởi động

### 1. Cài đặt Python và Dependencies

```bash
# Cài đặt các thư viện cần thiết
pip install -r requirements.txt
```

### 2. Chạy ứng dụng

```bash
python image_processing_app.py
```

## Giao diện Ứng dụng

Giao diện được chia thành 3 khu vực chính:

### Khu vực 1: Tải và Lưu Ảnh (Trái - Trên)
- **Nút "📂 Tải Ảnh"**: Click để chọn ảnh từ máy tính
- **Nút "💾 Lưu Ảnh"**: Lưu ảnh đã xử lý
- **Thông tin ảnh**: Hiển thị tên file, kích thước, và mode của ảnh

### Khu vực 2: Chức năng Xử lý (Trái - Dưới)
Có 3 tabs:

#### Tab "Chuyển đổi"
- **🎨 Ảnh Gốc**: Hiển thị lại ảnh gốc
- **⚫ Ảnh Xám**: Chuyển ảnh màu sang ảnh xám
- **📊 Ma trận Ảnh Xám**: Hiển thị ma trận số của ảnh xám
- **Thanh trượt Ngưỡng**: Điều chỉnh ngưỡng cho ảnh nhị phân (0-255)
- **⚪ Chuyển sang Nhị phân**: Tạo ảnh đen trắng với ngưỡng đã chọn
- **🔴 Kênh Đỏ (Red)**: Hiển thị chỉ kênh màu đỏ
- **🟢 Kênh Xanh lá (Green)**: Hiển thị chỉ kênh màu xanh lá
- **🔵 Kênh Xanh dương (Blue)**: Hiển thị chỉ kênh màu xanh dương
- **👁️ Kênh Alpha (PNG)**: Hiển thị kênh Alpha (chỉ cho ảnh PNG)

#### Tab "Chỉ số"
- **📊 Độ sáng trung bình**: Tính mức độ sáng trung bình của ảnh
- **📊 Độ tương phản**: Tính độ tương phản (Standard Deviation, RMS, Michelson)
- **📊 Entropy**: Tính lượng thông tin trong ảnh
- **📊 Độ sắc nét**: Tính độ rõ nét dựa trên gradient
- **📊 Tất cả các chỉ số**: Hiển thị tất cả các chỉ số cùng một lúc

#### Tab "Tăng cường"
- **🔄 Ảnh Âm bản (Negative)**: Đảo ngược màu sắc
- **Thanh trượt c (logarit)**: Điều chỉnh hệ số c cho biến đổi logarit
- **☀️ Biến đổi Logarit**: Tăng cường ảnh thiếu sáng
- **Thanh trượt c (logarit ngược)**: Điều chỉnh hệ số c cho logarit ngược
- **🌙 Biến đổi Logarit ngược**: Điều chỉnh ảnh dư sáng
- **Thanh trượt Gamma (γ)**: Điều chỉnh giá trị gamma (0.1 - 3.0)
- **⚡ Biến đổi Gamma**: Điều chỉnh độ sáng tổng thể

### Khu vực 3: Hiển thị (Bên phải)
Có 2 tabs:

#### Tab "Hiển thị Ảnh"
- Canvas lớn hiển thị ảnh gốc hoặc ảnh đã xử lý
- Ảnh tự động co dãn để vừa với màn hình

#### Tab "Ma trận / Thông tin"
- Hiển thị ma trận pixel (cho ảnh nhỏ)
- Hiển thị thông tin chi tiết về các chỉ số
- Hiển thị công thức và giải thích

## Hướng dẫn Từng bước

### 1. Tải và Hiển thị Ảnh

1. Click nút "📂 Tải Ảnh"
2. Chọn file ảnh (PNG, JPG, BMP, GIF)
3. Ảnh sẽ hiển thị ở khu vực bên phải
4. Thông tin ảnh xuất hiện ở khu vực trên bên trái

### 2. Chuyển đổi sang Ảnh Xám

1. Click nút "⚫ Ảnh Xám"
2. Ảnh xám sẽ hiển thị ở canvas
3. Click "📊 Ma trận Ảnh Xám" để xem ma trận số

### 3. Tạo Ảnh Nhị phân

1. Điều chỉnh thanh trượt "Ngưỡng" (0-255)
2. Giá trị ngưỡng hiển thị bên dưới thanh trượt
3. Click "⚪ Chuyển sang Nhị phân"
4. Ảnh nhị phân (đen trắng) sẽ hiển thị

**Lưu ý**: 
- Ngưỡng thấp (0-85): Nhiều pixel trắng
- Ngưỡng trung bình (86-170): Cân bằng
- Ngưỡng cao (171-255): Nhiều pixel đen

### 4. Tách Kênh Màu

1. Click một trong các nút: "🔴 Kênh Đỏ", "🟢 Kênh Xanh lá", hoặc "🔵 Kênh Xanh dương"
2. Ảnh hiển thị chỉ với kênh màu đó
3. Các kênh khác được đặt về 0

### 5. Kiểm tra Kênh Alpha

1. Tải ảnh PNG có độ trong suốt
2. Click "👁️ Kênh Alpha (PNG)"
3. Nếu ảnh có kênh Alpha, nó sẽ hiển thị dưới dạng ảnh xám
4. Ma trận Alpha hiển thị ở tab "Ma trận / Thông tin"

**Lưu ý**: Chỉ ảnh PNG với độ trong suốt mới có kênh Alpha

### 6. Tính Chỉ số Hình ảnh

#### Độ sáng trung bình
- Click "📊 Độ sáng trung bình"
- Kết quả hiển thị ở tab "Ma trận / Thông tin"
- Giải thích:
  - < 85: Ảnh tối
  - 85-170: Trung bình
  - > 170: Sáng

#### Độ tương phản
- Click "📊 Độ tương phản"
- Hiển thị 3 loại: Standard Deviation, RMS Contrast, Michelson Contrast
- Giá trị cao = tương phản cao

#### Entropy
- Click "📊 Entropy"
- Đo lượng thông tin trong ảnh
- Entropy cao = nhiều chi tiết

#### Độ sắc nét
- Click "📊 Độ sắc nét"
- Đo độ rõ nét của ảnh
- Giá trị cao = ảnh sắc nét

#### Tất cả các chỉ số
- Click "📊 Tất cả các chỉ số"
- Hiển thị tất cả 4 chỉ số cùng một lúc

### 7. Tăng cường Chất lượng Ảnh

#### Ảnh Âm bản
1. Click "🔄 Ảnh Âm bản (Negative)"
2. Ảnh âm bản hiển thị (vùng sáng thành tối và ngược lại)
3. Công thức: s = 255 - r

#### Biến đổi Logarit (cho ảnh thiếu sáng)
1. Điều chỉnh thanh trượt "c" (0.1 - 3.0)
2. Click "☀️ Biến đổi Logarit"
3. Ảnh sẽ sáng hơn, đặc biệt ở vùng tối
4. Công thức: s = c · log(1 + r)

**Tip**: 
- c nhỏ (< 1): Hiệu ứng nhẹ
- c lớn (> 1): Hiệu ứng mạnh

#### Biến đổi Logarit ngược (cho ảnh dư sáng)
1. Điều chỉnh thanh trượt "c" (0.1 - 3.0)
2. Click "🌙 Biến đổi Logarit ngược"
3. Giúp cân bằng ảnh quá sáng
4. Công thức: r = e^(s/c) - 1

#### Biến đổi Gamma
1. Điều chỉnh thanh trượt "Gamma (γ)" (0.1 - 3.0)
2. Click "⚡ Biến đổi Gamma"
3. Công thức: s = c · r^γ

**Giải thích Gamma**:
- γ < 1 (0.1 - 0.9): Làm sáng ảnh
- γ = 1: Không thay đổi
- γ > 1 (1.1 - 3.0): Làm tối ảnh

**Ví dụ**:
- γ = 0.5: Ảnh sáng hơn đáng kể
- γ = 2.0: Ảnh tối hơn đáng kể

### 8. Lưu Ảnh Đã Xử lý

1. Sau khi xử lý ảnh, click "💾 Lưu Ảnh"
2. Chọn vị trí và tên file
3. Chọn định dạng (PNG, JPG, BMP)
4. Click "Lưu"

## Các Công thức Toán học

### 1. Ảnh Âm bản
```
s = 255 - r
```
- r: giá trị pixel gốc (0-255)
- s: giá trị pixel sau biến đổi (0-255)

### 2. Biến đổi Logarit
```
s = c · log(1 + r)
```
- c: hằng số tỷ lệ (có thể điều chỉnh 0.1-3.0)
- r: giá trị pixel gốc
- s: giá trị pixel sau biến đổi (được chuẩn hóa về 0-255)

### 3. Biến đổi Logarit ngược
```
r = e^(s/c) - 1
```
- c: hằng số tỷ lệ (có thể điều chỉnh 0.1-3.0)
- s: giá trị pixel gốc
- r: giá trị pixel sau biến đổi (được chuẩn hóa về 0-255)

### 4. Biến đổi Gamma
```
s = c · r^γ
```
- γ (gamma): tham số điều chỉnh (0.1-3.0)
- c: hằng số (thường = 1)
- r: giá trị pixel gốc (chuẩn hóa 0-1)
- s: giá trị pixel sau biến đổi

## Các Chỉ số Hình ảnh

### 1. Độ sáng trung bình (Average Brightness)
```
Brightness = mean(pixel_values)
```
Giá trị: 0-255

### 2. Độ tương phản (Contrast)
```
Contrast = std(pixel_values)
RMS Contrast = sqrt(mean((pixels - mean)^2))
Michelson = (max - min) / (max + min)
```

### 3. Entropy
```
Entropy = -Σ(p_i · log2(p_i))
```
- p_i: xác suất của mức xám i
- Giá trị: 0-8 bits (cho ảnh 256 mức xám)

### 4. Độ sắc nét (Sharpness)
```
Sharpness = mean(sqrt(gx^2 + gy^2))
```
- gx, gy: gradient theo x và y

## Tips và Tricks

### Xử lý Ảnh Tối
1. Thử "Biến đổi Logarit" với c = 1.0-2.0
2. Hoặc "Biến đổi Gamma" với γ = 0.5-0.8

### Xử lý Ảnh Sáng
1. Thử "Biến đổi Logarit ngược" với c = 1.0-2.0
2. Hoặc "Biến đổi Gamma" với γ = 1.2-2.0

### Tạo Hiệu ứng Nghệ thuật
- Ảnh âm bản: Hiệu ứng negative film
- Kênh màu đơn: Hiệu ứng đơn sắc
- Ảnh nhị phân: Hiệu ứng sketch, line art

### Phân tích Ảnh
- Sử dụng "Tất cả các chỉ số" để đánh giá chất lượng ảnh
- Entropy cao: Ảnh phức tạp, nhiều chi tiết
- Entropy thấp: Ảnh đơn giản, ít chi tiết

## Khắc phục Sự cố

### Không tải được ảnh
- Kiểm tra định dạng file (PNG, JPG, BMP, GIF)
- Kiểm tra quyền truy cập file

### Kênh Alpha không hiển thị
- Chỉ ảnh PNG với độ trong suốt có kênh Alpha
- Thử với ảnh PNG khác

### Ma trận quá lớn
- Ứng dụng tự động giới hạn hiển thị 50x50 pixel đầu tiên
- Thống kê vẫn tính cho toàn bộ ảnh

## Lưu ý Kỹ thuật

- Tất cả biến đổi đều làm việc trên ảnh xám
- Ảnh được tự động chuyển sang xám nếu cần
- Kết quả được chuẩn hóa về [0, 255]
- Ma trận lớn (> 50x50) chỉ hiển thị một phần

## Hỗ trợ

Nếu gặp vấn đề, vui lòng:
1. Kiểm tra Python version >= 3.7
2. Kiểm tra đã cài đặt đầy đủ dependencies
3. Thử với ảnh test đơn giản

---

**Chúc bạn sử dụng ứng dụng vui vẻ!** 🎨📸
