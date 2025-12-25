# PHÂN CÔNG NHIỆM VỤ - ĐỒ ÁN XỬ LÝ ẢNH SỐ

## Trường: Đại học Thăng Long (TLU)
## Môn: Xử lý Ảnh Số
## Link GitHub: https://github.com/Minhhieu-coder/Xu-Ly-TLU

---

## 1. DANH SÁCH THÀNH VIÊN NHÓM

| STT | Họ và Tên | MSSV | Email | Vai trò |
|-----|-----------|------|-------|---------|
| 1 | [Tên thành viên 1] | [MSSV] | [Email] | Nhóm trưởng |
| 2 | [Tên thành viên 2] | [MSSV] | [Email] | Thành viên |
| 3 | [Tên thành viên 3] | [MSSV] | [Email] | Thành viên |
| 4 | [Tên thành viên 4] | [MSSV] | [Email] | Thành viên |

> **Lưu ý:** Vui lòng điền thông tin thành viên nhóm vào bảng trên.

---

## 2. PHÂN CÔNG NHIỆM VỤ CỤ THỂ

### 2.1. THÀNH VIÊN 1: [Tên]

#### Nhiệm vụ được giao:
- **Bài 1-3**: Xử lý ảnh cơ bản
  - Chuyển đổi ảnh xám (grayscale)
  - Chuyển đổi ảnh nhị phân (binary)
  - Tách kênh màu RGB
  - Hiển thị kênh Alpha

- **Machine Learning - Mô hình K-Means Segmentation**
  - Nghiên cứu lý thuyết K-Means clustering
  - Triển khai thuật toán phân đoạn ảnh
  - Viết code test và tài liệu

#### Kết quả đạt được:
| Nội dung | Trạng thái | Ghi chú |
|----------|------------|---------|
| Chuyển đổi ảnh xám | ✅ Hoàn thành | Hoạt động tốt |
| Chuyển đổi nhị phân | ✅ Hoàn thành | Có slider điều chỉnh ngưỡng |
| Tách kênh RGB | ✅ Hoàn thành | Hiển thị 3 kênh riêng biệt |
| K-Means Segmentation | ✅ Hoàn thành | K=2-10 clusters |

#### Mức độ tham gia: **[...]%**

---

### 2.2. THÀNH VIÊN 2: [Tên]

#### Nhiệm vụ được giao:
- **Bài 4-6**: Kéo dãn tương phản và Histogram
  - Linear contrast stretching
  - Type 1 & Type 2 clipping
  - Cân bằng Histogram
  - Histogram matching (CLAHE)

- **Machine Learning - Mô hình Otsu Thresholding**
  - Nghiên cứu phương pháp Otsu
  - Triển khai thuật toán tìm ngưỡng tự động
  - Viết code test và tài liệu

#### Kết quả đạt được:
| Nội dung | Trạng thái | Ghi chú |
|----------|------------|---------|
| Linear stretching | ✅ Hoàn thành | Tự động detect min/max |
| Type 1 Clipping | ✅ Hoàn thành | Ngưỡng 50-200 |
| Type 2 Clipping | ✅ Hoàn thành | Xử lý 3 vùng |
| Histogram equalization | ✅ Hoàn thành | Sử dụng CDF |
| CLAHE | ✅ Hoàn thành | Adaptive equalization |
| Otsu Thresholding | ✅ Hoàn thành | Tự động tìm ngưỡng tối ưu |

#### Mức độ tham gia: **[...]%**

---

### 2.3. THÀNH VIÊN 3: [Tên]

#### Nhiệm vụ được giao:
- **Bài 7-9**: Lọc nhiễu và Dò biên
  - Average Filter (3x3, 5x5)
  - Median Filter (3x3, 5x5)
  - Sobel, Prewitt, Roberts, Kirsch
  - Laplacian (4-neighbor, 8-neighbor)
  - LoG và Sharpening

- **Machine Learning - Mô hình Feature Extraction**
  - Trích xuất đặc trưng Histogram
  - Trích xuất đặc trưng Texture
  - Trích xuất đặc trưng Statistical
  - Viết code test và tài liệu

#### Kết quả đạt được:
| Nội dung | Trạng thái | Ghi chú |
|----------|------------|---------|
| Average Filter | ✅ Hoàn thành | 3x3 và 5x5 |
| Median Filter | ✅ Hoàn thành | 3x3 và 5x5 |
| Sobel | ✅ Hoàn thành | Dò biên phổ biến |
| Prewitt, Roberts | ✅ Hoàn thành | Các operators khác |
| Kirsch | ✅ Hoàn thành | 8 hướng |
| Laplacian | ✅ Hoàn thành | 4 và 8 neighbor |
| Feature Extraction | ✅ Hoàn thành | 29 dimensions |

#### Mức độ tham gia: **[...]%**

---

### 2.4. THÀNH VIÊN 4: [Tên]

#### Nhiệm vụ được giao:
- **Bài 10-12**: Biến đổi Fourier và Lọc tần số
  - FFT và IFFT
  - Magnitude Spectrum
  - Ideal Low-pass Filter
  - Gaussian Low-pass Filter
  - Ideal High-pass Filter
  - Butterworth High-pass Filter

