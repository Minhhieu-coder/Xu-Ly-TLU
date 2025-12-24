# Ứng dụng Xử lý Ảnh - Image Processing Application

## Tổng quan / Overview

Dự án này cung cấp một ứng dụng xử lý ảnh toàn diện với giao diện đồ họa (GUI), tích hợp đầy đủ các kỹ thuật xử lý ảnh từ Bài tập 1 đến Bài tập 11.

This project provides a comprehensive image processing application with a graphical user interface (GUI), integrating all image processing techniques from Exercise 1 to Exercise 11.

## Tính năng / Features

### Bài 1-3: Chuyển đổi Cơ bản / Basic Conversions
- ✅ Tải và hiển thị ảnh / Load and display images
- ✅ Chuyển đổi sang ảnh xám / Convert to grayscale
- ✅ Chuyển đổi sang ảnh nhị phân / Convert to binary (with adjustable threshold)
- ✅ Tách kênh màu RGB / Split RGB channels
- ✅ Hiển thị kênh Alpha / Display Alpha channel (PNG)
- ✅ Hiển thị ma trận ảnh / Display image matrix

### Bài 4-6: Tương phản và Histogram / Contrast and Histogram
- ✅ Kéo dãn tương phản tuyến tính / Linear contrast stretching
- ✅ Type 1 Clipping (ngưỡng tùy chỉnh) / Type 1 Clipping (custom thresholds)
- ✅ Type 2 Clipping (theo vùng) / Type 2 Region-based clipping
- ✅ Cân bằng Histogram / Histogram equalization
- ✅ Hiển thị Histogram / Histogram visualization
- ✅ Histogram Matching / Histogram specification
- ✅ Adaptive Histogram Equalization (CLAHE)

### Bài 7-9: Lọc và Dò biên / Filtering and Edge Detection
- ✅ Thêm nhiễu Salt & Pepper / Add salt & pepper noise
- ✅ Average Filter (3×3, 5×5) / Mean filter
- ✅ Median Filter (3×3, 5×5) / Median filter
- ✅ Sobel Edge Detection
- ✅ Prewitt Edge Detection
- ✅ Roberts Edge Detection
- ✅ Kirsch Edge Detection
- ✅ Laplacian 4-neighbor
- ✅ Laplacian 8-neighbor
- ✅ Laplacian of Gaussian (LoG)
- ✅ Image Sharpening (Laplacian & LoG)

### Bài 10-11: Biến đổi Fourier / Fourier Transform
- ✅ Forward Fourier Transform (FFT) / Biến đổi Fourier thuận
- ✅ Inverse Fourier Transform (IFFT) / Biến đổi Fourier ngược
- ✅ Magnitude Spectrum Display / Hiển thị phổ biên độ
- ✅ Ideal Low-pass Filter / Bộ lọc Thông thấp lý tưởng
- ✅ Gaussian Low-pass Filter / Bộ lọc Thông thấp Gaussian

## Cài đặt / Installation

### Yêu cầu / Requirements
- Python 3.8+
- NumPy
- OpenCV (cv2)
- Pillow (PIL)
- Matplotlib
- SciPy

### Cài đặt thư viện / Install dependencies

```bash
pip install numpy opencv-python pillow matplotlib scipy
```

Hoặc sử dụng file requirements.txt:

```bash
pip install -r requirements.txt
```

## Sử dụng / Usage

### Ứng dụng Toàn diện (Khuyến nghị) / Comprehensive App (Recommended)

Ứng dụng này tích hợp TẤT CẢ các chức năng từ Bài 1-11:

```bash
python comprehensive_app.py
```

**Đặc điểm:**
- Giao diện thống nhất với 4 tabs tổ chức theo bài tập
- Dễ sử dụng, tất cả chức năng trong một ứng dụng
- Hỗ trợ đầy đủ từ chuyển đổi cơ bản đến Fourier transform

### Ứng dụng Riêng lẻ / Individual Apps

#### 1. Ứng dụng Bài 1-3 (Chuyển đổi cơ bản)
```bash
python image_processing_app.py
```

#### 2. Ứng dụng Bài 4-9 (Advanced processing)
```bash
python main.py
```

## Cấu trúc Dự án / Project Structure

```
Xu-Ly-TLU/
├── comprehensive_app.py          # Ứng dụng tích hợp đầy đủ (Bài 1-11) ⭐
├── image_processing.py            # Core processing algorithms
├── image_processing_app.py        # App riêng cho Bài 1-3
├── main.py                        # App riêng cho Bài 4-9
├── test_fourier.py               # Test cho Fourier transforms
├── test_processing.py            # Test suite cho Bài 4-9
├── requirements.txt              # Python dependencies
├── COMPREHENSIVE_GUIDE.md        # Hướng dẫn chi tiết
├── HUONG_DAN.md                  # Hướng dẫn Bài 1-3
└── USAGE_GUIDE.md               # Hướng dẫn Bài 4-9
```

