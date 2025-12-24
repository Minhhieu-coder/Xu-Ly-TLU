# Hướng dẫn Sử dụng Ứng dụng Xử lý Ảnh Toàn diện

## Giới thiệu

Ứng dụng Xử lý Ảnh Toàn diện tích hợp đầy đủ các chức năng từ Bài tập 1 đến Bài tập 11, bao gồm:
- **Bài 1-3**: Chuyển đổi ảnh cơ bản (xám, nhị phân, tách kênh màu)
- **Bài 4-6**: Kéo dãn tương phản và xử lý histogram
- **Bài 7-9**: Lọc nhiễu, dò biên và làm nét
- **Bài 10-11**: Biến đổi Fourier và lọc tần số

## Cài đặt

### Yêu cầu hệ thống
- Python 3.8 trở lên
- Các thư viện: numpy, opencv-python, pillow, matplotlib, scipy

### Cài đặt dependencies

```bash
pip install numpy opencv-python pillow matplotlib scipy
```

## Khởi động Ứng dụng

```bash
python comprehensive_app.py
```

## Cấu trúc Giao diện

Giao diện được chia thành 3 phần chính:

### 1. Panel Trái - Điều khiển
- **File Operations**: Tải ảnh, lưu ảnh, hiển thị ảnh gốc
- **Notebook với 4 tabs**:
  - **Bài 1-3: Cơ bản** - Chuyển đổi ảnh cơ bản
  - **Bài 4-6: Contrast** - Xử lý tương phản và histogram
  - **Bài 7-9: Filters** - Lọc nhiễu và dò biên
  - **Bài 10-11: Fourier** - Biến đổi Fourier và lọc tần số

### 2. Panel Phải - Hiển thị
- **Tab "Hiển thị Ảnh"**: Canvas hiển thị ảnh
- **Tab "Thông tin / Ma trận"**: Hiển thị ma trận, thông tin chi tiết

### 3. Status Bar
Hiển thị trạng thái và thông tin về thao tác đang thực hiện

## Hướng dẫn Sử dụng Chi tiết

### Bài 1-3: Chuyển đổi Cơ bản

#### 1. Tải Ảnh
1. Click "📂 Tải Ảnh"
2. Chọn file ảnh (PNG, JPG, BMP, GIF, TIFF)
3. Ảnh sẽ hiển thị ở panel bên phải

#### 2. Chuyển đổi Ảnh Xám
- Click "⚫ Ảnh Xám" để chuyển ảnh sang grayscale

#### 3. Chuyển đổi Ảnh Nhị phân
1. Điều chỉnh thanh trượt "Ngưỡng nhị phân" (0-255)
2. Click "⚪ Ảnh Nhị phân"
3. Pixels > ngưỡng → trắng (255), pixels ≤ ngưỡng → đen (0)

#### 4. Tách Kênh Màu
- **🔴 Kênh Đỏ**: Hiển thị chỉ kênh Red
- **🟢 Kênh Xanh lá**: Hiển thị chỉ kênh Green
- **🔵 Kênh Xanh dương**: Hiển thị chỉ kênh Blue
- **👁️ Kênh Alpha**: Hiển thị kênh Alpha (chỉ cho ảnh PNG có transparency)

#### 5. Xem Ma trận
- Click "📊 Ma trận Ảnh Xám" để xem ma trận pixel values

### Bài 4-6: Contrast và Histogram

#### Bài 4: Contrast Stretching

**1. Kéo dãn tuyến tính**
- Click "Kéo dãn tuyến tính"
- Công thức: `s = (r - r_min) / (r_max - r_min) × 255`
- Tự động phát hiện min/max và kéo dãn toàn bộ range

**2. Type 1 Clipping**
- Click "Type 1 Clipping"
- Cắt ảnh trong khoảng [50, 200] rồi kéo dãn

**3. Type 2 Clipping**
- Click "Type 2 Clipping"
- Xử lý riêng 3 vùng: tối [0-85], trung bình [86-170], sáng [171-255]

#### Bài 5: Histogram

**1. Cân bằng Histogram**
- Click "Cân bằng Histogram"
- Sử dụng CDF để phân phối lại intensity
- Tăng tương phản toàn cục

**2. Hiển thị Histogram**
- Click "Hiển thị Histogram"
- Mở cửa sổ mới với 2 biểu đồ: Original vs Processed

#### Bài 6: Advanced Histogram

**1. Histogram Matching**
- Click "Histogram Matching"
- Khớp histogram với phân phối Gaussian chuẩn

