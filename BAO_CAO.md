# 📄 BÁO CÁO ĐỒ ÁN XỬ LÝ ẢNH SỐ

**Trường:** Đại học Thăng Long (TLU)  
**Môn học:** Xử lý Ảnh Số  
**Link GitHub:** https://github.com/Minhhieu-coder/Xu-Ly-TLU

---

## MỤC LỤC

1. [Giới thiệu bài toán](#1-giới-thiệu-bài-toán)
2. [Mô tả dữ liệu sử dụng + Tiền xử lý dữ liệu](#2-mô-tả-dữ-liệu-sử-dụng--tiền-xử-lý-dữ-liệu)
3. [Phương pháp/Mô hình Học máy áp dụng](#3-phương-phápmô-hình-học-máy-áp-dụng)
4. [Kết quả bước đầu và nhận xét](#4-kết-quả-bước-đầu-và-nhận-xét)
5. [Định hướng phát triển cho lần báo cáo cuối cùng](#5-định-hướng-phát-triển-cho-lần-báo-cáo-cuối-cùng)

---

## 1. GIỚI THIỆU BÀI TOÁN

### 1.1. Mục tiêu

Xây dựng ứng dụng **Xử lý Ảnh Số** với giao diện đồ họa (GUI), tích hợp các kỹ thuật Machine Learning:

- Chuyển đổi ảnh cơ bản (xám, nhị phân, tách kênh màu)
- Kéo dãn tương phản và xử lý Histogram
- Lọc nhiễu và dò biên
- Biến đổi Fourier và lọc tần số
- **Machine Learning**: Phân đoạn ảnh, trích xuất đặc trưng, phát hiện đối tượng

### 1.2. Phạm vi

| Nội dung | Mô tả |
|----------|-------|
| Bài 1-3 | Chuyển đổi ảnh cơ bản |
| Bài 4-6 | Kéo dãn tương phản và Histogram |
| Bài 7-9 | Lọc nhiễu và dò biên |
| Bài 10-12 | Biến đổi Fourier và lọc tần số |
| ML | Các mô hình Machine Learning |

### 1.3. Công nghệ sử dụng

| Thư viện | Mục đích |
|----------|----------|
| Python 3.8+ | Ngôn ngữ lập trình |
| NumPy | Tính toán ma trận |
| OpenCV | Xử lý ảnh |
| scikit-learn | Machine Learning |
| Tkinter | Giao diện đồ họa |

---

## 2. MÔ TẢ DỮ LIỆU SỬ DỤNG + TIỀN XỬ LÝ DỮ LIỆU

### 2.1. Dữ liệu sử dụng

**Định dạng hỗ trợ:** PNG, JPG, JPEG, BMP, GIF, TIFF

**Ảnh mẫu:**

| Tên file | Mục đích |
|----------|----------|
| gradient.png | Test kéo dãn tương phản |
| rgb_colors.png | Test tách kênh màu |
| dark_image.png | Test cân bằng histogram |
| shapes.png | Test phân đoạn ảnh |
| checkerboard.png | Test dò biên |

### 2.2. Tiền xử lý dữ liệu

```python
# Đọc ảnh
image = cv2.imread('image.png')

# Chuyển sang grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Chuẩn hóa về [0, 255]
normalized = np.clip(gray, 0, 255).astype(np.uint8)

# Tách kênh RGB
b, g, r = cv2.split(image)
```

---

## 3. PHƯƠNG PHÁP/MÔ HÌNH HỌC MÁY ÁP DỤNG

> **Lưu ý:** Mỗi thành viên áp dụng ít nhất 1 mô hình Machine Learning.

### 3.1. MÔ HÌNH 1: K-Means Clustering *(Thành viên 1)*

**Mục đích:** Phân đoạn ảnh thành K vùng

**Công thức:**
```
J = Σᵢ₌₁ᵏ Σₓ∈Cᵢ ||x - μᵢ||²
```

**Code:**
```python
def kmeans_segmentation(image, k=3, max_iterations=100):
    pixels = image.flatten().astype(np.float32)
    centroids = np.random.choice(np.unique(pixels), k, replace=False)
    
    for _ in range(max_iterations):
        distances = np.abs(pixels[:, np.newaxis] - centroids)
        labels = np.argmin(distances, axis=1)
        new_centroids = np.array([pixels[labels == i].mean() for i in range(k)])
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    
    return centroids[labels].reshape(image.shape).astype(np.uint8)
```

### 3.2. MÔ HÌNH 2: Otsu's Thresholding *(Thành viên 2)*

**Mục đích:** Tự động tìm ngưỡng tối ưu

**Công thức:**
```
σ²_B(t) = ω₀(t) · ω₁(t) · [μ₀(t) - μ₁(t)]²
t* = arg max σ²_B(t)
```

**Code:**
```python
def otsu_threshold(image):
    hist, _ = np.histogram(image.flatten(), bins=256, range=[0, 256])
    prob = hist / hist.sum()
    
    best_threshold = 0
    max_variance = 0
    
    for t in range(256):
        w0, w1 = np.sum(prob[:t+1]), np.sum(prob[t+1:])
        if w0 == 0 or w1 == 0:
            continue
        mu0 = np.sum(np.arange(t+1) * prob[:t+1]) / w0
        mu1 = np.sum(np.arange(t+1, 256) * prob[t+1:]) / w1
        variance = w0 * w1 * (mu0 - mu1) ** 2
        if variance > max_variance:
            max_variance = variance
            best_threshold = t
    
    return (image > best_threshold).astype(np.uint8) * 255, best_threshold
```

### 3.3. MÔ HÌNH 3: Feature Extraction *(Thành viên 3)*

**Mục đích:** Trích xuất vector đặc trưng từ ảnh (29 chiều)

**Các đặc trưng:**
- Histogram Features (16 dims)
- Texture Features (5 dims)  
- Statistical Features (8 dims)

**Code:**
```python
def extract_features(image):
    features = []
    
    # Histogram features
    hist, _ = np.histogram(image.flatten(), bins=16, range=[0, 256])
    features.extend(hist / hist.sum())
    
    # Texture features
    Gx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    Gy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = np.sqrt(Gx**2 + Gy**2)
    features.extend([np.mean(magnitude), np.std(magnitude)])
    
    return np.array(features)
```

### 3.4. MÔ HÌNH 4: Object Detection *(Thành viên 4)*

**Mục đích:** Phát hiện và đếm đối tượng

**Code:**
```python
def detect_objects(binary_image, min_area=100):
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
        binary_image, connectivity=8
    )
    
    objects = []
    for i in range(1, num_labels):
        if stats[i, cv2.CC_STAT_AREA] >= min_area:
            objects.append({
                'label': i,
                'area': stats[i, cv2.CC_STAT_AREA],
                'centroid': centroids[i]
            })
    return labels, objects
```

---

## 4. KẾT QUẢ BƯỚC ĐẦU VÀ NHẬN XÉT

### 4.1. Kết quả Test

```
✅ test_ml.py: All 9 tests passed
✅ test_processing.py: All tests passed
```

**Chi tiết:**
- K-Means Segmentation: ✅ Passed
- Otsu Thresholding: ✅ Passed (threshold = 128)
- Feature Extraction: ✅ Passed (29 dimensions)
- Object Detection: ✅ Passed (detected 2 objects)

### 4.2. Hiệu năng

| Thuật toán | Thời gian |
|------------|-----------|
| K-Means (k=3) | ~0.05s |
| Otsu | ~0.01s |
| Feature Extract | ~0.02s |
| Object Detection | ~0.01s |

### 4.3. Nhận xét

**Ưu điểm:**
- K-Means phân đoạn tốt với ảnh có các vùng rõ ràng
- Otsu tự động tìm ngưỡng, không cần điều chỉnh thủ công
- Feature Extraction cung cấp 29 đặc trưng đa dạng

**Hạn chế:**
- K-Means phụ thuộc vào việc chọn K
- Otsu hiệu quả nhất với ảnh bimodal

---

## 5. ĐỊNH HƯỚNG PHÁT TRIỂN CHO LẦN BÁO CÁO CUỐI CÙNG

### 5.1. Cải tiến thuật toán

- **K-Means++**: Cải tiến khởi tạo centroid
- **Adaptive K**: Tự động chọn số cụm K tối ưu
- **Multi-level Otsu**: Ngưỡng nhiều mức

### 5.2. Thêm mô hình mới

- **Deep Learning**: CNN cho phân loại ảnh
- **SVM**: Support Vector Machine
- **Random Forest**: Ensemble learning

### 5.3. Cải tiến ứng dụng

- **Real-time Processing**: Xử lý video
- **Batch Processing**: Xử lý nhiều ảnh
- **GPU Acceleration**: Tăng tốc với CUDA

### 5.4. Tính năng bổ sung

- So sánh before/after
- Lưu và load cài đặt
- Xuất báo cáo PDF

---

## PHỤ LỤC

### Cấu trúc Source Code

```
Xu-Ly-TLU/
├── comprehensive_app.py      # Ứng dụng GUI chính
├── image_processing.py       # Thuật toán xử lý ảnh
├── ml_processing.py          # Thuật toán ML
├── requirements.txt          # Dependencies
├── test_ml.py               # Test ML
├── sample_images/           # Ảnh mẫu
├── BAO_CAO.md              # Báo cáo
└── PHAN_CONG_NHIEM_VU.md   # Phân công
```

### Hướng dẫn chạy

```bash
# Clone và cài đặt
git clone https://github.com/Minhhieu-coder/Xu-Ly-TLU.git
cd Xu-Ly-TLU
pip install -r requirements.txt

# Chạy ứng dụng
python comprehensive_app.py
```

---

**Ngày:** December 25, 2024  
**Repository:** https://github.com/Minhhieu-coder/Xu-Ly-TLU
