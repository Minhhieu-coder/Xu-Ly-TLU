# Bài 12: Bộ Lọc Thông Cao (High-Pass Filters)

## Tổng quan
Bài tập 12 hoàn thiện ứng dụng xử lý ảnh bằng cách thêm các bộ lọc thông cao (high-pass filters) trong miền tần số. Các bộ lọc này được sử dụng để làm nổi bật các cạnh và chi tiết trong ảnh.

## Chức năng đã triển khai

### 12.1: Bộ lọc Thông cao Lý tưởng (Ideal High-Pass Filter)
**Công thức:** `H_ideal_high = 1 - H_ideal_low`

**Cách hoạt động:**
- Tạo mặt nạ lọc với giá trị 1 (giữ nguyên tần số cao) và 0 (chặn tần số thấp)
- Chặn hoàn toàn các tần số có khoảng cách từ tâm ≤ D0
- Cho phép hoàn toàn các tần số có khoảng cách từ tâm > D0

**Ưu điểm:**
- Đơn giản, dễ hiểu
- Làm nổi bật cạnh rõ ràng

**Nhược điểm:**
- Chuyển tiếp đột ngột gây hiện tượng ringing (vòng tròn lan truyền)
- Có thể tạo ra các artifact không mong muốn

**Tham số:**
- `cutoff_frequency` (D0): Bán kính ngưỡng cắt (10-100)
  - D0 nhỏ: Giữ nhiều tần số cao → cạnh rõ nét hơn
  - D0 lớn: Giữ ít tần số cao → cạnh mềm hơn

### 12.2: Bộ lọc Thông cao Butterworth
**Công thức:** `H(u,v) = 1 / (1 + (D0/D(u,v))^(2n))`

**Cách hoạt động:**
- Tạo mặt nạ lọc với chuyển tiếp mượt mà giữa 0 và 1
- Sử dụng hàm Butterworth để tạo gradient mềm
- Không có ngưỡng cắt đột ngột như bộ lọc lý tưởng

**Ưu điểm:**
- Chuyển tiếp mượt mà, giảm hiện tượng ringing
- Kết quả tự nhiên hơn
- Điều chỉnh được độ sắc nét qua tham số n

**Nhược điểm:**
- Phức tạp hơn bộ lọc lý tưởng
- Tính toán lâu hơn một chút

**Tham số:**
- `D0`: Tần số cắt (10-100)
- `n`: Bậc của bộ lọc (1-10)
  - n nhỏ (1-2): Chuyển tiếp rất mượt
  - n lớn (5-10): Chuyển tiếp sắc nét hơn, gần với lý tưởng

## So sánh Ideal vs Butterworth

| Đặc điểm | Ideal High-Pass | Butterworth High-Pass |
|----------|-----------------|----------------------|
| Chuyển tiếp | Đột ngột (0→1) | Mượt mà (gradient) |
| Ringing | Có thể có nhiều | Ít hơn đáng kể |
| Tính toán | Đơn giản, nhanh | Phức tạp hơn một chút |
| Kết quả | Cạnh rất sắc nét | Cạnh tự nhiên hơn |
| Khuyến nghị | Demo, giáo dục | Ứng dụng thực tế |

## Cách sử dụng

### 1. Trong Python code

```python
from image_processing import ImageProcessor
import cv2

# Tải ảnh
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Áp dụng Ideal High-pass
ideal_result = ImageProcessor.ideal_highpass_filter(image, cutoff_frequency=30)

# Áp dụng Butterworth High-pass
butter_result = ImageProcessor.butterworth_highpass_filter(image, D0=30, n=2)

# Lưu kết quả
cv2.imwrite('ideal_highpass.jpg', ideal_result)
cv2.imwrite('butterworth_highpass.jpg', butter_result)
```

### 2. Trong GUI

