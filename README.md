# Ứng dụng Xử lý Ảnh Toàn diện - Comprehensive Image Processing Application

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](PROJECT_COMPLETION_SUMMARY.md)

## 📝 Tổng quan / Overview

Ứng dụng xử lý ảnh với giao diện đồ họa (GUI), tích hợp **đầy đủ** tất cả chức năng từ **Bài tập 1-12**:
- Chuyển đổi ảnh cơ bản (xám, nhị phân, tách kênh)
- Kéo dãn tương phản và xử lý histogram
- Lọc nhiễu và dò biên
- Biến đổi Fourier và lọc tần số (thông thấp & thông cao)

A comprehensive image processing application with GUI, integrating **all features** from **Exercises 1-12**:
- Basic image conversions (grayscale, binary, channel splitting)
- Contrast stretching and histogram processing
- Noise filtering and edge detection
- Fourier transform and frequency domain filtering (low-pass & high-pass)

## 🚀 Quick Start

### Cài đặt / Installation

```bash
# Clone repository
git clone https://github.com/Minhhieu-coder/Xu-Ly-TLU.git
cd Xu-Ly-TLU

# Install dependencies
pip install numpy opencv-python pillow matplotlib scipy

# (Optional) Download Bean Leaf dataset for practice
pip install kaggle
python download_dataset.py

# Run comprehensive app (RECOMMENDED)
python comprehensive_app.py
```

### Hoặc sử dụng Menu / Or use Menu Launcher

```bash
python start.py
```

## 📊 Dataset / Bộ dữ liệu

### Bean Leaf Lesions Classification Dataset ⭐ NEW

This repository now includes support for the **Bean Leaf Lesions Classification** dataset from Kaggle!

- **Source**: [Kaggle - Bean Leaf Lesions Classification](https://www.kaggle.com/datasets/marquis03/bean-leaf-lesions-classification)
- **Categories**: Angular leaf spot, Bean rust, Healthy leaves
- **Purpose**: Practice image processing techniques on real agricultural data

#### Quick Download:
```bash
# Install Kaggle API
pip install kaggle

# Configure credentials (see data/README.md)
# Then download:
python download_dataset.py

# Try example processing:
python example_bean_leaf_processing.py
```

See **[data/README.md](data/README.md)** for detailed instructions (English).  
See **[DATASET_GUIDE_VI.md](DATASET_GUIDE_VI.md)** for Vietnamese guide (Hướng dẫn tiếng Việt).


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

### ✅ Bài 10-11: Fourier Transform & Low-Pass
- FFT & IFFT
- Magnitude Spectrum
- Ideal Low-pass Filter
- Gaussian Low-pass Filter

### ✅ Bài 12: High-Pass Filters ⭐ NEW
- Ideal High-pass Filter (D0: 10-100)
- Butterworth High-pass Filter (D0: 10-100, n: 1-10)
- Edge enhancement
- Detail preservation

## 📚 Documentation

### Hướng dẫn Chính / Main Guides
- **[COMPREHENSIVE_GUIDE.md](COMPREHENSIVE_GUIDE.md)** 📘 - Hướng dẫn chi tiết
- **[QUICK_REFERENCE_COMPREHENSIVE.md](QUICK_REFERENCE_COMPREHENSIVE.md)** 🔖 - Quick reference
- **[PROJECT_COMPLETION_SUMMARY.md](PROJECT_COMPLETION_SUMMARY.md)** ✅ - Tổng kết

### Hướng dẫn Riêng / Individual Guides
- **[HUONG_DAN.md](HUONG_DAN.md)** - Hướng dẫn Bài 1-3
- **[USAGE_GUIDE.md](USAGE_GUIDE.md)** - Hướng dẫn Bài 4-9
- **[BAI12_HUONG_DAN.md](BAI12_HUONG_DAN.md)** ⭐ - Hướng dẫn Bài 12 (High-Pass Filters)
- **[data/README.md](data/README.md)** 📊 - Dataset guide (Bean Leaf Lesions)

## 🗂️ Cấu trúc / Structure

```
comprehensive_app.py              ⭐ Main app (Bài 1-12)
image_processing.py               Core algorithms
start.py                          Quick start menu
test_highpass.py                  Test Bài 12
demo_highpass.py                  Demo Bài 12
download_dataset.py               ⭐ Dataset downloader
example_bean_leaf_processing.py   ⭐ Dataset example
data/                             📊 Datasets directory
  └── README.md                   Dataset documentation
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

### 4. Làm nổi cạnh (High-pass) ⭐ NEW
```
Tải ảnh → Butterworth High-pass (D0=30, n=2) → Lưu
```

## 🧪 Testing

```bash
python test_highpass.py       # Test High-Pass (Bài 12) ⭐ NEW
python test_fourier.py        # Test Fourier (Bài 10-11)
python test_processing.py     # Test Bài 4-9
python create_test_images.py  # Generate samples

# Demo
python demo_highpass.py       # Visual demo Bài 12 ⭐ NEW
python example_bai12.py       # Simple example Bài 12 ⭐ NEW
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
