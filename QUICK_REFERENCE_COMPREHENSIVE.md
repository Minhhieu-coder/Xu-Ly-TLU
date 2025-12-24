# Quick Reference - Ứng dụng Xử lý Ảnh

## Khởi động / Start

```bash
python comprehensive_app.py
```

## Các Tab Chức năng

### 📁 Bài 1-3: Cơ bản
| Chức năng | Mô tả | Khi nào dùng |
|-----------|-------|--------------|
| **Ảnh Xám** | Chuyển RGB → Grayscale | Bước đầu cho hầu hết xử lý |
| **Ảnh Nhị phân** | Grayscale → Black/White | Segmentation, OCR |
| **Kênh RGB** | Tách Red/Green/Blue | Phân tích màu sắc |
| **Ma trận** | Xem pixel values | Debug, học tập |

### 📊 Bài 4-6: Contrast
| Chức năng | Công thức | Khi nào dùng |
|-----------|-----------|--------------|
| **Kéo dãn tuyến tính** | `s = (r-min)/(max-min)×255` | Ảnh tối hoặc quá sáng |
| **Type 1 Clipping** | Cắt [low,high] + stretch | Tùy chỉnh range cụ thể |
| **Type 2 Clipping** | 3 vùng riêng biệt | Chi tiết trong tất cả vùng |
| **Cân bằng Histogram** | CDF mapping | Ảnh low contrast |
| **Histogram Matching** | Match reference | Chuẩn hóa nhiều ảnh |
| **CLAHE** | Local equalization | Chi tiết cục bộ |

### 🔧 Bài 7-9: Filters
| Chức năng | Kernel | Khi nào dùng |
|-----------|--------|--------------|
| **Average 3×3** | 1/9 × ones(3,3) | Khử nhiễu nhẹ, blur |
| **Average 5×5** | 1/25 × ones(5,5) | Khử nhiễu mạnh |
| **Median 3×3** | Sort & pick middle | Salt & pepper noise |
| **Median 5×5** | Sort & pick middle | Nhiễu mạnh |
| **Sobel** | Gx, Gy kernels | Dò biên cân bằng |
| **Prewitt** | Simpler than Sobel | Dò biên đơn giản |
| **Roberts** | 2×2 kernels | Dò biên nhanh |
| **Kirsch** | 8 directions | Dò biên chi tiết nhất |
| **Laplacian 4** | [[0,1,0],[1,-4,1],[0,1,0]] | Dò biên đơn giản |
| **Laplacian 8** | [[1,1,1],[1,-8,1],[1,1,1]] | Dò biên nhạy |
| **LoG** | Gaussian + Laplacian | Dò biên ít nhiễu |
| **Sharpen** | Original - Laplacian | Làm nét ảnh |

### 🌊 Bài 10-11: Fourier
| Chức năng | Mô tả | Khi nào dùng |
|-----------|-------|--------------|
| **FFT** | Time → Frequency domain | Phân tích tần số |
| **IFFT** | Frequency → Time domain | Khôi phục ảnh |
| **Ideal LPF** | Hard cutoff | Làm mờ, anti-aliasing |
| **Gaussian LPF** | Smooth cutoff | Làm mờ tự nhiên |

## Workflows Phổ biến

### 🎯 Workflow 1: Cải thiện ảnh tối
```
Tải ảnh → Kéo dãn tuyến tính → Cân bằng Histogram → Lưu
```
**Kết quả**: Tăng sáng và tương phản

### 🎯 Workflow 2: Khử nhiễu
```
Tải ảnh → Median Filter 3×3 → Lưu
```
**Kết quả**: Loại bỏ salt & pepper noise

### 🎯 Workflow 3: Dò biên
```
Tải ảnh → Ảnh Xám → Sobel → Lưu
```
**Kết quả**: Edge map

### 🎯 Workflow 4: Làm nét
```
Tải ảnh → Sharpen (Laplacian) → Lưu
```
**Kết quả**: Ảnh sắc nét hơn

### 🎯 Workflow 5: Làm mờ tự nhiên
```
Tải ảnh → Gaussian LPF (sigma=30) → Lưu
```
**Kết quả**: Blur mượt mà

