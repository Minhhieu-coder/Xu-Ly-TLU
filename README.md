# Ứng dụng Xử lý Ảnh - Bài 4-9

Ứng dụng xử lý ảnh toàn diện với giao diện đồ họa (GUI) được phát triển bằng Python, tích hợp các kỹ thuật xử lý ảnh nâng cao từ Bài 4 đến Bài 9.

## Tính năng

### Bài 4: Kéo dãn độ tương phản (Contrast Stretching)
- **Linear Stretching**: Biến đổi tuyến tính kéo dãn toàn bộ mức xám về khoảng [0, 255]
  - Công thức: `s = (r - r_min) / (r_max - r_min) * 255`
- **Type 1 Clipping**: Điều chỉnh ngưỡng tùy chỉnh [r_min, r_max]
- **Type 2 Clipping**: Xử lý chi tiết từng vùng ánh sáng khác nhau (tối, trung bình, sáng)

### Bài 5: Cân bằng Histogram tiêu chuẩn
- Tính histogram ảnh gốc
- Tính hàm phân bố tích lũy (CDF - Cumulative Distribution Function)
- Biến đổi mức xám dựa trên CDF
- Hiển thị ảnh gốc, ảnh sau cân bằng và biểu đồ histogram

### Bài 6: Histogram Matching và Cân bằng cục bộ
- **Histogram Matching**: Khớp histogram ảnh với histogram tham chiếu
- **Adaptive Equalization (CLAHE)**: Cân bằng histogram cục bộ, nâng cao chi tiết từng vùng

### Bài 7: Phép nhân chập và Khử nhiễu
- Tự xây dựng phép nhân chập 2D với ma trận kernel
- **Average Filter**: Bộ lọc trung bình (3x3, 5x5) để khử nhiễu
- **Median Filter**: Bộ lọc trung vị (3x3, 5x5) hiệu quả với nhiễu muối tiêu
- Công cụ thêm nhiễu muối tiêu để kiểm tra

### Bài 8: Dò biên nâng cao
Các toán tử dò biên bậc 1:
- **Sobel Operator**: Toán tử Sobel với kernel 3x3
- **Prewitt Operator**: Toán tử Prewitt 
- **Roberts Operator**: Toán tử Roberts với kernel 2x2
- **Kirsch Operator**: 8 kernel hướng khác nhau
- Tổng hợp biên bằng công thức gradient magnitude

### Bài 9: Dò biên Laplace và Làm nét ảnh
- **Laplacian 4-neighbor**: Kernel Laplace với 4 hàng xóm
- **Laplacian 8-neighbor**: Kernel Laplace với 8 hàng xóm  
- **Laplacian of Gaussian (LoG)**: Làm mịn Gaussian trước khi áp dụng Laplace
- **Image Sharpening**: Làm nét ảnh bằng cách cộng/trừ Laplacian vào ảnh gốc

## Cài đặt

### Yêu cầu hệ thống
- Python 3.8 trở lên
- pip (Python package manager)

### Cài đặt thư viện

```bash
pip install -r requirements.txt
```

Các thư viện cần thiết:
- numpy: Xử lý mảng và ma trận
- opencv-python: Xử lý ảnh cơ bản
- Pillow: Hiển thị ảnh trong GUI
- matplotlib: Vẽ biểu đồ histogram
- scipy: Các hàm toán học nâng cao

## Sử dụng

### Chạy ứng dụng

```bash
python main.py
```

### Hướng dẫn sử dụng

1. **Load Image**: Tải ảnh từ file (hỗ trợ JPG, PNG, BMP, TIFF)
2. **Chọn chức năng**: Click vào các nút tương ứng với chức năng muốn áp dụng
3. **Xem kết quả**: Ảnh được xử lý hiển thị trên canvas chính
4. **Save Result**: Lưu ảnh đã xử lý

### Quy trình làm việc điển hình

#### Khử nhiễu muối tiêu:
1. Load ảnh gốc
2. Click "Add Salt & Pepper Noise" để tạo nhiễu
3. Thử nghiệm với "Median Filter 3x3" hoặc "Median Filter 5x5"
4. So sánh với "Average Filter" để thấy sự khác biệt

