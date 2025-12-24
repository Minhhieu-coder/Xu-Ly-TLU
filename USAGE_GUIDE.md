# Hướng dẫn Sử dụng Chi tiết - Ứng dụng Xử lý Ảnh

## Giới thiệu
Ứng dụng xử lý ảnh này cung cấp các công cụ toàn diện cho xử lý ảnh từ cơ bản đến nâng cao, bao gồm cân bằng độ tương phản, histogram, khử nhiễu, dò biên và làm nét ảnh.

## Cài đặt và Khởi chạy

### 1. Cài đặt môi trường
```bash
# Clone repository
git clone https://github.com/Minhhieu-coder/Xu-Ly-TLU.git
cd Xu-Ly-TLU

# Cài đặt dependencies
pip install -r requirements.txt
```

### 2. Chạy ứng dụng GUI
```bash
python main.py
```

### 3. Chạy test và tạo ảnh mẫu
```bash
# Tạo ảnh mẫu và chạy test
python test_processing.py

# Tạo demo visualization
python create_demo.py
```

## Hướng dẫn Chi tiết Từng Chức năng

### Bài 4: Kéo dãn độ tương phản (Contrast Stretching)

#### 1. Linear Stretching
**Mục đích**: Mở rộng dải động của ảnh về toàn bộ khoảng [0, 255]

**Cách sử dụng**:
1. Load ảnh có độ tương phản thấp
2. Click "Linear Stretching"
3. Ảnh sẽ được kéo dãn tự động

**Công thức**: `s = (r - r_min) / (r_max - r_min) * 255`

**Khi nào sử dụng**:
- Ảnh có độ tương phản thấp
- Các giá trị pixel tập trung trong khoảng hẹp
- Cần cải thiện độ tương phản toàn cục

#### 2. Type 1 Clipping
**Mục đích**: Cắt bỏ các giá trị ngoài ngưỡng và kéo dãn

**Cách sử dụng**:
1. Load ảnh
2. Click "Type 1 Clipping"
3. Nhập ngưỡng thấp (low threshold) và ngưỡng cao (high threshold)
4. Click "Apply"

**Tham số đề xuất**:
- Ảnh tối: Low=30, High=220
- Ảnh sáng: Low=50, High=200
- Ảnh cân bằng: Low=40, High=240

#### 3. Type 2 Clipping
**Mục đích**: Xử lý riêng 3 vùng sáng (tối, trung bình, sáng)

**Cách sử dụng**:
1. Load ảnh có nhiều vùng sáng tối khác nhau
2. Click "Type 2 Clipping"

**Ngưỡng mặc định**:
- Vùng tối: [0, 85]
- Vùng trung bình: [86, 170]
- Vùng sáng: [171, 255]

### Bài 5: Cân bằng Histogram Tiêu chuẩn

#### Standard Equalization
**Mục đích**: Phân bố lại histogram để tăng độ tương phản

**Cách sử dụng**:
1. Load ảnh
2. Click "Standard Equalization"
3. Xem kết quả trực tiếp

**Khi nào sử dụng**:
- Ảnh có histogram tập trung ở một vùng
- Cần cải thiện độ tương phản tổng thể
- Ảnh y tế, ảnh vệ tinh

#### Show Histogram
**Mục đích**: So sánh histogram trước và sau xử lý

**Cách sử dụng**:
1. Load ảnh và áp dụng bất kỳ xử lý nào
2. Click "Show Histogram"
3. Cửa sổ mới hiển thị 2 histogram song song

**Phân tích**:
- Histogram gốc tập trung → cần equalization
- Histogram đều → ảnh có độ tương phản tốt

### Bài 6: Histogram Matching & Adaptive Equalization

#### Histogram Matching
**Mục đích**: Khớp histogram ảnh với histogram mẫu

**Cách sử dụng**:
1. Load ảnh nguồn
2. Click "Histogram Matching"
3. Ứng dụng sử dụng Gaussian distribution làm histogram tham chiếu

**Ứng dụng**:
- Chuẩn hóa nhiều ảnh chụp trong điều kiện khác nhau
- Tạo phong cách ảnh nhất quán
- Xử lý ảnh y tế

#### Adaptive Equalization (CLAHE)
**Mục đích**: Cân bằng histogram cục bộ, tránh over-amplification

**Cách sử dụng**:
1. Load ảnh
2. Click "Adaptive Equalization"

**Tham số mặc định**:
- Clip limit: 2.0
- Tile grid size: 8x8

**Ưu điểm so với Standard Equalization**:
- Bảo toàn chi tiết cục bộ
- Không tạo quá nhiều nhiễu
- Tốt cho ảnh có vùng sáng tối đan xen

### Bài 7: Phép nhân chập và Khử nhiễu