## Hướng dẫn Sử dụng / User Guide

### Khởi động / Starting the App

1. **Chạy comprehensive_app.py**
2. **Tải ảnh**: Click "📂 Tải Ảnh" và chọn file ảnh
3. **Chọn tab chức năng**: Chọn tab tương ứng với bài tập muốn thực hiện
4. **Áp dụng chức năng**: Click vào các nút chức năng
5. **Lưu kết quả**: Click "💾 Lưu Ảnh"

### Ví dụ Workflow

#### Workflow 1: Xử lý ảnh tối
```
1. Tải ảnh
2. Tab "Bài 4-6" → Click "Kéo dãn tuyến tính"
3. Click "Cân bằng Histogram"
4. Lưu ảnh
```

#### Workflow 2: Khử nhiễu và dò biên
```
1. Tải ảnh
2. Tab "Bài 7-9" → Click "Median Filter 3x3"
3. Click "Sobel"
4. Lưu ảnh
```

#### Workflow 3: Lọc tần số
```
1. Tải ảnh
2. Tab "Bài 10-11" → Xem "FFT (Magnitude Spectrum)"
3. Điều chỉnh sigma
4. Click "Gaussian Low-pass Filter"
5. Lưu ảnh
```

## Kiểm thử / Testing

### Test Fourier Transform (Bài 10-11)
```bash
python test_fourier.py
```

### Test các chức năng Bài 4-9
```bash
python test_processing.py
```

## Tài liệu / Documentation

- **COMPREHENSIVE_GUIDE.md**: Hướng dẫn chi tiết cho comprehensive_app.py
- **HUONG_DAN.md**: Hướng dẫn cho Bài 1-3
- **USAGE_GUIDE.md**: Hướng dẫn cho Bài 4-9

## Các Công thức Toán học / Mathematical Formulas

### Bài 4: Contrast Stretching
```
s = (r - r_min) / (r_max - r_min) × 255
```

### Bài 5: Histogram Equalization
```
CDF: cdf[i] = Σ(hist[0...i])
s = (cdf[r] - cdf_min) / (cdf_max - cdf_min) × 255
```

### Bài 8: Edge Detection
```
Gradient Magnitude: G = √(Gx² + Gy²)
```

### Bài 9: Sharpening
```
sharpened = original - laplacian
```

### Bài 10: Fourier Transform
```
FFT: F(u,v) = Σ Σ f(x,y) × e^(-j2π(ux/M + vy/N))
IFFT: f(x,y) = Σ Σ F(u,v) × e^(j2π(ux/M + vy/N))
```

### Bài 11: Frequency Filters
```
Ideal LPF: H(u,v) = 1 if D(u,v) ≤ D₀, else 0
Gaussian LPF: H(u,v) = e^(-D²(u,v)/(2σ²))
```

## Tính năng Kỹ thuật / Technical Features

- **Modular Design**: Core algorithms tách biệt khỏi GUI
- **Type Hints**: Hỗ trợ type checking
- **Error Handling**: Xử lý lỗi toàn diện
- **Performance**: Tối ưu với NumPy operations
- **Cross-platform**: Chạy trên Windows, macOS, Linux

## Hiệu năng / Performance

| Image Size | Processing Speed |
|-----------|-----------------|
| 256×256 | Real-time (< 0.1s) |
| 512×512 | Fast (< 0.5s) |
| 1024×1024 | Moderate (< 2s) |
| 2048×2048 | Slower (2-5s) |

*Note: Kirsch và FFT có thể chậm hơn với ảnh lớn*

## Khắc phục Sự cố / Troubleshooting

### Lỗi ModuleNotFoundError
```bash
pip install numpy opencv-python pillow matplotlib scipy
```

### Lỗi hiển thị ảnh
- Kiểm tra định dạng file (PNG, JPG, BMP supported)
- Thử với ảnh test khác

### FFT chậm
- Giảm kích thước ảnh
- Sử dụng ảnh < 1024×1024 để có kết quả nhanh

## Đóng góp / Contributing

Mọi đóng góp đều được hoan nghênh! Vui lòng:
1. Fork repository
2. Tạo feature branch
3. Commit changes
4. Push và tạo Pull Request

## License

MIT License - Xem file LICENSE để biết chi tiết

## Tác giả / Author

- **Minhhieu-coder**
- GitHub: [@Minhhieu-coder](https://github.com/Minhhieu-coder)

## Acknowledgments

Cảm ơn các thư viện mã nguồn mở:
- NumPy - Numerical computing
- OpenCV - Computer vision
- Pillow - Image processing
- Matplotlib - Visualization
- SciPy - Scientific computing

---

**Chúc bạn sử dụng ứng dụng hiệu quả!** 🎨📸

**Happy Image Processing!** 🚀✨