#### Cải thiện độ tương phản:
1. Load ảnh có độ tương phản thấp
2. Click "Linear Stretching" hoặc "Standard Equalization"
3. Thử "Adaptive Equalization" cho kết quả tốt hơn với ảnh có nhiều vùng sáng tối khác nhau

#### Dò biên:
1. Load ảnh cần dò biên
2. Thử các toán tử: Sobel, Prewitt, Roberts, Kirsch
3. So sánh kết quả để chọn toán tử phù hợp

#### Làm nét ảnh:
1. Load ảnh mờ
2. Click "Sharpen (Laplacian)" hoặc "Sharpen (LoG)"
3. LoG cho kết quả mượt mà hơn nhờ làm mịn Gaussian trước

## Cấu trúc Project

```
Xu-Ly-TLU/
├── main.py                 # GUI application chính
├── image_processing.py     # Core image processing functions
├── requirements.txt        # Python dependencies
├── README.md              # Documentation (file này)
├── sample_images/         # Ảnh mẫu để test (optional)
└── .gitignore            # Git ignore rules
```

## Chi tiết kỹ thuật

### Bài 4: Contrast Stretching

**Linear Stretching:**
```python
s = (r - r_min) / (r_max - r_min) * 255
```

**Type 2 Clipping**: Chia ảnh thành 3 vùng [0-85], [86-170], [171-255] và xử lý riêng

### Bài 5: Histogram Equalization

```python
# CDF normalization
cdf_normalized = (cdf - cdf_min) * 255 / (cdf_max - cdf_min)
# Pixel mapping
output[i,j] = cdf_normalized[input[i,j]]
```

### Bài 6: CLAHE
Sử dụng OpenCV's CLAHE với clip_limit=2.0 và tile_grid_size=(8,8)

### Bài 7: Convolution

**Average Filter Kernel (3x3):**
```
1/9 * [1 1 1]
      [1 1 1]
      [1 1 1]
```

**Median Filter**: Thay thế pixel bằng giá trị trung vị trong cửa sổ

### Bài 8: Edge Detection

**Sobel Kernels:**
```
Gx = [-1  0  1]    Gy = [-1 -2 -1]
     [-2  0  2]         [ 0  0  0]
     [-1  0  1]         [ 1  2  1]
```

**Gradient Magnitude:**
```
G = sqrt(Gx^2 + Gy^2)
```

### Bài 9: Laplacian

**4-neighbor Kernel:**
```
[0  1  0]
[1 -4  1]
[0  1  0]
```

**8-neighbor Kernel:**
```
[1  1  1]
[1 -8  1]
[1  1  1]
```

**Sharpening:**
```
sharpened = original - laplacian
```

## Ví dụ kết quả

### So sánh bộ lọc khử nhiễu
- Average Filter: Làm mờ toàn bộ ảnh, kể cả biên
- Median Filter: Khử nhiễu muối tiêu hiệu quả, bảo toàn biên tốt hơn

### So sánh toán tử dò biên
- Sobel: Tốt cho biên mạnh, ít nhiễu
- Prewitt: Tương tự Sobel nhưng ít nhạy hơn
- Roberts: Phát hiện biên chéo tốt, nhạy với nhiễu
- Kirsch: Phát hiện biên theo 8 hướng, chi tiết nhất

### Histogram Equalization vs CLAHE
- Standard: Cải thiện tương phản toàn cục
- CLAHE: Cải thiện chi tiết cục bộ, tránh over-amplification

## Lỗi thường gặp

### "No module named 'cv2'"
```bash
pip install opencv-python
```

### "tkinter module not found"
- Ubuntu/Debian: `sudo apt-get install python3-tk`
- macOS: tkinter đã được cài sẵn với Python
- Windows: tkinter đã được cài sẵn với Python

### Ảnh hiển thị quá nhỏ/lớn
Ảnh tự động scale để vừa với canvas. Resize cửa sổ để điều chỉnh kích thước hiển thị.

## Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng:
1. Fork repository
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Liên hệ

Repository: [https://github.com/Minhhieu-coder/Xu-Ly-TLU](https://github.com/Minhhieu-coder/Xu-Ly-TLU)

## Tài liệu tham khảo

- Digital Image Processing - Rafael C. Gonzalez & Richard E. Woods
- OpenCV Documentation: https://docs.opencv.org/
- NumPy Documentation: https://numpy.org/doc/