# ĐỒ ÁN XỬ LÝ ẢNH SỐ - Đại học Thăng Long (TLU)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)

## 📋 Tài liệu Nộp bài

| Tài liệu | Mô tả |
|----------|-------|
| **[BAO_CAO.md](BAO_CAO.md)** 📄 | Báo cáo đồ án đầy đủ |
| **[PHAN_CONG_NHIEM_VU.md](PHAN_CONG_NHIEM_VU.md)** 👥 | Phân công nhiệm vụ thành viên |
| **Source Code** 💻 | Mã nguồn trong repository |

---

## 📝 Tổng quan Dự án

Ứng dụng xử lý ảnh với giao diện đồ họa (GUI), tích hợp **đầy đủ** các chức năng từ **Bài tập 1-12** và **Machine Learning**:

- **Bài 1-3**: Chuyển đổi ảnh cơ bản (xám, nhị phân, tách kênh)
- **Bài 4-6**: Kéo dãn tương phản và xử lý histogram
- **Bài 7-9**: Lọc nhiễu và dò biên
- **Bài 10-11**: Biến đổi Fourier và lọc tần số thông thấp
- **Bài 12**: Lọc tần số thông cao
- **Machine Learning**: Phân đoạn K-Means, Otsu, trích xuất đặc trưng, phát hiện đối tượng

## 🚀 Cài đặt và Chạy

```bash
# 1. Clone repository
git clone https://github.com/Minhhieu-coder/Xu-Ly-TLU.git
cd Xu-Ly-TLU

# 2. Cài đặt dependencies
pip install -r requirements.txt

# 3. Chạy ứng dụng
python comprehensive_app.py

# 4. Chạy tests
python test_ml.py
python test_processing.py
```

## 🗂️ Cấu trúc Source Code

```
Xu-Ly-TLU/
├── comprehensive_app.py      # ⭐ Ứng dụng GUI chính (Bài 1-12 + ML)
├── image_processing.py       # Thuật toán xử lý ảnh core
├── ml_processing.py          # Thuật toán Machine Learning
├── requirements.txt          # Dependencies
├── test_ml.py               # Test Machine Learning
├── test_processing.py       # Test Image Processing
├── sample_images/           # Ảnh mẫu
├── BAO_CAO.md              # 📄 Báo cáo đồ án
└── PHAN_CONG_NHIEM_VU.md   # 👥 Phân công nhiệm vụ
```

## ✨ Tính năng Machine Learning

| Mô hình | Mô tả |
|---------|-------|
| **K-Means Segmentation** | Phân đoạn ảnh thành K vùng |
| **Otsu Thresholding** | Tự động tìm ngưỡng tối ưu |
| **Feature Extraction** | Trích xuất đặc trưng 29 chiều |
| **Object Detection** | Phát hiện và đếm đối tượng |
| **Morphological Ops** | Erosion, Dilation, Opening, Closing |

## 🧪 Kết quả Test

```
✅ test_ml.py: All 9 tests passed
✅ test_processing.py: All tests passed
✅ test_fourier.py: All tests passed
✅ test_highpass.py: All tests passed
```

## 📊 Hiệu năng

| Kích thước ảnh | Thời gian xử lý |
|----------------|-----------------|
| 256×256 | < 0.1s |
| 512×512 | < 0.5s |
| 1024×1024 | < 2s |

## 📝 License

MIT License

## 👥 Repository

**GitHub:** https://github.com/Minhhieu-coder/Xu-Ly-TLU

---

**Xem chi tiết tại:** [BAO_CAO.md](BAO_CAO.md) | [PHAN_CONG_NHIEM_VU.md](PHAN_CONG_NHIEM_VU.md)
