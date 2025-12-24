# Hướng Dẫn Sử Dụng Dataset Bean Leaf Lesions

## Tổng Quan

Repository này hiện hỗ trợ dataset **Bean Leaf Lesions Classification** từ Kaggle để thực hành xử lý ảnh.

## Tải Dataset

### Bước 1: Cài Đặt Kaggle API

```bash
pip install kaggle
```

### Bước 2: Lấy API Token

1. Truy cập [https://www.kaggle.com/account](https://www.kaggle.com/account)
2. Cuộn xuống phần "API"
3. Click "Create New API Token"
4. File `kaggle.json` sẽ được tải về

### Bước 3: Cấu Hình Credentials

**Linux/Mac:**
```bash
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

**Windows:**
```cmd
mkdir %USERPROFILE%\.kaggle
move Downloads\kaggle.json %USERPROFILE%\.kaggle\
```

### Bước 4: Tải Dataset

```bash
python download_dataset.py
```

Script sẽ:
- ✓ Kiểm tra Kaggle đã cài đặt
- ✓ Kiểm tra credentials
- ✓ Tải dataset (~500MB)
- ✓ Giải nén vào thư mục `data/bean-leaf-lesions/`
- ✓ Hiển thị cấu trúc dataset

## Sử Dụng Dataset

### Thử Nghiệm Cơ Bản

```bash
python example_bean_leaf_processing.py
```

Script này sẽ:
1. Tải mẫu ảnh từ 3 categories (angular leaf spot, bean rust, healthy)
2. Áp dụng các kỹ thuật xử lý ảnh:
   - Chuyển đổi grayscale
   - Histogram equalization
   - Dò biên (edge detection)
   - Lọc nhiễu (median filter)
3. Lưu kết quả vào `bean_leaf_processed/`
4. Tạo visualization so sánh

### Sử Dụng Với Ứng Dụng Chính

```python
# Mở comprehensive_app.py
python comprehensive_app.py

# Trong ứng dụng:
# 1. Click "Load Image"
# 2. Chọn ảnh từ data/bean-leaf-lesions/train/angular_leaf_spot/
# 3. Thử nghiệm các chức năng xử lý ảnh
```

## Cấu Trúc Dataset

```
data/bean-leaf-lesions/
├── train/                    # Dữ liệu huấn luyện
│   ├── angular_leaf_spot/   # Bệnh đốm lá góc
│   ├── bean_rust/           # Bệnh rỉ sắt đậu
│   └── healthy/             # Lá khỏe mạnh
├── test/                     # Dữ liệu kiểm tra
│   ├── angular_leaf_spot/
│   ├── bean_rust/
│   └── healthy/
└── validation/               # Dữ liệu xác thực
    ├── angular_leaf_spot/
    ├── bean_rust/
    └── healthy/
```

## Ví Dụ Xử Lý

### 1. Phân Tích Histogram

```python
import cv2
import matplotlib.pyplot as plt

# Tải ảnh lá bệnh
img = cv2.imread('data/bean-leaf-lesions/train/angular_leaf_spot/image_001.jpg', 0)

# Tính histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Hiển thị
plt.plot(hist)
plt.title('Histogram - Angular Leaf Spot')
plt.show()
```

### 2. Dò Biên (Edge Detection)

```python
import cv2
import numpy as np

# Tải ảnh
img = cv2.imread('data/bean-leaf-lesions/train/bean_rust/image_001.jpg', 0)

# Áp dụng Sobel
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Kết hợp
edges = np.sqrt(sobelx**2 + sobely**2)
edges = np.uint8(edges / edges.max() * 255) if edges.max() > 0 else edges.astype(np.uint8)

# Lưu kết quả
cv2.imwrite('edges.jpg', edges)
```

### 3. Cải Thiện Độ Tương Phản

```python
import cv2

# Tải ảnh
img = cv2.imread('data/bean-leaf-lesions/train/healthy/image_001.jpg', 0)

# Cân bằng histogram
enhanced = cv2.equalizeHist(img)

# So sánh
cv2.imshow('Original', img)
cv2.imshow('Enhanced', enhanced)
cv2.waitKey(0)
```

## Troubleshooting

### Lỗi: "Could not find kaggle.json"

**Giải pháp:**
```bash
# Kiểm tra vị trí file
ls ~/.kaggle/kaggle.json

# Nếu không có, lấy lại từ Kaggle
# Xem Bước 2 và 3 ở trên
```

### Lỗi: "Dataset appears to be empty"

**Giải pháp:**
```bash
# Tải lại dataset
python download_dataset.py

# Hoặc tải thủ công từ Kaggle
# Rồi giải nén vào data/bean-leaf-lesions/
```

### Lỗi: Permission denied

**Giải pháp:**
```bash
# Cấp quyền cho file credentials
chmod 600 ~/.kaggle/kaggle.json
```

## Thông Tin Thêm

- **Kích thước**: ~500MB (sau giải nén ~1GB)
- **Số lượng ảnh**: ~1000+ ảnh
- **Định dạng**: JPG
- **Độ phân giải**: Đa dạng (thường 500x500 đến 1000x1000)

## Tài Liệu Tham Khảo

- [Kaggle Dataset](https://www.kaggle.com/datasets/marquis03/bean-leaf-lesions-classification)
- [Kaggle API Documentation](https://github.com/Kaggle/kaggle-api)
- [data/README.md](README.md) - English version

## Lưu Ý

- Dataset không được commit vào Git (quá lớn)
- Chỉ có cấu trúc thư mục và documentation được track
- Mỗi người cần tải dataset riêng
- Dữ liệu chỉ dùng cho mục đích học tập và nghiên cứu

---

**Chúc bạn thực hành vui vẻ! 🌱📸**