#### Thêm Nhiễu Salt & Pepper
**Mục đích**: Tạo nhiễu để test các bộ lọc

**Cách sử dụng**:
1. Load ảnh gốc
2. Click "Add Salt & Pepper Noise"
3. Nhiễu được thêm với xác suất mặc định 2% salt + 2% pepper

#### Average Filter 3x3 / 5x5
**Mục đích**: Làm mịn ảnh bằng trung bình cục bộ

**Cách sử dụng**:
1. Load ảnh nhiễu
2. Click "Average Filter 3x3" hoặc "Average Filter 5x5"

**So sánh**:
- 3x3: Nhanh hơn, giữ biên tốt hơn
- 5x5: Mịn hơn, loại nhiễu tốt hơn

**Nhược điểm**: Làm mờ cả biên

#### Median Filter 3x3 / 5x5
**Mục đích**: Khử nhiễu muối tiêu hiệu quả

**Cách sử dụng**:
1. Load ảnh nhiễu muối tiêu
2. Click "Median Filter 3x3" hoặc "Median Filter 5x5"

**Ưu điểm**:
- Rất hiệu quả với nhiễu muối tiêu
- Bảo toàn biên tốt hơn Average Filter
- Không làm mờ chi tiết

**Khuyến nghị**:
- Nhiễu nhẹ: Median 3x3
- Nhiễu nặng: Median 5x5

### Bài 8: Dò biên Nâng cao

#### Sobel Operator
**Mục đích**: Dò biên bằng toán tử Sobel (phổ biến nhất)

**Cách sử dụng**:
1. Load ảnh
2. Click "Sobel"

**Đặc điểm**:
- Kernel 3x3 với trọng số
- Tốt cho biên mạnh
- Ít nhạy với nhiễu
- Sử dụng rộng rãi nhất

#### Prewitt Operator
**Mục đích**: Dò biên tương tự Sobel

**Cách sử dụng**:
1. Load ảnh
2. Click "Prewitt"

**So sánh với Sobel**:
- Kernel đơn giản hơn (không có trọng số 2)
- Ít nhạy hơn một chút
- Tính toán nhanh hơn

#### Roberts Operator
**Mục đích**: Dò biên chéo với kernel 2x2

**Cách sử dụng**:
1. Load ảnh
2. Click "Roberts"

**Đặc điểm**:
- Kernel 2x2 nhỏ nhất
- Tốt cho biên chéo
- Nhạy với nhiễu
- Nhanh nhất

#### Kirsch Operator
**Mục đích**: Dò biên theo 8 hướng

**Cách sử dụng**:
1. Load ảnh
2. Click "Kirsch"

**Đặc điểm**:
- 8 kernel cho 8 hướng
- Chi tiết nhất
- Chậm nhất
- Tốt cho phân tích hướng biên

**So sánh tổng quan**:
| Operator | Tốc độ | Độ chính xác | Nhạy nhiễu | Ứng dụng |
|----------|--------|--------------|------------|----------|
| Roberts  | Nhanh nhất | Thấp | Cao | Biên chéo |
| Prewitt  | Nhanh | Trung bình | Trung bình | Đa dụng |
| Sobel    | Trung bình | Cao | Thấp | Đa dụng, phổ biến |
| Kirsch   | Chậm | Rất cao | Trung bình | Phân tích hướng |

### Bài 9: Laplacian và Làm nét Ảnh

#### Laplacian 4-neighbor
**Mục đích**: Dò biên bậc 2 với 4 hàng xóm

**Cách sử dụng**:
1. Load ảnh
2. Click "Laplacian 4-neighbor"

**Kernel**:
```
[ 0  1  0]
[ 1 -4  1]
[ 0  1  0]
```

**Đặc điểm**:
- Phát hiện biên theo 4 hướng chính
- Nhạy với nhiễu
- Đơn giản, nhanh

#### Laplacian 8-neighbor
**Mục đích**: Dò biên bậc 2 với 8 hàng xóm

**Cách sử dụng**:
1. Load ảnh
2. Click "Laplacian 8-neighbor"

**Kernel**:
```
[ 1  1  1]
[ 1 -8  1]
[ 1  1  1]
```

**Đặc điểm**:
- Phát hiện biên theo 8 hướng
- Nhạy hơn 4-neighbor
- Chi tiết hơn

#### LoG (Laplacian of Gaussian)
**Mục đích**: Giảm nhiễu bằng Gaussian trước khi Laplacian

**Cách sử dụng**:
1. Load ảnh
2. Click "LoG (Laplacian of Gaussian)"

**Quy trình**:
1. Gaussian blur (σ=1.4)
2. Laplacian 8-neighbor