- **Machine Learning - Mô hình Object Detection**
  - Phát hiện đối tượng bằng Connected Components
  - Morphological Operations (Erosion, Dilation, Opening, Closing)
  - Viết code test và tài liệu

#### Kết quả đạt được:
| Nội dung | Trạng thái | Ghi chú |
|----------|------------|---------|
| FFT | ✅ Hoàn thành | Biến đổi Fourier thuận |
| IFFT | ✅ Hoàn thành | Biến đổi Fourier ngược |
| Ideal Low-pass | ✅ Hoàn thành | Cutoff 5-100 |
| Gaussian Low-pass | ✅ Hoàn thành | Sigma 5-100 |
| Ideal High-pass | ✅ Hoàn thành | D0 10-100 |
| Butterworth High-pass | ✅ Hoàn thành | D0 10-100, n 1-10 |
| Object Detection | ✅ Hoàn thành | Bounding box + centroid |
| Morphological Ops | ✅ Hoàn thành | 4 operations |

#### Mức độ tham gia: **[...]%**

---

## 3. TỔNG HỢP TIẾN ĐỘ THỰC HIỆN

### 3.1. Timeline

| Giai đoạn | Thời gian | Nội dung | Trạng thái |
|-----------|-----------|----------|------------|
| 1 | Tuần 1-2 | Nghiên cứu lý thuyết | ✅ Hoàn thành |
| 2 | Tuần 3-4 | Triển khai Bài 1-6 | ✅ Hoàn thành |
| 3 | Tuần 5-6 | Triển khai Bài 7-9 | ✅ Hoàn thành |
| 4 | Tuần 7-8 | Triển khai Bài 10-12 | ✅ Hoàn thành |
| 5 | Tuần 9-10 | Triển khai ML | ✅ Hoàn thành |
| 6 | Tuần 11-12 | Testing & Documentation | ✅ Hoàn thành |

### 3.2. Thống kê Code

| Thành phần | Số dòng code | Ghi chú |
|------------|--------------|---------|
| comprehensive_app.py | ~1,500 lines | Ứng dụng GUI chính |
| image_processing.py | ~700 lines | Thuật toán core |
| ml_processing.py | ~600 lines | Machine Learning |
| Tests | ~400 lines | Unit tests |
| Documentation | ~1,000 lines | Tài liệu |
| **Tổng** | **~4,200 lines** | |

### 3.3. Kết quả Testing

```
✅ test_ml.py: All 9 tests passed
✅ test_processing.py: All tests passed
✅ test_fourier.py: All tests passed
✅ test_highpass.py: All tests passed
```

---

## 4. ĐÁNH GIÁ MỨC ĐỘ ĐÓNG GÓP

| Thành viên | Công việc chính | Đánh giá |
|------------|-----------------|----------|
| Thành viên 1 | Bài 1-3, K-Means | [...]% |
| Thành viên 2 | Bài 4-6, Otsu | [...]% |
| Thành viên 3 | Bài 7-9, Features | [...]% |
| Thành viên 4 | Bài 10-12, Detection | [...]% |

> **Lưu ý:** Vui lòng điền % đóng góp của mỗi thành viên (tổng = 100%).

---

## 5. GHI CHÚ THÊM

### 5.1. Các buổi họp nhóm

| # | Ngày | Nội dung | Kết quả |
|---|------|----------|---------|
| 1 | [Ngày] | Phân công công việc | Đã thống nhất phân công |
| 2 | [Ngày] | Review code Bài 1-6 | Đã hoàn thành |
| 3 | [Ngày] | Review code Bài 7-12 | Đã hoàn thành |
| 4 | [Ngày] | Tích hợp ML | Đã hoàn thành |
| 5 | [Ngày] | Testing & Docs | Đã hoàn thành |

### 5.2. Khó khăn gặp phải và cách giải quyết

| Khó khăn | Giải pháp |
|----------|-----------|
| Hiểu thuật toán K-Means | Nghiên cứu tài liệu, tham khảo code mẫu |
| Triển khai FFT | Sử dụng NumPy FFT |
| GUI layout | Sử dụng Tkinter notebook tabs |
| Testing | Tạo ảnh mẫu, viết unit tests |

### 5.3. Kinh nghiệm rút ra

1. Tầm quan trọng của việc phân công rõ ràng
2. Code review giúp phát hiện lỗi sớm
3. Documentation quan trọng cho bảo trì
4. Testing đảm bảo chất lượng code

---

## 6. XÁC NHẬN

| Thành viên | Chữ ký | Ngày |
|------------|--------|------|
| [Tên 1] | __________ | [Ngày] |
| [Tên 2] | __________ | [Ngày] |
| [Tên 3] | __________ | [Ngày] |
| [Tên 4] | __________ | [Ngày] |

---

**Ngày lập:** December 25, 2024  
**Repository:** https://github.com/Minhhieu-coder/Xu-Ly-TLU
