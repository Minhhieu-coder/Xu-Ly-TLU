# Quick Reference - Tài liệu Tham khảo Nhanh

## Khởi động Ứng dụng

```bash
python image_processing_app.py
```

## Phím tắt Chức năng (Quick Actions)

### Tải và Lưu
- **Tải ảnh**: Click "📂 Tải Ảnh" → Chọn file
- **Lưu ảnh**: Click "💾 Lưu Ảnh" → Chọn vị trí và định dạng

### Chuyển đổi Cơ bản (Tab "Chuyển đổi")
- **Ảnh gốc**: "🎨 Ảnh Gốc"
- **Ảnh xám**: "⚫ Ảnh Xám"
- **Ma trận xám**: "📊 Ma trận Ảnh Xám"
- **Ảnh nhị phân**: Điều chỉnh slider → "⚪ Chuyển sang Nhị phân"
- **Kênh đỏ**: "🔴 Kênh Đỏ (Red)"
- **Kênh xanh lá**: "🟢 Kênh Xanh lá (Green)"
- **Kênh xanh dương**: "🔵 Kênh Xanh dương (Blue)"
- **Kênh Alpha**: "👁️ Kênh Alpha (PNG)"

### Chỉ số (Tab "Chỉ số")
- **Độ sáng**: "📊 Độ sáng trung bình"
- **Tương phản**: "📊 Độ tương phản"
- **Entropy**: "📊 Entropy"
- **Độ sắc nét**: "📊 Độ sắc nét"
- **Tất cả**: "📊 Tất cả các chỉ số"

### Tăng cường (Tab "Tăng cường")
- **Âm bản**: "🔄 Ảnh Âm bản (Negative)"
- **Logarit**: Điều chỉnh c → "☀️ Biến đổi Logarit"
- **Logarit ngược**: Điều chỉnh c → "🌙 Biến đổi Logarit ngược"
- **Gamma**: Điều chỉnh γ → "⚡ Biến đổi Gamma"

## Công thức Nhanh

| Chức năng | Công thức | Tham số |
|-----------|-----------|---------|
| Âm bản | s = 255 - r | - |
| Logarit | s = c · log(1 + r) | c: 0.1-3.0 |
| Logarit ngược | r = e^(s/c) - 1 | c: 0.1-3.0 |
| Gamma | s = c · r^γ | γ: 0.1-3.0 |

## Giải thích Chỉ số

| Chỉ số | Ý nghĩa | Giá trị |
|--------|---------|---------|
| Độ sáng | Mức sáng trung bình | 0-255 |
| Tương phản | Độ khác biệt sáng tối | Càng cao càng rõ |
| Entropy | Lượng thông tin | 0-8 bits |
| Độ sắc nét | Độ rõ nét | Càng cao càng sắc |

## Giá trị Gamma

| Gamma (γ) | Hiệu ứng | Ứng dụng |
|-----------|----------|----------|
| 0.1 - 0.9 | Làm sáng | Ảnh tối |
| 1.0 | Không đổi | - |
| 1.1 - 3.0 | Làm tối | Ảnh sáng |

**Giá trị khuyên dùng:**
- Ảnh tối: γ = 0.5 - 0.7
- Ảnh sáng: γ = 1.5 - 2.0

## Ngưỡng Nhị phân

| Ngưỡng | Kết quả |
|---------|---------|
| 0-85 | Nhiều trắng |
| 86-170 | Cân bằng |
| 171-255 | Nhiều đen |

**Giá trị khuyên dùng:** 127 (trung bình)

## Ảnh Mẫu để Test

| File | Mục đích |
|------|----------|
| 03_dark_image.png | Test logarit |
| 04_bright_image.png | Test logarit ngược |
| 07_alpha_transparency.png | Test kênh Alpha |
| 08_high_contrast.png | Test chỉ số |
| 10_complex_detailed.png | Test entropy |

## Use Cases Phổ biến

### 1. Tăng sáng ảnh tối
1. Tải ảnh tối
2. Tab "Tăng cường"
3. c = 1.5
4. Click "☀️ Biến đổi Logarit"

### 2. Giảm sáng ảnh quá sáng
1. Tải ảnh sáng
2. Tab "Tăng cường"
3. γ = 1.5 - 2.0
4. Click "⚡ Biến đổi Gamma"

### 3. Tạo ảnh đen trắng
1. Tải ảnh
2. Tab "Chuyển đổi"
3. Slider = 127
4. Click "⚪ Chuyển sang Nhị phân"

### 4. Phân tích chất lượng ảnh
1. Tải ảnh
2. Tab "Chỉ số"
3. Click "📊 Tất cả các chỉ số"
4. Xem tab "Ma trận / Thông tin"

## Xử lý Lỗi Thường gặp

| Lỗi | Nguyên nhân | Giải pháp |
|-----|-------------|-----------|
| "Chưa có ảnh" | Chưa tải ảnh | Click "📂 Tải Ảnh" |
| "Không có Alpha" | Ảnh không phải PNG | Dùng ảnh PNG có transparency |
| Ma trận quá lớn | Ảnh kích thước lớn | Ứng dụng tự giới hạn 50x50 |

## Tips Nâng cao

1. **So sánh trước/sau**: Dùng "🎨 Ảnh Gốc" để xem lại
2. **Thử nghiệm**: Điều chỉnh slider để xem hiệu ứng real-time
3. **Lưu nhiều phiên bản**: Lưu các kết quả khác nhau
4. **Kết hợp**: Áp dụng nhiều biến đổi tuần tự

## Hỗ trợ

- Đọc: `README.md` (tổng quan)
- Đọc: `HUONG_DAN.md` (chi tiết)
- Đọc: `UI_DESCRIPTION.md` (giao diện)
- Đọc: `PROJECT_SUMMARY.md` (tổng kết)

## Dependencies

```bash
pip install -r requirements.txt
```

Bao gồm:
- Pillow >= 10.0.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0

---

**Version:** 1.0  
**Last Updated:** December 2024