**Ưu điểm**:
- Ít nhiễu hơn Laplacian thuần
- Biên mượt mà hơn
- Tốt cho ảnh có nhiễu

#### Sharpen (Laplacian)
**Mục đích**: Làm nét ảnh bằng Laplacian

**Cách sử dụng**:
1. Load ảnh mờ
2. Click "Sharpen (Laplacian)"

**Công thức**: `sharpened = original - laplacian`

**Hiệu quả**:
- Tăng độ sắc nét biên
- Làm rõ chi tiết
- Có thể tăng nhiễu

#### Sharpen (LoG)
**Mục đích**: Làm nét mượt mà hơn

**Cách sử dụng**:
1. Load ảnh mờ
2. Click "Sharpen (LoG)"

**Quy trình**:
1. Gaussian blur
2. Laplacian
3. Trừ khỏi ảnh gốc

**Ưu điểm so với Sharpen (Laplacian)**:
- Ít nhiễu hơn
- Kết quả mượt mà hơn
- Tốt cho ảnh nhiễu

## Quy trình Xử lý Đề xuất

### 1. Ảnh có độ tương phản thấp
```
Load ảnh → Linear Stretching → Adaptive Equalization → Sharpen (LoG)
```

### 2. Ảnh nhiễu muối tiêu
```
Load ảnh → Median Filter 5x5 → Contrast Stretching → (Optional) Sharpen
```

### 3. Dò biên chất lượng cao
```
Load ảnh → (Optional) Median Filter 3x3 → Sobel/Kirsch
```

### 4. Ảnh y tế/khoa học
```
Load ảnh → CLAHE → LoG Edge Detection hoặc Sharpen (LoG)
```

### 5. Chuẩn hóa nhiều ảnh
```
Load ảnh → Histogram Matching → Contrast Stretching
```

## Tips và Tricks

### 1. Thứ tự xử lý quan trọng
- Khử nhiễu TRƯỚC khi dò biên
- Cân bằng độ tương phản TRƯỚC khi làm nét
- Làm nét là bước CUỐI CÙNG

### 2. Chọn bộ lọc phù hợp
- Salt & Pepper noise → Median Filter
- Gaussian noise → Average Filter
- Mixed noise → Median rồi Average

### 3. Dò biên hiệu quả
- Ảnh ít nhiễu → Roberts (nhanh)
- Ảnh thông thường → Sobel (cân bằng)
- Cần chi tiết → Kirsch (chậm nhưng tốt)

### 4. Làm nét cẩn thận
- Ảnh sạch → Sharpen (Laplacian)
- Ảnh có nhiễu → Sharpen (LoG)
- Không sharpen ảnh đã có nhiễu nhiều

### 5. So sánh kết quả
- Luôn giữ ảnh gốc để so sánh
- Thử nhiều phương pháp khác nhau
- Sử dụng "Show Histogram" để phân tích

## Khắc phục Sự cố

### Ảnh quá sáng/tối sau equalization
→ Dùng CLAHE thay vì Standard Equalization

### Còn nhiễu sau median filter
→ Tăng kernel size (3x3 → 5x5)

### Biên quá mỏng/yếu
→ Thử Kirsch hoặc tăng độ tương phản trước

### Ảnh bị mờ sau average filter
→ Dùng median filter hoặc giảm kernel size

### Sharpen tạo quá nhiều nhiễu
→ Dùng Sharpen (LoG) thay vì Sharpen (Laplacian)

## Phím tắt (trong GUI)
- Ctrl+O: Load Image (không có, nhưng có thể thêm)
- Ctrl+S: Save Result (không có, nhưng có thể thêm)

## Hiệu suất

### Tốc độ xử lý (ảnh 256x256):
- Contrast operations: < 0.01s
- Histogram operations: < 0.1s
- Filters 3x3: < 0.1s
- Filters 5x5: < 0.2s
- Edge detection: < 0.2s
- Kirsch: < 0.5s (chậm nhất)

### Khuyến nghị kích thước ảnh:
- Tối ưu: 256x256 đến 512x512
- Tốt: 512x512 đến 1024x1024
- Chấp nhận được: 1024x1024 đến 2048x2048
- Chậm: > 2048x2048

## Tài liệu Tham khảo

1. **Digital Image Processing** - Gonzalez & Woods
2. **Computer Vision: Algorithms and Applications** - Richard Szeliski
3. OpenCV Documentation
4. SciPy Documentation

## Hỗ trợ

Nếu gặp vấn đề:
1. Kiểm tra console/terminal xem có lỗi không
2. Đảm bảo ảnh đầu vào là grayscale hoặc sẽ được convert tự động
3. Thử với ảnh mẫu trong `sample_images/`
4. Xem demo trong `demo_results/`

Repository: https://github.com/Minhhieu-coder/Xu-Ly-TLU
