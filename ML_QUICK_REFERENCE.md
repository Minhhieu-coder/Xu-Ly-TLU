# MACHINE LEARNING - TÓM TẮT NHANH
# Quick Reference cho Bài tập Machine Learning

## 📚 Các thuật toán chính

### 1. K-Means Clustering
**Mục đích:** Phân đoạn ảnh thành K vùng

```python
from ml_processing import MLImageProcessor

segmented, centers = MLImageProcessor.kmeans_segmentation(image, k=4)
```

**Công thức:**
- Distance: `d(x, μ) = |x - μ|`
- Update: `μᵢ = mean(pixels in cluster i)`

---

### 2. Otsu Thresholding
**Mục đích:** Tự động tìm ngưỡng tối ưu

```python
binary, threshold = MLImageProcessor.otsu_threshold(image)
print(f"Ngưỡng tối ưu: {threshold}")
```

**Công thức:**
```
σ²_B(t) = ω₀·ω₁·(μ₀ - μ₁)²
t* = argmax σ²_B(t)
```

---

### 3. Feature Extraction
**Mục đích:** Trích xuất vector đặc trưng 29 chiều

```python
features = MLImageProcessor.extract_combined_features(image)
# Shape: (29,) = 16 histogram + 5 texture + 8 statistical
```

**Các đặc trưng:**
| Loại | Số chiều | Mô tả |
|------|----------|-------|
| Histogram | 16 | Phân bố cường độ |
| Texture | 5 | Gradient stats |
| Statistical | 8 | Mean, std, entropy... |

---

### 4. Object Detection
**Mục đích:** Phát hiện và đếm đối tượng

```python
labels, objects = MLImageProcessor.simple_object_detection(binary, min_area=50)

for obj in objects:
    print(f"Object: area={obj['area']}, center=({obj['centroid_x']:.1f}, {obj['centroid_y']:.1f})")
```

---

### 5. Morphological Operations
**Mục đích:** Xử lý hình thái học

```python
# Các phép toán có sẵn: 'erosion', 'dilation', 'opening', 'closing'
result = MLImageProcessor.morphological_operations(binary, 'erosion', kernel_size=3)
```

| Phép toán | Công thức | Ứng dụng |
|-----------|-----------|----------|
| Erosion | A ⊖ B | Loại nhiễu nhỏ |
| Dilation | A ⊕ B | Lấp lỗ trống |
| Opening | (A ⊖ B) ⊕ B | Loại nhiễu |
| Closing | (A ⊕ B) ⊖ B | Lấp lỗ |

---

## 🖥️ Sử dụng GUI

1. **Khởi động:** `python comprehensive_app.py`
2. **Tải ảnh:** Click "📂 Tải Ảnh"
3. **Chuyển tab:** Click "🤖 ML"
4. **Chọn chức năng:** Điều chỉnh tham số và click nút

---

## 📊 Workflow phổ biến

### Phân đoạn ảnh
```
Tải ảnh → K-Means (K=4) → Lưu kết quả
```

### Phát hiện đối tượng
```
Tải ảnh → Otsu → Object Detection → Xem thông tin
```

### Trích xuất đặc trưng
```
Tải ảnh → Extract Features → Xem trong tab Info
```

---

## 🧪 Test

```bash
# Chạy tất cả ML tests
python test_ml.py

# Expected output: All 9 tests passed
```

---

## 📁 Files quan trọng

| File | Mô tả |
|------|-------|
| `ml_processing.py` | Module ML chính |
| `comprehensive_app.py` | GUI tích hợp |
| `test_ml.py` | Unit tests |
| `BAO_CAO_MACHINE_LEARNING.md` | Báo cáo đầy đủ |

---

## 🔧 Dependencies

```
pip install numpy opencv-python scipy scikit-learn pillow matplotlib
```

---

**Xem báo cáo đầy đủ:** `BAO_CAO_MACHINE_LEARNING.md`
