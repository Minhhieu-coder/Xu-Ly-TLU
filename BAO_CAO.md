# BÁO CÁO ĐỒ ÁN XỬ LÝ ẢNH SỐ

## Trường: Đại học Thăng Long (TLU)
## Môn: Xử lý Ảnh Số
## Link GitHub: https://github.com/Minhhieu-coder/Xu-Ly-TLU

---

## MỤC LỤC

1. [Giới thiệu Bài toán](#1-giới-thiệu-bài-toán)
2. [Mô tả Dữ liệu và Tiền xử lý](#2-mô-tả-dữ-liệu-và-tiền-xử-lý)
3. [Phương pháp/Mô hình Học máy Áp dụng](#3-phương-phápmô-hình-học-máy-áp-dụng)
4. [Kết quả Bước đầu và Nhận xét](#4-kết-quả-bước-đầu-và-nhận-xét)
5. [Định hướng Phát triển](#5-định-hướng-phát-triển)

---

## 1. GIỚI THIỆU BÀI TOÁN

### 1.1. Mục tiêu Đồ án

Xây dựng ứng dụng xử lý ảnh toàn diện với giao diện đồ họa (GUI), tích hợp các kỹ thuật xử lý ảnh cơ bản đến nâng cao và Machine Learning, bao gồm:

- **Xử lý ảnh cơ bản**: Chuyển đổi ảnh xám, nhị phân, tách kênh màu
- **Kéo dãn tương phản và Histogram**: Cải thiện chất lượng ảnh
- **Lọc nhiễu và Dò biên**: Khử nhiễu, phát hiện cạnh
- **Biến đổi Fourier**: Lọc tần số (thông thấp, thông cao)
- **Machine Learning**: Phân đoạn ảnh, trích xuất đặc trưng, phát hiện đối tượng

### 1.2. Phạm vi Bài toán

| STT | Nội dung | Mô tả |
|-----|----------|-------|
| 1 | Bài 1-3 | Chuyển đổi ảnh cơ bản |
| 2 | Bài 4-6 | Kéo dãn tương phản và Histogram |
| 3 | Bài 7-9 | Lọc nhiễu và Dò biên |
| 4 | Bài 10-11 | Biến đổi Fourier và Lọc tần số thông thấp |
| 5 | Bài 12 | Lọc tần số thông cao |
| 6 | ML | Machine Learning cho xử lý ảnh |

### 1.3. Công nghệ Sử dụng

| Thư viện | Phiên bản | Mục đích |
|----------|-----------|----------|
| Python | ≥3.8 | Ngôn ngữ lập trình |
| NumPy | ≥1.21.0 | Tính toán ma trận |
| OpenCV | ≥4.5.0 | Xử lý ảnh |
| SciPy | ≥1.7.0 | Phép tích chập |
| scikit-learn | ≥1.0.1 | Machine Learning utilities |
| Pillow | ≥8.0.0 | Hiển thị GUI |
| Matplotlib | ≥3.3.0 | Biểu đồ |
| Tkinter | Built-in | Giao diện đồ họa |

---

## 2. MÔ TẢ DỮ LIỆU VÀ TIỀN XỬ LÝ

### 2.1. Dữ liệu Đầu vào

#### 2.1.1. Định dạng Ảnh hỗ trợ
- PNG, JPG, JPEG, BMP, GIF, TIFF

#### 2.1.2. Ảnh Mẫu (Sample Images)

| # | Tên file | Mục đích |
|---|----------|----------|
| 1 | 01_gradient.png | Test kéo dãn tương phản |
| 2 | 02_rgb_colors.png | Test tách kênh màu |
| 3 | 03_dark_image.png | Test cân bằng histogram |
| 4 | 04_bright_image.png | Test xử lý ảnh quá sáng |
| 5 | 05_checkerboard.png | Test dò biên |
| 6 | 06_shapes.png | Test phân đoạn ảnh |
| 7 | 07_alpha_transparency.png | Test kênh Alpha |
| 8 | 08_high_contrast.png | Test ảnh tương phản cao |
| 9 | 09_low_contrast.png | Test ảnh tương phản thấp |
| 10 | 10_complex_detailed.png | Test tổng hợp |

### 2.2. Tiền xử lý Dữ liệu

#### 2.2.1. Đọc và Chuẩn hóa Ảnh

```python
# Đọc ảnh
image = cv2.imread('image.png')

# Chuyển sang grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Chuẩn hóa về [0, 255]
normalized = np.clip(image, 0, 255).astype(np.uint8)
```

#### 2.2.2. Xử lý Kênh Màu

```python
# Tách kênh RGB
b, g, r = cv2.split(image)

# Kiểm tra kênh Alpha (PNG)
if image.shape[2] == 4:
    alpha = image[:, :, 3]
```

#### 2.2.3. Resize và Padding

- Tự động resize ảnh lớn để hiển thị phù hợp
- Zero-padding cho các phép lọc tích chập

---

## 3. PHƯƠNG PHÁP/MÔ HÌNH HỌC MÁY ÁP DỤNG

### 3.1. MÔ HÌNH 1: K-Means Clustering (Phân đoạn ảnh)

#### 3.1.1. Lý thuyết

K-Means là thuật toán phân cụm không giám sát (unsupervised learning), chia dữ liệu thành K cụm dựa trên khoảng cách Euclidean đến các tâm cụm.

**Hàm mục tiêu:**
```
J = Σᵢ₌₁ᵏ Σₓ∈Cᵢ ||x - μᵢ||²
```

**Thuật toán:**
1. Khởi tạo K tâm cụm ngẫu nhiên
2. Gán mỗi pixel vào cụm có tâm gần nhất
3. Cập nhật tâm cụm = trung bình các pixel trong cụm
4. Lặp lại bước 2-3 cho đến khi hội tụ

#### 3.1.2. Code Triển khai

```python
def kmeans_segmentation(image, k=3, max_iterations=100):
    pixels = image.flatten().astype(np.float32)
    
    # Khởi tạo centroids
    unique_vals = np.unique(pixels)
    idx = np.random.choice(len(unique_vals), k, replace=False)
    centroids = unique_vals[idx].astype(np.float32)
    
    for _ in range(max_iterations):
        # Gán labels
        distances = np.abs(pixels[:, np.newaxis] - centroids)
        labels = np.argmin(distances, axis=1)
        
        # Cập nhật centroids
        new_centroids = np.array([
            pixels[labels == i].mean() if np.any(labels == i) else centroids[i]
            for i in range(k)
        ])
        
        if np.allclose(centroids, new_centroids, atol=1.0):
            break
        centroids = new_centroids
    
    segmented = centroids[labels].reshape(image.shape).astype(np.uint8)
    return segmented, centroids
```

### 3.2. MÔ HÌNH 2: Otsu's Thresholding (Ngưỡng tự động)

#### 3.2.1. Lý thuyết

Phương pháp Otsu tìm ngưỡng tối ưu bằng cách tối đa hóa phương sai giữa các lớp (between-class variance).

**Công thức:**
```
σ²_B(t) = ω₀(t) · ω₁(t) · [μ₀(t) - μ₁(t)]²
t* = arg max σ²_B(t)
```

#### 3.2.2. Code Triển khai

```python
def otsu_threshold(image):
    hist, _ = np.histogram(image.flatten(), bins=256, range=[0, 256])
    prob = hist / hist.sum()
    
    best_threshold = 0
    max_variance = 0
    
    for t in range(256):
        w0 = np.sum(prob[:t+1])
        w1 = np.sum(prob[t+1:])
        
        if w0 == 0 or w1 == 0:
            continue
        
        mu0 = np.sum(np.arange(t+1) * prob[:t+1]) / w0
        mu1 = np.sum(np.arange(t+1, 256) * prob[t+1:]) / w1
        
        variance = w0 * w1 * (mu0 - mu1) ** 2
        
        if variance > max_variance:
            max_variance = variance
            best_threshold = t
    
    binary = (image > best_threshold).astype(np.uint8) * 255
    return binary, best_threshold
```

### 3.3. MÔ HÌNH 3: KNN Classifier (Phân loại)

#### 3.3.1. Lý thuyết

K-Nearest Neighbors phân loại dựa trên K láng giềng gần nhất.

**Công thức khoảng cách Euclidean:**
```
d(x, y) = √[Σᵢ₌₁ⁿ (xᵢ - yᵢ)²]
```

#### 3.3.2. Code Triển khai

```python
def knn_classify(train_features, train_labels, test_feature, k=3):
    distances = np.sqrt(np.sum((train_features - test_feature) ** 2, axis=1))
    nearest_indices = np.argsort(distances)[:k]
    nearest_labels = train_labels[nearest_indices]
    
    # Majority voting
    unique_labels, counts = np.unique(nearest_labels, return_counts=True)
    return unique_labels[np.argmax(counts)]
```

### 3.4. MÔ HÌNH 4: Feature Extraction (Trích xuất đặc trưng)

#### 3.4.1. Lý thuyết

Trích xuất vector đặc trưng từ ảnh bao gồm:
- **Histogram Features**: Phân bố cường độ pixel (16 bins)
- **Texture Features**: Gradient magnitude và direction
- **Statistical Features**: Mean, Std, Skewness, Kurtosis, Energy, Entropy

**Công thức Entropy:**
```
H = -Σᵢ p(i) · log₂(p(i))
```

#### 3.4.2. Code Triển khai

```python
def extract_combined_features(image):
    features = []
    
    # Histogram features (16 dims)
    hist, _ = np.histogram(image.flatten(), bins=16, range=[0, 256])
    hist = hist / hist.sum()
    features.extend(hist)
    
    # Texture features (5 dims)
    Gx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    Gy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = np.sqrt(Gx**2 + Gy**2)
    features.extend([np.mean(magnitude), np.std(magnitude), np.max(magnitude)])
    
    # Statistical features (8 dims)
    features.extend([np.mean(image)/255, np.std(image)/128, ...])
    
    return np.array(features)  # 29 dimensions
```

### 3.5. MÔ HÌNH 5: Object Detection (Phát hiện đối tượng)

#### 3.5.1. Lý thuyết

Sử dụng Connected Components để phát hiện và đếm đối tượng trong ảnh nhị phân.

#### 3.5.2. Code Triển khai

```python
def simple_object_detection(binary_image, min_area=100):
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
        binary_image, connectivity=8
    )
    
    objects = []
    for i in range(1, num_labels):
        area = stats[i, cv2.CC_STAT_AREA]
        if area >= min_area:
            obj = {
                'label': i,
                'area': area,
                'centroid': centroids[i]
            }
            objects.append(obj)
    
    return labels, objects
```

### 3.6. MÔ HÌNH 6: Morphological Operations

#### 3.6.1. Lý thuyết

Các phép toán hình thái học trên ảnh nhị phân:

- **Erosion (Ăn mòn)**: A ⊖ B
- **Dilation (Giãn nở)**: A ⊕ B
- **Opening (Mở)**: (A ⊖ B) ⊕ B
- **Closing (Đóng)**: (A ⊕ B) ⊖ B

#### 3.6.2. Code Triển khai

```python
def morphological_operations(image, operation='erosion', kernel_size=3):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    
    if operation == 'erosion':
        return cv2.erode(image, kernel)
    elif operation == 'dilation':
        return cv2.dilate(image, kernel)
    elif operation == 'opening':
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    elif operation == 'closing':
        return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
```

---

## 4. KẾT QUẢ BƯỚC ĐẦU VÀ NHẬN XÉT

### 4.1. Kết quả Test

Chạy test suite: `python test_ml.py`

```
==================================================
Machine Learning Image Processing Test Suite
==================================================
Testing K-Means Segmentation...
  ✓ K-Means segmentation passed

Testing Feature Extraction...
  ✓ Feature extraction passed

Testing KNN Classifier...
  ✓ KNN classifier passed

Testing Otsu Thresholding...
  - Optimal threshold: 128
  ✓ Otsu thresholding passed

Testing Adaptive Thresholding...
  ✓ Adaptive thresholding passed

Testing ML Edge Detection...
  ✓ ML edge detection passed

Testing Morphological Operations...
  ✓ Morphological operations passed

Testing Object Detection...
  - Object 1: area=709, centroid=(30.0, 30.0)
  - Object 2: area=961, centroid=(75.0, 75.0)
  ✓ Object detection passed

Testing PCA Reduction...
  - Reduced from 1024 to 3 dimensions
  ✓ PCA reduction passed

==================================================
All ML tests passed successfully!
==================================================
```

### 4.2. Đánh giá Hiệu năng

| Thuật toán | Kích thước ảnh | Thời gian |
|------------|----------------|-----------|
| K-Means (k=3) | 256×256 | ~0.05s |
| K-Means (k=5) | 512×512 | ~0.2s |
| Otsu Threshold | 256×256 | ~0.01s |
| Feature Extract | 256×256 | ~0.02s |
| Object Detection | 256×256 | ~0.01s |
| Edge Detection | 256×256 | ~0.1s |

### 4.3. Nhận xét

#### 4.3.1. Ưu điểm

1. **K-Means Segmentation**: Phân đoạn tốt với ảnh có các vùng rõ ràng
2. **Otsu Threshold**: Tự động tìm ngưỡng tối ưu, không cần điều chỉnh thủ công
3. **Feature Extraction**: Vector 29 chiều cung cấp thông tin đa dạng về ảnh
4. **Object Detection**: Phát hiện chính xác các đối tượng riêng biệt

#### 4.3.2. Hạn chế

1. **K-Means**: Kết quả phụ thuộc vào việc chọn K
2. **Otsu**: Hiệu quả nhất với ảnh bimodal (2 đỉnh histogram)
3. **KNN**: Chậm với tập dữ liệu lớn

#### 4.3.3. So sánh các mô hình

| Mô hình | Độ chính xác | Tốc độ | Phù hợp với |
|---------|--------------|--------|-------------|
| K-Means | Cao | Trung bình | Phân đoạn vùng |
| Otsu | Cao | Nhanh | Ảnh 2 lớp |
| KNN | Trung bình | Chậm | Phân loại |
| Feature Extract | - | Nhanh | Tiền xử lý |

---

## 5. ĐỊNH HƯỚNG PHÁT TRIỂN

### 5.1. Cải tiến Thuật toán

1. **K-Means++**: Cải tiến khởi tạo centroid
2. **Adaptive K**: Tự động chọn số cụm K tối ưu
3. **Multi-level Otsu**: Ngưỡng nhiều mức

### 5.2. Thêm Mô hình Mới

1. **Deep Learning**: CNN cho phân loại ảnh
2. **SVM**: Support Vector Machine cho phân loại
3. **Random Forest**: Ensemble learning

### 5.3. Cải tiến Ứng dụng

1. **Real-time Processing**: Xử lý video
2. **Batch Processing**: Xử lý nhiều ảnh cùng lúc
3. **GPU Acceleration**: Tăng tốc với CUDA

### 5.4. Tính năng Bổ sung

1. **Image Comparison**: So sánh before/after
2. **Preset Management**: Lưu và load cài đặt
3. **Export Report**: Xuất báo cáo PDF

---

## PHỤ LỤC

### A. Cấu trúc Source Code

```
Xu-Ly-TLU/
├── comprehensive_app.py      # Ứng dụng GUI chính (Bài 1-12 + ML)
├── image_processing.py       # Thuật toán xử lý ảnh core
├── ml_processing.py          # Thuật toán Machine Learning
├── requirements.txt          # Dependencies
├── test_ml.py               # Test Machine Learning
├── test_processing.py       # Test Image Processing
├── sample_images/           # Ảnh mẫu
├── BAO_CAO.md              # Báo cáo đồ án
└── PHAN_CONG_NHIEM_VU.md   # Phân công nhiệm vụ
```

### B. Hướng dẫn Cài đặt và Chạy

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

---

**Ngày hoàn thành:** December 25, 2024  
**Tác giả:** Minhhieu-coder  
**Repository:** https://github.com/Minhhieu-coder/Xu-Ly-TLU