**2. Adaptive Equalization (CLAHE)**
- Click "Adaptive (CLAHE)"
- Cân bằng histogram cục bộ
- Tốt hơn cho chi tiết địa phương

### Bài 7-9: Filters và Edge Detection

#### Bài 7: Noise Removal

**1. Thêm Nhiễu**
- Click "➕ Thêm Nhiễu"
- Thêm salt & pepper noise để test các filter

**2. Average Filter**
- **Average Filter 3x3**: Làm mờ nhẹ, khử nhiễu nhanh
- **Average Filter 5x5**: Làm mờ mạnh hơn

**3. Median Filter**
- **Median Filter 3x3**: Tốt cho salt & pepper noise
- **Median Filter 5x5**: Khử nhiễu mạnh, giữ được cạnh

#### Bài 8: Edge Detection

**1. Sobel**
- Toán tử Sobel 3×3
- Phát hiện cạnh tốt, ít nhiễu
- Sử dụng phổ biến nhất

**2. Prewitt**
- Tương tự Sobel nhưng không có trọng số
- Đơn giản hơn

**3. Roberts**
- Toán tử 2×2 nhỏ nhất
- Nhanh nhưng nhạy nhiễu

**4. Kirsch**
- 8 toán tử theo 8 hướng
- Chi tiết nhất nhưng chậm nhất

#### Bài 9: Laplacian và Sharpening

**1. Laplacian**
- **Laplacian 4-neighbor**: Đạo hàm bậc 2, 4 hướng
- **Laplacian 8-neighbor**: Đạo hàm bậc 2, 8 hướng, nhạy hơn

**2. LoG (Laplacian of Gaussian)**
- Gaussian blur trước → Laplacian sau
- Giảm nhiễu, kết quả mượt hơn

**3. Sharpening**
- **Sharpen (Laplacian)**: `sharpened = original - laplacian`
- **Sharpen (LoG)**: Sử dụng LoG để làm nét

### Bài 10-11: Fourier Transform và Frequency Filters

#### Bài 10: Fourier Transform

**1. FFT (Magnitude Spectrum)**
- Click "🔄 FFT (Magnitude Spectrum)"
- Hiển thị magnitude spectrum trong miền tần số
- Tần số thấp ở giữa, tần số cao ở rìa
- Sử dụng log scale để dễ nhìn

**Giải thích:**
- **Tần số thấp**: Biến đổi chậm, vùng mượt
- **Tần số cao**: Biến đổi nhanh, cạnh, chi tiết

**2. Inverse FFT**
- Click "↩️ Inverse FFT"
- Khôi phục ảnh từ magnitude và phase spectrum
- Kiểm tra độ chính xác của FFT

#### Bài 11: Frequency Domain Filters

**1. Ideal Low-pass Filter**
- Điều chỉnh "Cutoff" (5-100)
- Click "Ideal Low-pass Filter"
- Chặn hoàn toàn tần số cao hơn cutoff
- Giữ lại tần số thấp

**Hiệu ứng:**
- Cutoff thấp (5-20): Rất mờ, chỉ giữ cấu trúc cơ bản
- Cutoff trung bình (20-50): Mờ vừa phải
- Cutoff cao (50-100): Giữ nhiều chi tiết

**2. Gaussian Low-pass Filter**
- Điều chỉnh "Sigma" (5.0-100.0)
- Click "Gaussian Low-pass Filter"
- Lọc mượt mà hơn Ideal filter
- Không có hiện tượng ringing

**Hiệu ứng:**
- Sigma nhỏ (5-20): Giữ nhiều chi tiết
- Sigma trung bình (20-50): Làm mờ vừa phải
- Sigma lớn (50-100): Rất mờ

**So sánh Ideal vs Gaussian:**
- **Ideal**: Cắt sắc nét, có thể gây ringing artifacts
- **Gaussian**: Mượt mà, tự nhiên hơn, ít artifacts

## Workflow Đề nghị

### 1. Xử lý Ảnh Tối
1. Tải ảnh
2. Bài 4: Kéo dãn tuyến tính
3. Bài 5: Cân bằng histogram
4. Kiểm tra kết quả

### 2. Khử Nhiễu
1. Tải ảnh nhiễu (hoặc thêm nhiễu)
2. Bài 7: Median Filter 3x3 (cho salt & pepper)
3. Hoặc Average Filter 5x5 (cho nhiễu Gaussian)

### 3. Dò Biên
1. Tải ảnh
2. Bài 8: Sobel (cân bằng tốc độ/chất lượng)
3. Hoặc Kirsch (chi tiết nhất)