## Tham số Đề nghị

### Ngưỡng Nhị phân
- **Text/OCR**: 127
- **Dark images**: 80-100
- **Bright images**: 150-180

### Average/Median Filter
- **Nhiễu nhẹ**: 3×3
- **Nhiễu vừa**: 5×5
- **Nhiễu mạnh**: 7×7 (tự implement)

### CLAHE
- **Clip limit**: 2.0 (default, good)
- **Tile grid**: 8×8 (default)

### Ideal LPF Cutoff
- **Blur mạnh**: 10-20
- **Blur vừa**: 30-50
- **Blur nhẹ**: 60-100

### Gaussian LPF Sigma
- **Blur nhẹ**: 10-20
- **Blur vừa**: 30-50
- **Blur mạnh**: 60-100

## Chọn Filter/Detector

### Khử nhiễu
| Loại nhiễu | Filter đề nghị |
|-----------|---------------|
| Salt & Pepper | **Median 3×3** |
| Gaussian | Average 5×5 hoặc Gaussian LPF |
| Speckle | Median 5×5 |

### Dò biên
| Yêu cầu | Detector đề nghị |
|---------|------------------|
| Nhanh | **Roberts** |
| Cân bằng | **Sobel** ⭐ |
| Chi tiết | Kirsch |
| Ít nhiễu | **LoG** |

### Làm mờ
| Yêu cầu | Method đề nghị |
|---------|---------------|
| Nhanh | Average Filter |
| Tự nhiên | **Gaussian LPF** ⭐ |
| Preserve edges | Bilateral (cần add) |

## Phím tắt & Tips

### Shortcuts
- Không có phím tắt, dùng chuột click
- Reset: Click "🔄 Hiển thị Ảnh Gốc"

### Tips
1. **Luôn bắt đầu với ảnh gốc** trước khi thử chức năng mới
2. **Lưu kết quả trung gian** nếu muốn so sánh
3. **Thử nhiều giá trị** tham số để tìm kết quả tốt nhất
4. **Xử lý tuần tự**: Khử nhiễu → Dò biên/Làm nét
5. **Ảnh lớn có thể chậm**: Reduce size trước khi test

### Common Issues
| Vấn đề | Giải pháp |
|--------|-----------|
| Kênh Alpha không có | Chỉ PNG có transparency |
| FFT chậm | Giảm kích thước ảnh |
| Ảnh quá mờ sau filter | Giảm kernel size hoặc sigma |
| Edge map quá nhiễu | Khử nhiễu trước khi dò biên |

## Keyboard Bindings (Không có)
- Ứng dụng chỉ hỗ trợ chuột click
- Không có phím tắt

## File Formats Supported
| Format | Read | Write | Notes |
|--------|------|-------|-------|
| PNG | ✅ | ✅ | Recommended |
| JPG | ✅ | ✅ | Lossy |
| BMP | ✅ | ✅ | Large files |
| GIF | ✅ | ❌ | Read only |
| TIFF | ✅ | ❌ | Read only |

## Performance Guide

### Image Size Recommendations
| Size | Speed | Use for |
|------|-------|---------|
| 256×256 | ⚡ Real-time | Testing, learning |
| 512×512 | 🏃 Fast | Daily use |
| 1024×1024 | 🚶 OK | Production |
| 2048×2048+ | 🐌 Slow | Be patient |

### Slow Operations
1. **Kirsch** (8 kernels)
2. **FFT** (large images)
3. **Median 5×5** (large images)

## Công thức Nhanh

```python
# Bài 4
s = (r - r_min) / (r_max - r_min) * 255

# Bài 5
s = (cdf[r] - cdf_min) / (cdf_max - cdf_min) * 255

# Bài 8
G = sqrt(Gx² + Gy²)

# Bài 9
sharpened = original - laplacian

# Bài 11
H_ideal(u,v) = 1 if D ≤ D₀ else 0
H_gaussian(u,v) = exp(-D²/(2σ²))
```

---

**🚀 Happy Processing!**

Xem thêm: `COMPREHENSIVE_GUIDE.md` để biết chi tiết
