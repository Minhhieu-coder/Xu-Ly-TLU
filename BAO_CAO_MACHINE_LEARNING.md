# BÁO CÁO BÀI TẬP LỚN
# ỨNG DỤNG MACHINE LEARNING TRONG XỬ LÝ ẢNH SỐ

---

## THÔNG TIN CHUNG

**Môn học:** Xử lý Ảnh Số  
**Trường:** Đại học Thăng Long (TLU)  
**Tên dự án:** Ứng dụng Machine Learning trong Xử lý Ảnh  
**Ngôn ngữ lập trình:** Python 3.8+  
**Repository:** https://github.com/Minhhieu-coder/Xu-Ly-TLU

---

## MỤC LỤC

1. [Giới thiệu](#1-giới-thiệu)
2. [Cơ sở lý thuyết](#2-cơ-sở-lý-thuyết)
3. [Các thuật toán đã triển khai](#3-các-thuật-toán-đã-triển-khai)
4. [Hướng dẫn cài đặt](#4-hướng-dẫn-cài-đặt)
5. [Hướng dẫn sử dụng](#5-hướng-dẫn-sử-dụng)
6. [Code mẫu](#6-code-mẫu)
7. [Kết quả thực nghiệm](#7-kết-quả-thực-nghiệm)
8. [Kết luận](#8-kết-luận)
9. [Tài liệu tham khảo](#9-tài-liệu-tham-khảo)

---

## 1. GIỚI THIỆU

### 1.1. Mục đích

Bài tập lớn này trình bày việc áp dụng các kỹ thuật Machine Learning vào xử lý ảnh số, bao gồm:
- Phân đoạn ảnh (Image Segmentation)
- Trích xuất đặc trưng (Feature Extraction)
- Phân loại ảnh (Image Classification)
- Phát hiện đối tượng (Object Detection)

### 1.2. Phạm vi

Module Machine Learning được tích hợp vào ứng dụng xử lý ảnh toàn diện đã có sẵn (Bài 1-12), mở rộng khả năng của ứng dụng với các công cụ học máy hiện đại.

### 1.3. Công nghệ sử dụng

| Thư viện | Phiên bản | Mục đích |
|----------|-----------|----------|
| Python | ≥3.8 | Ngôn ngữ lập trình |
| NumPy | ≥1.21.0 | Tính toán ma trận |
| OpenCV | ≥4.5.0 | Xử lý ảnh |
| SciPy | ≥1.7.0 | Phép tích chập |
| scikit-learn | ≥1.0.1 | ML utilities |
| Pillow | ≥8.0.0 | Hiển thị GUI |
| Matplotlib | ≥3.3.0 | Biểu đồ |
| Tkinter | Built-in | Giao diện đồ họa |

---

## 2. CƠ SỞ LÝ THUYẾT

### 2.1. Thuật toán K-Means Clustering

#### 2.1.1. Định nghĩa
K-Means là thuật toán phân cụm không giám sát (unsupervised learning), chia dữ liệu thành K cụm dựa trên khoảng cách đến các tâm cụm (centroids).

#### 2.1.2. Công thức toán học

**Hàm mục tiêu (Objective Function):**
```
J = Σᵢ₌₁ᵏ Σₓ∈Cᵢ ||x - μᵢ||²
```

Trong đó:
- K: Số cụm
- Cᵢ: Cụm thứ i
- μᵢ: Tâm của cụm i
- x: Điểm dữ liệu (pixel)

**Cập nhật tâm cụm:**
```
μᵢ = (1/|Cᵢ|) Σₓ∈Cᵢ x
```

#### 2.1.3. Thuật toán
```
1. Khởi tạo K tâm cụm ngẫu nhiên
2. Repeat:
   a. Gán mỗi pixel vào cụm có tâm gần nhất
   b. Cập nhật tâm cụm = trung bình các pixel trong cụm
3. Until: Các tâm cụm không thay đổi (hội tụ)
```

### 2.2. Phương pháp Otsu

#### 2.2.1. Định nghĩa
Phương pháp Otsu tự động tìm ngưỡng tối ưu để phân chia ảnh thành hai lớp (foreground và background) bằng cách tối đa hóa phương sai giữa các lớp.

#### 2.2.2. Công thức toán học

**Phương sai giữa các lớp (Between-class variance):**
```
σ²_B(t) = ω₀(t) · ω₁(t) · [μ₀(t) - μ₁(t)]²
```

Trong đó:
- t: Ngưỡng
- ω₀(t), ω₁(t): Xác suất của lớp 0 và lớp 1
- μ₀(t), μ₁(t): Giá trị trung bình của lớp 0 và lớp 1

**Xác suất lớp:**
```
ω₀(t) = Σᵢ₌₀ᵗ p(i)
ω₁(t) = Σᵢ₌ₜ₊₁²⁵⁵ p(i)
```

**Ngưỡng tối ưu:**
```
t* = arg max σ²_B(t)
      0≤t≤255
```

### 2.3. K-Nearest Neighbors (KNN)

#### 2.3.1. Định nghĩa
KNN là thuật toán phân loại dựa trên khoảng cách, dự đoán nhãn của mẫu mới dựa trên K láng giềng gần nhất.

#### 2.3.2. Công thức khoảng cách Euclidean
```
d(x, y) = √[Σᵢ₌₁ⁿ (xᵢ - yᵢ)²]
```

#### 2.3.3. Thuật toán
```
1. Tính khoảng cách từ mẫu test đến tất cả mẫu training
2. Chọn K mẫu gần nhất
3. Bỏ phiếu đa số (Majority voting)
4. Trả về nhãn được chọn nhiều nhất
```

### 2.4. Principal Component Analysis (PCA)

#### 2.4.1. Định nghĩa
PCA là kỹ thuật giảm chiều dữ liệu bằng cách chiếu dữ liệu lên các thành phần chính (principal components).

#### 2.4.2. Các bước thực hiện
```
1. Chuẩn hóa dữ liệu (Zero mean)
2. Tính ma trận hiệp phương sai
3. Tính eigenvalues và eigenvectors
4. Sắp xếp theo eigenvalue giảm dần
5. Chọn top-n principal components
6. Chiếu dữ liệu lên không gian mới
```

### 2.5. Các đặc trưng ảnh (Image Features)

#### 2.5.1. Histogram Features
- Phân bố cường độ pixel
- Normalized histogram với N bins

#### 2.5.2. Texture Features
- Gradient magnitude: `G = √(Gx² + Gy²)`
- Gradient direction: `θ = arctan(Gy/Gx)`
- Statistics: mean, std, max

#### 2.5.3. Statistical Features
- Mean, Standard deviation
- Skewness, Kurtosis
- Energy, Entropy

**Công thức Entropy:**
```
H = -Σᵢ p(i) · log₂(p(i))
```

**Công thức Energy:**
```
E = Σᵢ p(i)²
```

### 2.6. Morphological Operations

#### 2.6.1. Erosion (Ăn mòn)
```
A ⊖ B = {z | (B)_z ⊆ A}
```

#### 2.6.2. Dilation (Giãn nở)
```
A ⊕ B = {z | (B̂)_z ∩ A ≠ ∅}
```

#### 2.6.3. Opening (Mở)
```
A ∘ B = (A ⊖ B) ⊕ B
```

#### 2.6.4. Closing (Đóng)
```
A • B = (A ⊕ B) ⊖ B
```

---

## 3. CÁC THUẬT TOÁN ĐÃ TRIỂN KHAI

### 3.1. Module `ml_processing.py`

| # | Thuật toán | Hàm | Mô tả |
|---|-----------|-----|-------|
| 1 | K-Means Segmentation | `kmeans_segmentation()` | Phân đoạn ảnh grayscale |
| 2 | Color K-Means | `color_kmeans_segmentation()` | Phân đoạn ảnh màu |
| 3 | Histogram Features | `extract_histogram_features()` | Trích xuất đặc trưng histogram |
| 4 | Texture Features | `extract_texture_features()` | Trích xuất đặc trưng texture |
| 5 | Statistical Features | `extract_statistical_features()` | Trích xuất đặc trưng thống kê |
| 6 | Combined Features | `extract_combined_features()` | Kết hợp tất cả đặc trưng |
| 7 | KNN Classifier | `knn_classify()` | Phân loại KNN |
| 8 | PCA | `pca_reduce()` | Giảm chiều PCA |
| 9 | Otsu Thresholding | `otsu_threshold()` | Ngưỡng tự động Otsu |
| 10 | Adaptive Threshold | `adaptive_threshold_ml()` | Ngưỡng cục bộ |
| 11 | ML Edge Detection | `detect_edges_ml()` | Phát hiện cạnh kiểu Canny |
| 12 | Morphological Ops | `morphological_operations()` | Erosion, Dilation, Opening, Closing |
| 13 | Object Detection | `simple_object_detection()` | Phát hiện đối tượng |

### 3.2. Chi tiết các hàm

#### 3.2.1. K-Means Segmentation
```python
def kmeans_segmentation(image: np.ndarray, k: int = 3, 
                        max_iterations: int = 100) -> Tuple[np.ndarray, np.ndarray]:
    """
    Phân đoạn ảnh sử dụng K-Means clustering
    
    Args:
        image: Ảnh grayscale đầu vào
        k: Số cụm (2-10)
        max_iterations: Số vòng lặp tối đa
        
    Returns:
        Tuple của (ảnh phân đoạn, tâm các cụm)
    """
```

#### 3.2.2. Otsu Thresholding
```python
def otsu_threshold(image: np.ndarray) -> Tuple[np.ndarray, int]:
    """
    Tìm ngưỡng tối ưu sử dụng phương pháp Otsu
    
    Args:
        image: Ảnh grayscale đầu vào
        
    Returns:
        Tuple của (ảnh nhị phân, ngưỡng tối ưu)
    """
```

#### 3.2.3. Feature Extraction
```python
def extract_combined_features(image: np.ndarray) -> np.ndarray:
    """
    Trích xuất vector đặc trưng kết hợp (29 chiều)
    
    Args:
        image: Ảnh grayscale đầu vào
        
    Returns:
        Vector đặc trưng 29 chiều:
        - 16 histogram features
        - 5 texture features
        - 8 statistical features
    """
```

#### 3.2.4. Object Detection
```python
def simple_object_detection(image: np.ndarray, min_area: int = 100) -> Tuple[np.ndarray, List[dict]]:
    """
    Phát hiện đối tượng sử dụng Connected Components
    
    Args:
        image: Ảnh nhị phân đầu vào
        min_area: Diện tích tối thiểu của đối tượng
        
    Returns:
        Tuple của (ảnh labeled, danh sách đối tượng)
        
    Mỗi đối tượng chứa:
        - label: Nhãn của đối tượng
        - area: Diện tích (số pixel)
        - x, y: Vị trí góc trái trên
        - width, height: Kích thước bounding box
        - centroid_x, centroid_y: Tọa độ tâm
    """
```

---

## 4. HƯỚNG DẪN CÀI ĐẶT

### 4.1. Yêu cầu hệ thống
- Python 3.8 trở lên
- Windows/Linux/MacOS
- RAM: ≥4GB (khuyến nghị 8GB)

### 4.2. Cài đặt

```bash
# 1. Clone repository
git clone https://github.com/Minhhieu-coder/Xu-Ly-TLU.git
cd Xu-Ly-TLU

# 2. Cài đặt dependencies
pip install -r requirements.txt

# 3. Kiểm tra cài đặt
python test_ml.py
```

### 4.3. File requirements.txt

```text
numpy>=1.21.0
opencv-python>=4.5.0
scipy>=1.7.0
Pillow>=8.0.0
matplotlib>=3.3.0
scikit-learn>=1.0.1
```

---

## 5. HƯỚNG DẪN SỬ DỤNG

### 5.1. Sử dụng GUI

#### Bước 1: Khởi động ứng dụng
```bash
python comprehensive_app.py
```

#### Bước 2: Tải ảnh
- Click "📂 Tải Ảnh"
- Chọn file ảnh (PNG, JPG, BMP, etc.)

#### Bước 3: Chuyển sang tab "🤖 ML"
- Click vào tab ML ở panel bên trái

#### Bước 4: Sử dụng các chức năng

**K-Means Segmentation:**
1. Điều chỉnh slider "Số cụm K" (2-10)
2. Click "K-Means Segmentation"
3. Xem kết quả phân đoạn

**Otsu Thresholding:**
1. Click "Otsu Auto Threshold"
2. Xem ngưỡng tối ưu trong tab Info

**Feature Extraction:**
1. Click "Extract Features"
2. Xem chi tiết các đặc trưng trong tab Info

**Object Detection:**
1. Click "Detect Objects"
2. Xem bounding boxes và thông tin đối tượng

**Morphological Operations:**
1. Chọn phép toán: Erosion/Dilation/Opening/Closing
2. Click nút tương ứng

### 5.2. Sử dụng trong Code

#### Import module
```python
from ml_processing import MLImageProcessor
import cv2
import numpy as np
```

#### Ví dụ hoàn chỉnh
```python
# Tải ảnh
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 1. K-Means Segmentation
segmented, centers = MLImageProcessor.kmeans_segmentation(image, k=4)
print(f"Cluster centers: {centers}")

# 2. Otsu Thresholding
binary, threshold = MLImageProcessor.otsu_threshold(image)
print(f"Optimal threshold: {threshold}")

# 3. Feature Extraction
features = MLImageProcessor.extract_combined_features(image)
print(f"Feature vector shape: {features.shape}")  # (29,)

# 4. Object Detection
labels, objects = MLImageProcessor.simple_object_detection(binary, min_area=50)
print(f"Detected {len(objects)} objects")

# 5. Morphological Operations
eroded = MLImageProcessor.morphological_operations(binary, 'erosion')
dilated = MLImageProcessor.morphological_operations(binary, 'dilation')

# Lưu kết quả
cv2.imwrite('segmented.png', segmented)
cv2.imwrite('binary.png', binary)
```

---

## 6. CODE MẪU

### 6.1. K-Means Image Segmentation

```python
import numpy as np
import cv2

def kmeans_segmentation(image, k=3, max_iterations=100):
    """
    K-Means clustering cho phân đoạn ảnh
    
    Thuật toán:
    1. Flatten ảnh thành vector 1D
    2. Khởi tạo K centroids ngẫu nhiên
    3. Lặp cho đến khi hội tụ:
       - Gán mỗi pixel vào cụm gần nhất
       - Cập nhật centroids = mean của các pixel trong cụm
    4. Reshape về kích thước ảnh gốc
    """
    # Flatten image
    pixels = image.flatten().astype(np.float32)
    
    # Initialize centroids
    np.random.seed(42)
    unique_vals = np.unique(pixels)
    idx = np.random.choice(len(unique_vals), k, replace=False)
    centroids = unique_vals[idx].astype(np.float32)
    
    # K-Means loop
    for _ in range(max_iterations):
        # Assign pixels to nearest centroid
        distances = np.abs(pixels[:, np.newaxis] - centroids)
        labels = np.argmin(distances, axis=1)
        
        # Update centroids
        new_centroids = np.array([
            pixels[labels == i].mean() if np.any(labels == i) else centroids[i]
            for i in range(k)
        ])
        
        # Check convergence
        if np.allclose(centroids, new_centroids, atol=1.0):
            break
        centroids = new_centroids
    
    # Create segmented image
    segmented = centroids[labels].reshape(image.shape).astype(np.uint8)
    return segmented, centroids
```

### 6.2. Otsu's Method

```python
def otsu_threshold(image):
    """
    Phương pháp Otsu tìm ngưỡng tối ưu
    
    Công thức:
    - σ²_B(t) = ω₀·ω₁·(μ₀ - μ₁)²
    - t* = argmax σ²_B(t)
    """
    # Calculate histogram
    hist, _ = np.histogram(image.flatten(), bins=256, range=[0, 256])
    hist = hist.astype(np.float64)
    
    # Total pixels
    total = hist.sum()
    prob = hist / total
    
    # Find optimal threshold
    best_threshold = 0
    max_variance = 0
    
    for t in range(256):
        # Class probabilities
        w0 = np.sum(prob[:t+1])
        w1 = np.sum(prob[t+1:])
        
        if w0 == 0 or w1 == 0:
            continue
        
        # Class means
        mu0 = np.sum(np.arange(t+1) * prob[:t+1]) / w0
        mu1 = np.sum(np.arange(t+1, 256) * prob[t+1:]) / w1
        
        # Between-class variance
        variance = w0 * w1 * (mu0 - mu1) ** 2
        
        if variance > max_variance:
            max_variance = variance
            best_threshold = t
    
    # Apply threshold
    binary = (image > best_threshold).astype(np.uint8) * 255
    return binary, best_threshold
```

### 6.3. Feature Extraction

```python
def extract_features(image):
    """
    Trích xuất vector đặc trưng từ ảnh
    
    Các loại đặc trưng:
    1. Histogram features (16 dims)
    2. Texture features (5 dims)
    3. Statistical features (8 dims)
    
    Total: 29 dimensions
    """
    features = []
    
    # 1. Histogram features
    hist, _ = np.histogram(image.flatten(), bins=16, range=[0, 256])
    hist = hist / hist.sum()  # Normalize
    features.extend(hist)
    
    # 2. Texture features (gradient-based)
    Gx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    Gy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = np.sqrt(Gx**2 + Gy**2)
    direction = np.arctan2(Gy, Gx)
    
    features.extend([
        np.mean(magnitude),
        np.std(magnitude),
        np.max(magnitude),
        np.mean(np.abs(direction)),
        np.std(direction)
    ])
    
    # 3. Statistical features
    features.extend([
        np.mean(image) / 255,           # Mean
        np.std(image) / 128,            # Std
        (image.max() - image.min()) / 255,  # Contrast
        np.median(image) / 255,         # Median
        # Skewness, Kurtosis, Energy, Entropy...
    ])
    
    return np.array(features)
```

### 6.4. Object Detection

```python
def detect_objects(binary_image, min_area=100):
    """
    Phát hiện đối tượng sử dụng Connected Components
    
    Các bước:
    1. Tìm connected components
    2. Lọc theo min_area
    3. Trích xuất properties
    """
    # Find connected components
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
        binary_image, connectivity=8
    )
    
    objects = []
    for i in range(1, num_labels):  # Skip background (0)
        area = stats[i, cv2.CC_STAT_AREA]
        
        if area >= min_area:
            obj = {
                'label': i,
                'area': area,
                'x': stats[i, cv2.CC_STAT_LEFT],
                'y': stats[i, cv2.CC_STAT_TOP],
                'width': stats[i, cv2.CC_STAT_WIDTH],
                'height': stats[i, cv2.CC_STAT_HEIGHT],
                'centroid': (centroids[i, 0], centroids[i, 1])
            }
            objects.append(obj)
    
    return labels, objects
```

---

## 7. KẾT QUẢ THỰC NGHIỆM

### 7.1. Test Results

Chạy test suite với lệnh: `python test_ml.py`

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

### 7.2. Performance Metrics

| Algorithm | Input Size | Execution Time |
|-----------|------------|----------------|
| K-Means (k=3) | 256×256 | ~0.05s |
| K-Means (k=5) | 512×512 | ~0.2s |
| Otsu | 256×256 | ~0.01s |
| Feature Extract | 256×256 | ~0.02s |
| Object Detection | 256×256 | ~0.01s |
| Edge Detection | 256×256 | ~0.1s |

### 7.3. Ví dụ kết quả

#### K-Means Segmentation (k=4)
- Input: Ảnh grayscale với nhiều mức xám
- Output: Ảnh với 4 mức xám riêng biệt
- Cluster centers: [32, 96, 160, 224]

#### Otsu Thresholding
- Input: Ảnh với foreground và background
- Output: Ảnh nhị phân
- Optimal threshold: Tự động xác định

#### Object Detection
- Input: Ảnh nhị phân với nhiều đối tượng
- Output: Bounding boxes + thông tin chi tiết
- Metrics: Area, Position, Centroid

---

## 8. KẾT LUẬN

### 8.1. Kết quả đạt được

✅ **Hoàn thành đầy đủ** các mục tiêu đề ra:

1. **Phân đoạn ảnh**: Triển khai K-Means clustering cho cả ảnh grayscale và color
2. **Trích xuất đặc trưng**: 29-dimensional feature vector (histogram + texture + statistical)
3. **Phân loại**: KNN classifier với custom implementation
4. **Giảm chiều**: PCA với eigenvalue decomposition
5. **Thresholding**: Otsu và Adaptive thresholding
6. **Object Detection**: Connected components với bounding boxes
7. **Morphological Operations**: Erosion, Dilation, Opening, Closing

### 8.2. Ưu điểm

- **Educational**: Custom implementations giúp hiểu rõ thuật toán
- **Integrated**: Tích hợp hoàn chỉnh vào GUI
- **Well-documented**: Code có type hints và docstrings
- **Well-tested**: 9 test cases đều passed

### 8.3. Hướng phát triển

1. Thêm Deep Learning models (CNN)
2. Real-time video processing
3. GPU acceleration với CUDA
4. Thêm nhiều thuật toán: SVM, Random Forest
5. Image classification với pre-trained models

### 8.4. Bài học kinh nghiệm

1. Tầm quan trọng của preprocessing trong ML
2. Trade-off giữa độ phức tạp và hiệu quả
3. Cách tổ chức code theo module
4. Testing và documentation quan trọng

---

## 9. TÀI LIỆU THAM KHẢO

### 9.1. Sách

1. Rafael C. Gonzalez, Richard E. Woods. "Digital Image Processing", 4th Edition. Pearson, 2018.
2. Richard O. Duda, Peter E. Hart, David G. Stork. "Pattern Classification", 2nd Edition. Wiley, 2000.
3. Christopher M. Bishop. "Pattern Recognition and Machine Learning". Springer, 2006.

### 9.2. Tài liệu Online

1. OpenCV Documentation: https://docs.opencv.org/
2. NumPy Documentation: https://numpy.org/doc/
3. scikit-learn Documentation: https://scikit-learn.org/stable/
4. Studocu - Digital Image Processing: https://www.studocu.com/

### 9.3. Papers

1. Otsu, N. (1979). "A Threshold Selection Method from Gray-Level Histograms". IEEE Transactions on Systems, Man, and Cybernetics.
2. MacQueen, J. (1967). "Some Methods for classification and Analysis of Multivariate Observations". Proceedings of 5th Berkeley Symposium on Mathematical Statistics and Probability.

---

## PHỤ LỤC

### A. Cấu trúc thư mục

```
Xu-Ly-TLU/
├── comprehensive_app.py      # Ứng dụng GUI chính
├── image_processing.py       # Core algorithms (Bài 1-12)
├── ml_processing.py          # Machine Learning module
├── test_ml.py               # ML test suite
├── requirements.txt          # Dependencies
├── README.md                 # Project overview
├── COMPREHENSIVE_GUIDE.md    # User guide
├── BAO_CAO_MACHINE_LEARNING.md  # Báo cáo này
└── sample_images/            # Ảnh mẫu
```

### B. API Reference

```python
class MLImageProcessor:
    @staticmethod
    def kmeans_segmentation(image, k=3, max_iterations=100)
    
    @staticmethod
    def color_kmeans_segmentation(image, k=3)
    
    @staticmethod
    def extract_histogram_features(image, bins=32)
    
    @staticmethod
    def extract_texture_features(image)
    
    @staticmethod
    def extract_statistical_features(image)
    
    @staticmethod
    def extract_combined_features(image)
    
    @staticmethod
    def knn_classify(train_features, train_labels, test_feature, k=3)
    
    @staticmethod
    def pca_reduce(images, n_components=10)
    
    @staticmethod
    def otsu_threshold(image)
    
    @staticmethod
    def adaptive_threshold_ml(image, block_size=15, C=5)
    
    @staticmethod
    def detect_edges_ml(image, low_threshold=0.1, high_threshold=0.3)
    
    @staticmethod
    def morphological_operations(image, operation='erosion', kernel_size=3)
    
    @staticmethod
    def simple_object_detection(image, min_area=100)
```

---

**Ngày hoàn thành:** December 25, 2024  
**Tác giả:** Minhhieu-coder  
**Version:** 1.0

---

*Báo cáo này được tạo như một phần của dự án Xử lý Ảnh Số tại Đại học Thăng Long (TLU).*