### 4. Làm Nét
1. Tải ảnh hơi mờ
2. Bài 9: Sharpen (Laplacian)
3. Hoặc Sharpen (LoG) nếu có nhiễu

### 5. Lọc Tần số
1. Tải ảnh
2. Bài 10: Xem FFT để hiểu cấu trúc tần số
3. Bài 11: Áp dụng Gaussian Low-pass để làm mờ tự nhiên

## Tips & Tricks

### Tối ưu Workflow
- Luôn bắt đầu với ảnh gốc bằng "🔄 Hiển thị Ảnh Gốc"
- Lưu kết quả trung gian bằng "💾 Lưu Ảnh"
- Thử nhiều giá trị tham số để tìm kết quả tốt nhất

### Chọn Filter phù hợp
- **Salt & Pepper noise**: Median Filter
- **Gaussian noise**: Average Filter hoặc Gaussian Low-pass
- **Làm nét**: Laplacian hoặc LoG Sharpening
- **Làm mờ tự nhiên**: Gaussian Low-pass Filter

### Chọn Edge Detector
- **Nhanh, đơn giản**: Roberts
- **Cân bằng tốt**: Sobel
- **Chi tiết nhất**: Kirsch
- **Ít nhiễu**: LoG

### Xử lý ảnh có nhiễu
1. Khử nhiễu trước (Bài 7)
2. Sau đó dò biên hoặc làm nét (Bài 8-9)

## Công thức Toán học

### Bài 4
```
Linear Stretching: s = (r - r_min) / (r_max - r_min) × 255
```

### Bài 5
```
CDF: cdf[i] = Σ(hist[0...i])
Equalization: s = (cdf[r] - cdf_min) / (cdf_max - cdf_min) × 255
```

### Bài 8
```
Sobel X: [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
Sobel Y: [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
Magnitude: G = √(Gx² + Gy²)
```

### Bài 9
```
Laplacian 4: [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
Laplacian 8: [[1, 1, 1], [1, -8, 1], [1, 1, 1]]
Sharpen: sharpened = original - laplacian
```

### Bài 10
```
FFT: F(u,v) = Σ Σ f(x,y) × e^(-j2π(ux/M + vy/N))
IFFT: f(x,y) = Σ Σ F(u,v) × e^(j2π(ux/M + vy/N))
```

### Bài 11
```
Ideal LPF: H(u,v) = 1 if D(u,v) ≤ D₀, else 0
Gaussian LPF: H(u,v) = e^(-D²(u,v)/(2σ²))
D(u,v) = √((u-M/2)² + (v-N/2)²)
```

## Khắc phục Sự cố

### Không tải được ảnh
- Kiểm tra định dạng file
- Đảm bảo file không bị lỗi
- Thử ảnh khác

### Kênh Alpha không hiển thị
- Chỉ ảnh PNG với transparency mới có Alpha channel
- Thử với file PNG khác

### FFT không hoạt động
- Đảm bảo đã tải ảnh
- Chuyển sang ảnh xám trước
- Kiểm tra kích thước ảnh (nên < 2048×2048 để nhanh)

### Ảnh bị mờ sau khi xử lý
- Kiểm tra xem có áp dụng filter làm mờ không
- Thử "🔄 Hiển thị Ảnh Gốc" để reset

## Phím tắt và Thao tác nhanh

1. **Chuyển đổi nhanh**: Click trực tiếp vào các nút chức năng
2. **So sánh**: Lưu ảnh gốc → Xử lý → So sánh với file đã lưu
3. **Reset**: Click "🔄 Hiển thị Ảnh Gốc"

## Lưu ý Kỹ thuật

- Tất cả xử lý làm việc trên ảnh grayscale
- Ảnh màu tự động chuyển sang grayscale khi cần
- Kết quả luôn được chuẩn hóa về [0, 255]
- Ma trận lớn chỉ hiển thị 50×50 đầu tiên

## Hiệu năng

- Ảnh nhỏ (< 512×512): Rất nhanh, real-time
- Ảnh trung bình (512×1024): Nhanh, < 1s
- Ảnh lớn (> 1024×1024): Có thể chậm cho các toán tử phức tạp (Kirsch, FFT)

## Hỗ trợ

Nếu gặp vấn đề:
1. Kiểm tra đã cài đủ dependencies
2. Thử với ảnh test đơn giản
3. Kiểm tra log/error message

---

**Chúc bạn sử dụng ứng dụng hiệu quả!** 🎨📸