1. Mở ứng dụng: `python comprehensive_app.py`
2. Tải ảnh qua nút "📂 Tải Ảnh"
3. Chuyển sang tab "Bài 12: High-Pass"
4. Chọn bộ lọc:
   - **Ideal High-pass**: Điều chỉnh D0 (10-100)
   - **Butterworth High-pass**: Điều chỉnh D0 (10-100) và n (1-10)
5. Nhấn nút "Apply" tương ứng

### 3. Chạy Demo

```bash
# Chạy demo để tạo ảnh so sánh
python demo_highpass.py

# Kiểm tra kết quả
# - bai12_ideal_highpass_comparison.png
# - bai12_butterworth_highpass_comparison.png
# - bai12_ideal_vs_butterworth.png
```

### 4. Chạy Test

```bash
# Kiểm tra các hàm lọc
python test_highpass.py
```

## Công thức toán học

### Bộ lọc Ideal High-pass
```
H(u,v) = { 0  nếu D(u,v) ≤ D0
         { 1  nếu D(u,v) > D0

Trong đó:
D(u,v) = √[(u - M/2)² + (v - N/2)²]
M, N: Kích thước ảnh
D0: Bán kính ngưỡng cắt
```

### Bộ lọc Butterworth High-pass
```
H(u,v) = 1 / [1 + (D0/D(u,v))^(2n)]

Trong đó:
D(u,v) = √[(u - M/2)² + (v - N/2)²]
D0: Tần số cắt
n: Bậc của bộ lọc
```

## Quy trình xử lý

1. **Biến đổi Fourier**: Chuyển ảnh từ miền không gian sang miền tần số
   ```python
   F = fft2(image)
   F_shifted = fftshift(F)  # Dịch tâm về giữa
   ```

2. **Tạo mặt nạ lọc**: Tạo H(u,v) theo công thức
   ```python
   mask = create_highpass_mask(rows, cols, D0, ...)
   ```

3. **Áp dụng lọc**: Nhân phổ với mặt nạ
   ```python
   F_filtered = F_shifted * mask
   ```

4. **Biến đổi ngược**: Chuyển về miền không gian
   ```python
   F_ishifted = ifftshift(F_filtered)
   result = abs(ifft2(F_ishifted))
   ```

## Ví dụ kết quả

### Input: Ảnh với các hình học
- Circle (đường tròn)
- Rectangle (hình chữ nhật)
- Triangle (tam giác)
- Star (ngôi sao)

### Output với Ideal High-pass (D0=30):
- Chỉ còn các cạnh/đường viền
- Nền đen (tần số thấp bị loại)
- Có thể thấy vòng tròn ringing quanh các cạnh sắc

### Output với Butterworth High-pass (D0=30, n=2):
- Cạnh/đường viền mượt hơn
- Ít ringing hơn
- Kết quả tự nhiên hơn

## Lưu ý khi sử dụng

1. **Chọn D0 phù hợp:**
   - D0 nhỏ (10-20): Giữ nhiều chi tiết, nhiễu có thể tăng
   - D0 trung bình (30-50): Cân bằng
   - D0 lớn (60-100): Chỉ giữ cạnh rất rõ nét

2. **Chọn bậc n cho Butterworth:**
   - n=1: Rất mượt, ít ringing
   - n=2: Cân bằng (khuyến nghị)
   - n≥5: Gần với ideal, có thể có ringing

3. **Ứng dụng:**
   - Phát hiện cạnh
   - Tăng cường chi tiết
   - Làm nổi bật đường viền
   - Loại bỏ thành phần tần số thấp (nền đồng nhất)

## Tham khảo

- Rafael C. Gonzalez, Richard E. Woods. "Digital Image Processing", 4th Edition
- Chương 4: Filtering in the Frequency Domain
- GitHub references (trong problem statement)

## Files liên quan

- `image_processing.py`: Chứa hàm `ideal_highpass_filter()` và `butterworth_highpass_filter()`
- `comprehensive_app.py`: GUI tích hợp bộ lọc
- `test_highpass.py`: Unit tests
- `demo_highpass.py`: Script demo với visualization
