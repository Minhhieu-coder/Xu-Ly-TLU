# Ứng dụng Xử lý Ảnh Toàn diện - Comprehensive Image Processing Application

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](PROJECT_COMPLETION_SUMMARY.md)

## 📝 Tổng quan / Overview

Ứng dụng xử lý ảnh với giao diện đồ họa (GUI), tích hợp **đầy đủ** tất cả chức năng từ **Bài tập 1-11**:
- Chuyển đổi ảnh cơ bản (xám, nhị phân, tách kênh)
- Kéo dãn tương phản và xử lý histogram
- Lọc nhiễu và dò biên
- Biến đổi Fourier và lọc tần số

A comprehensive image processing application with GUI, integrating **all features** from **Exercises 1-11**:
- Basic image conversions (grayscale, binary, channel splitting)
- Contrast stretching and histogram processing
- Noise filtering and edge detection
- Fourier transform and frequency domain filtering

## 🚀 Quick Start

### Cài đặt / Installation

```bash
# Clone repository
git clone https://github.com/Minhhieu-coder/Xu-Ly-TLU.git
cd Xu-Ly-TLU

# Install dependencies
pip install numpy opencv-python pillow matplotlib scipy

# Run comprehensive app (RECOMMENDED)
python comprehensive_app.py
```

### Hoặc sử dụng Menu / Or use Menu Launcher

```bash
python start.py
```

## ✨ Tính năng / Features

### ✅ Bài 1-3: Chuyển đổi Cơ bản / Basic Conversions
- Tải và hiển thị ảnh / Load and display images
- Chuyển đổi ảnh xám / Grayscale conversion
- Chuyển đổi nhị phân / Binary conversion (adjustable threshold)
- Tách kênh RGB / RGB channel splitting
- Kênh Alpha / Alpha channel (PNG)
- Ma trận ảnh / Image matrix display

### ✅ Bài 4-6: Contrast & Histogram
- Kéo dãn tuyến tính / Linear contrast stretching
- Type 1 & 2 Clipping
- Cân bằng Histogram / Histogram equalization
- Histogram Matching
- CLAHE (Adaptive)

### ✅ Bài 7-9: Filters & Edge Detection
- Average & Median Filters (3×3, 5×5)
- Sobel, Prewitt, Roberts, Kirsch
- Laplacian (4 & 8 neighbor)
- LoG (Laplacian of Gaussian)
- Image Sharpening

### ✅ Bài 10-11: Fourier Transform
- FFT & IFFT
- Magnitude Spectrum
- Ideal Low-pass Filter
- Gaussian Low-pass Filter

## 📚 Documentation

### Hướng dẫn Chính / Main Guides
- **[COMPREHENSIVE_GUIDE.md](COMPREHENSIVE_GUIDE.md)** 📘 - Hướng dẫn chi tiết
- **[QUICK_REFERENCE_COMPREHENSIVE.md](QUICK_REFERENCE_COMPREHENSIVE.md)** 🔖 - Quick reference
- **[PROJECT_COMPLETION_SUMMARY.md](PROJECT_COMPLETION_SUMMARY.md)** ✅ - Tổng kết

### Hướng dẫn Riêng / Individual Guides
- **[HUONG_DAN.md](HUONG_DAN.md)** - Hướng dẫn Bài 1-3
- **[USAGE_GUIDE.md](USAGE_GUIDE.md)** - Hướng dẫn Bài 4-9

## 🗂️ Cấu trúc / Structure

```
comprehensive_app.py     ⭐ Main app (Bài 1-11)
image_processing.py      Core algorithms
start.py                 Quick start menu
```

## 🎯 Workflows

### 1. Cải thiện ảnh tối
```
Tải ảnh → Kéo dãn tuyến tính → Cân bằng Histogram → Lưu
```

### 2. Khử nhiễu
```
Tải ảnh → Median Filter 3×3 → Lưu
```

### 3. Dò biên
```
Tải ảnh → Sobel → Lưu
```

## 🧪 Testing

```bash
python test_fourier.py        # Test Fourier (Bài 10-11)
python test_processing.py     # Test Bài 4-9
python create_test_images.py  # Generate samples
```

## 📊 Performance

| Size | Speed |
|------|-------|
| 256×256 | ⚡ < 0.1s |
| 512×512 | 🏃 < 0.5s |
| 1024×1024 | 🚶 < 2s |

## ✅ Quality

- Code Review: ✅ Passed
- Security Scan: ✅ 0 vulnerabilities
- Tests: ✅ All passed

## 📝 License

MIT License

## 👤 Author

**Minhhieu-coder**
- GitHub: [@Minhhieu-coder](https://github.com/Minhhieu-coder)

---

**🎨 Happy Image Processing! 📸**

See [COMPREHENSIVE_GUIDE.md](COMPREHENSIVE_GUIDE.md) for details
