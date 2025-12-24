"""
Ứng dụng xử lý ảnh với giao diện đồ họa
Image Processing Application with GUI

Tác giả: Minhhieu-coder
Mô tả: Ứng dụng xử lý ảnh với các chức năng: chuyển đổi ảnh xám, nhị phân,
       tách kênh màu, tính toán các chỉ số hình ảnh, và tăng cường chất lượng ảnh.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from PIL import Image, ImageTk
import numpy as np
import math
import os


class ImageProcessingApp:
    """Lớp chính cho ứng dụng xử lý ảnh"""
    
    def __init__(self, root):
        """Khởi tạo ứng dụng"""
        self.root = root
        self.root.title("Ứng dụng Xử lý Ảnh - Image Processing Application")
        self.root.geometry("1400x800")
        
        # Biến lưu trữ ảnh
        self.original_image = None
        self.processed_image = None
        self.current_image = None
        self.image_path = None
        
        # Tạo giao diện
        self.create_gui()
        
    def create_gui(self):
        """Tạo giao diện người dùng với 3 khu vực"""
        
        # Khu vực chính - chia làm 2 phần: trái và phải
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # ===== PHẦN TRÁI: Điều khiển =====
        left_frame = ttk.Frame(main_frame, width=400)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10))
        left_frame.pack_propagate(False)
        
        # Khu vực 1: Tải ảnh (Trái - Trên)
        load_frame = ttk.LabelFrame(left_frame, text="1. Tải và Lưu Ảnh", padding=10)
        load_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(load_frame, text="📂 Tải Ảnh", command=self.load_image, width=30).pack(pady=5)
        ttk.Button(load_frame, text="💾 Lưu Ảnh", command=self.save_image, width=30).pack(pady=5)
        
        self.image_info_label = ttk.Label(load_frame, text="Chưa có ảnh", font=("Arial", 9))
        self.image_info_label.pack(pady=5)
        
        # Khu vực 2: Chức năng xử lý (Trái - Dưới)
        functions_frame = ttk.LabelFrame(left_frame, text="2. Chức năng Xử lý Ảnh", padding=10)
        functions_frame.pack(fill=tk.BOTH, expand=True)
        
        # Tạo notebook (tabs) cho các nhóm chức năng
        self.notebook = ttk.Notebook(functions_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Tab 1: Chuyển đổi cơ bản
        basic_tab = ttk.Frame(self.notebook)
        self.notebook.add(basic_tab, text="Chuyển đổi")
        
        ttk.Button(basic_tab, text="🎨 Ảnh Gốc", command=self.show_original, width=28).pack(pady=5)
        ttk.Button(basic_tab, text="⚫ Ảnh Xám", command=self.convert_to_grayscale, width=28).pack(pady=5)
        ttk.Button(basic_tab, text="📊 Ma trận Ảnh Xám", command=self.show_grayscale_matrix, width=28).pack(pady=5)
        
        # Binary conversion với slider
        ttk.Label(basic_tab, text="Ảnh Nhị phân (Ngưỡng):").pack(pady=(10, 0))
        self.binary_threshold = tk.IntVar(value=127)
        threshold_slider = ttk.Scale(basic_tab, from_=0, to=255, variable=self.binary_threshold, 
                                      orient=tk.HORIZONTAL, command=self.update_binary_preview)
        threshold_slider.pack(fill=tk.X, padx=10, pady=5)
        
        self.threshold_label = ttk.Label(basic_tab, text="Ngưỡng: 127")
        self.threshold_label.pack()
        
        ttk.Button(basic_tab, text="⚪ Chuyển sang Nhị phân", 
                  command=self.convert_to_binary, width=28).pack(pady=5)
        
        # RGB channels
        ttk.Label(basic_tab, text="Tách kênh màu:").pack(pady=(10, 0))
        ttk.Button(basic_tab, text="🔴 Kênh Đỏ (Red)", command=self.show_red_channel, width=28).pack(pady=5)
        ttk.Button(basic_tab, text="🟢 Kênh Xanh lá (Green)", command=self.show_green_channel, width=28).pack(pady=5)
        ttk.Button(basic_tab, text="🔵 Kênh Xanh dương (Blue)", command=self.show_blue_channel, width=28).pack(pady=5)
        
        # Alpha channel
        ttk.Button(basic_tab, text="👁️ Kênh Alpha (PNG)", 
                  command=self.show_alpha_channel, width=28).pack(pady=5)
        
        # Tab 2: Chỉ số hình ảnh
        metrics_tab = ttk.Frame(self.notebook)
        self.notebook.add(metrics_tab, text="Chỉ số")
        
        ttk.Label(metrics_tab, text="Tính toán chỉ số hình ảnh:", font=("Arial", 10, "bold")).pack(pady=10)
        ttk.Button(metrics_tab, text="📊 Độ sáng trung bình", 
                  command=self.calculate_brightness, width=28).pack(pady=5)
        ttk.Button(metrics_tab, text="📊 Độ tương phản", 
                  command=self.calculate_contrast, width=28).pack(pady=5)
        ttk.Button(metrics_tab, text="📊 Entropy", 
                  command=self.calculate_entropy, width=28).pack(pady=5)
        ttk.Button(metrics_tab, text="📊 Độ sắc nét", 
                  command=self.calculate_sharpness, width=28).pack(pady=5)
        ttk.Button(metrics_tab, text="📊 Tất cả các chỉ số", 
                  command=self.calculate_all_metrics, width=28).pack(pady=5)
        
        # Tab 3: Tăng cường chất lượng
        enhancement_tab = ttk.Frame(self.notebook)
        self.notebook.add(enhancement_tab, text="Tăng cường")
        
        ttk.Label(enhancement_tab, text="Tăng cường chất lượng ảnh:", font=("Arial", 10, "bold")).pack(pady=10)
        
        ttk.Button(enhancement_tab, text="🔄 Ảnh Âm bản (Negative)", 
                  command=self.create_negative, width=28).pack(pady=5)
        
        ttk.Label(enhancement_tab, text="Logarit (thiếu sáng):").pack(pady=(10, 0))
        self.log_c = tk.DoubleVar(value=1.0)
        ttk.Scale(enhancement_tab, from_=0.1, to=3.0, variable=self.log_c, 
                 orient=tk.HORIZONTAL).pack(fill=tk.X, padx=10)
        self.log_c_label = ttk.Label(enhancement_tab, text="c = 1.0")
        self.log_c_label.pack()
        self.log_c.trace_add("write", self.update_log_c_label)
        
        ttk.Button(enhancement_tab, text="☀️ Biến đổi Logarit", 
                  command=self.log_transform, width=28).pack(pady=5)
        
        ttk.Label(enhancement_tab, text="Logarit ngược (dư sáng):").pack(pady=(10, 0))
        self.inv_log_c = tk.DoubleVar(value=1.0)
        ttk.Scale(enhancement_tab, from_=0.1, to=3.0, variable=self.inv_log_c, 
                 orient=tk.HORIZONTAL).pack(fill=tk.X, padx=10)
        self.inv_log_c_label = ttk.Label(enhancement_tab, text="c = 1.0")
        self.inv_log_c_label.pack()
        self.inv_log_c.trace_add("write", self.update_inv_log_c_label)
        
        ttk.Button(enhancement_tab, text="🌙 Biến đổi Logarit ngược", 
                  command=self.inverse_log_transform, width=28).pack(pady=5)
        
        ttk.Label(enhancement_tab, text="Gamma (điều chỉnh sáng):").pack(pady=(10, 0))
        self.gamma = tk.DoubleVar(value=1.0)
        ttk.Scale(enhancement_tab, from_=0.1, to=3.0, variable=self.gamma, 
                 orient=tk.HORIZONTAL).pack(fill=tk.X, padx=10)
        self.gamma_label = ttk.Label(enhancement_tab, text="γ = 1.0")
        self.gamma_label.pack()
        self.gamma.trace_add("write", self.update_gamma_label)
        
        ttk.Button(enhancement_tab, text="⚡ Biến đổi Gamma", 
                  command=self.gamma_transform, width=28).pack(pady=5)
        
        # ===== PHẦN PHẢI: Hiển thị =====
        # Khu vực 3: Hiển thị ảnh và kết quả (Bên phải)
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Tạo notebook cho hiển thị ảnh và ma trận
        self.display_notebook = ttk.Notebook(right_frame)
        self.display_notebook.pack(fill=tk.BOTH, expand=True)
        
        # Tab hiển thị ảnh
        image_tab = ttk.Frame(self.display_notebook)
        self.display_notebook.add(image_tab, text="Hiển thị Ảnh")
        
        # Canvas để hiển thị ảnh
        self.canvas_frame = ttk.Frame(image_tab)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        self.canvas = tk.Canvas(self.canvas_frame, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Tab hiển thị ma trận/thông tin
        matrix_tab = ttk.Frame(self.display_notebook)
        self.display_notebook.add(matrix_tab, text="Ma trận / Thông tin")
        
        self.matrix_text = scrolledtext.ScrolledText(matrix_tab, wrap=tk.WORD, 
                                                      font=("Courier", 9))
        self.matrix_text.pack(fill=tk.BOTH, expand=True)
        
    def load_image(self):
        """Tải ảnh từ máy tính"""
        file_path = filedialog.askopenfilename(
            title="Chọn ảnh",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif"),
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg *.jpeg"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                self.image_path = file_path
                self.original_image = Image.open(file_path)
                self.current_image = self.original_image.copy()
                
                # Hiển thị thông tin ảnh
                width, height = self.original_image.size
                mode = self.original_image.mode
                file_name = os.path.basename(file_path)
                
                info = f"Tên: {file_name}\nKích thước: {width}x{height}\nMode: {mode}"
                self.image_info_label.config(text=info)
                
                # Hiển thị ảnh
                self.display_image(self.original_image)
                
                messagebox.showinfo("Thành công", f"Đã tải ảnh: {file_name}")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể tải ảnh:\n{str(e)}")
    
    def save_image(self):
        """Lưu ảnh đã xử lý"""
        if self.current_image is None:
            messagebox.showwarning("Cảnh báo", "Không có ảnh để lưu!")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Lưu ảnh",
            defaultextension=".png",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg"),
                ("BMP files", "*.bmp"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                self.current_image.save(file_path)
                messagebox.showinfo("Thành công", f"Đã lưu ảnh: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể lưu ảnh:\n{str(e)}")
    
    def display_image(self, image):
        """Hiển thị ảnh trên canvas"""
        if image is None:
            return
        
        # Lấy kích thước canvas
        self.canvas.update()
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        # Resize ảnh để vừa với canvas nhưng giữ tỷ lệ
        img_width, img_height = image.size
        
        # Tính tỷ lệ scale
        scale = min(canvas_width / img_width, canvas_height / img_height, 1)
        new_width = int(img_width * scale * 0.9)  # 90% để có padding
        new_height = int(img_height * scale * 0.9)
        
        if new_width > 0 and new_height > 0:
            resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Chuyển sang PhotoImage và hiển thị
            self.photo = ImageTk.PhotoImage(resized_image)
            
            self.canvas.delete("all")
            self.canvas.create_image(canvas_width // 2, canvas_height // 2, 
                                    image=self.photo, anchor=tk.CENTER)
    
    def show_original(self):
        """Hiển thị ảnh gốc"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh gốc!")
            return
        
        self.current_image = self.original_image.copy()
        self.display_image(self.current_image)
        self.matrix_text.delete(1.0, tk.END)
        self.matrix_text.insert(tk.END, "Đã hiển thị ảnh gốc")
    
    def convert_to_grayscale(self):
        """Chuyển ảnh sang ảnh xám"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh để xử lý!")
            return
        
        try:
            # Chuyển sang grayscale
            gray_image = self.original_image.convert('L')
            self.current_image = gray_image
            self.display_image(gray_image)
            
            self.matrix_text.delete(1.0, tk.END)
            self.matrix_text.insert(tk.END, "Đã chuyển sang ảnh xám.\nChọn 'Ma trận Ảnh Xám' để xem ma trận.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể chuyển sang ảnh xám:\n{str(e)}")
    
    def show_grayscale_matrix(self):
        """Hiển thị ma trận ảnh xám"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh để xử lý!")
            return
        
        try:
            # Chuyển sang grayscale và lấy ma trận
            gray_image = self.original_image.convert('L')
            gray_array = np.array(gray_image)
            
            self.matrix_text.delete(1.0, tk.END)
            self.matrix_text.insert(tk.END, "=== MA TRẬN ẢNH XÁM ===\n\n")
            self.matrix_text.insert(tk.END, f"Kích thước: {gray_array.shape}\n")
            self.matrix_text.insert(tk.END, f"Kiểu dữ liệu: {gray_array.dtype}\n\n")
            
            # Hiển thị ma trận (giới hạn kích thước để tránh quá tải)
            if gray_array.shape[0] > 50 or gray_array.shape[1] > 50:
                self.matrix_text.insert(tk.END, 
                    f"Ma trận quá lớn để hiển thị đầy đủ ({gray_array.shape[0]}x{gray_array.shape[1]}).\n")
                self.matrix_text.insert(tk.END, "Hiển thị góc trên-trái (50x50):\n\n")
                display_array = gray_array[:50, :50]
            else:
                display_array = gray_array
            
            # Format ma trận
            self.matrix_text.insert(tk.END, str(display_array))
            self.matrix_text.insert(tk.END, f"\n\n--- Thống kê ---\n")
            self.matrix_text.insert(tk.END, f"Min: {np.min(gray_array)}\n")
            self.matrix_text.insert(tk.END, f"Max: {np.max(gray_array)}\n")
            self.matrix_text.insert(tk.END, f"Mean: {np.mean(gray_array):.2f}\n")
            self.matrix_text.insert(tk.END, f"Std: {np.std(gray_array):.2f}\n")
            
            # Chuyển tab sang ma trận
            self.display_notebook.select(1)
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể hiển thị ma trận:\n{str(e)}")
    
    def update_binary_preview(self, val):
        """Cập nhật label ngưỡng nhị phân"""
        threshold = int(float(val))
        self.threshold_label.config(text=f"Ngưỡng: {threshold}")
    
    def convert_to_binary(self):
        """Chuyển ảnh sang ảnh nhị phân"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh để xử lý!")
            return
        
        try:
            # Chuyển sang grayscale trước
            gray_image = self.original_image.convert('L')
            gray_array = np.array(gray_image)
            
            # Áp dụng ngưỡng
            threshold = self.binary_threshold.get()
            binary_array = (gray_array > threshold) * 255
            
            # Chuyển về ảnh
            binary_image = Image.fromarray(binary_array.astype(np.uint8))
            self.current_image = binary_image
            self.display_image(binary_image)
            
            self.matrix_text.delete(1.0, tk.END)
            self.matrix_text.insert(tk.END, f"Đã chuyển sang ảnh nhị phân với ngưỡng = {threshold}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể chuyển sang ảnh nhị phân:\n{str(e)}")
    
    def show_red_channel(self):
        """Hiển thị kênh màu đỏ"""
        self.show_color_channel('R', 'Đỏ (Red)')
    
    def show_green_channel(self):
        """Hiển thị kênh màu xanh lá"""
        self.show_color_channel('G', 'Xanh lá (Green)')
    
    def show_blue_channel(self):
        """Hiển thị kênh màu xanh dương"""
        self.show_color_channel('B', 'Xanh dương (Blue)')
    
    def show_color_channel(self, channel, name):
        """Hiển thị một kênh màu cụ thể"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh để xử lý!")
            return
        
        try:
            # Chuyển sang RGB nếu cần
            if self.original_image.mode != 'RGB':
                rgb_image = self.original_image.convert('RGB')
            else:
                rgb_image = self.original_image
            
            # Tách kênh
            r, g, b = rgb_image.split()
            
            # Chọn kênh tương ứng
            if channel == 'R':
                channel_image = r
            elif channel == 'G':
                channel_image = g
            else:  # 'B'
                channel_image = b
            
            # Tạo ảnh RGB với chỉ một kênh
            if channel == 'R':
                display_image = Image.merge('RGB', (channel_image, Image.new('L', channel_image.size), 
                                                    Image.new('L', channel_image.size)))
            elif channel == 'G':
                display_image = Image.merge('RGB', (Image.new('L', channel_image.size), channel_image, 
                                                    Image.new('L', channel_image.size)))
            else:
                display_image = Image.merge('RGB', (Image.new('L', channel_image.size), 
                                                    Image.new('L', channel_image.size), channel_image))
            
            self.current_image = display_image
            self.display_image(display_image)
            
            self.matrix_text.delete(1.0, tk.END)
            self.matrix_text.insert(tk.END, f"Đã hiển thị kênh {name}")
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể hiển thị kênh màu:\n{str(e)}")
    
    def show_alpha_channel(self):
        """Hiển thị kênh Alpha (chỉ cho ảnh PNG)"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh để xử lý!")
            return
        
        try:
            # Kiểm tra xem ảnh có kênh alpha không
            if self.original_image.mode not in ('RGBA', 'LA'):
                messagebox.showinfo("Thông tin", 
                    "Ảnh này không có kênh Alpha.\n"
                    "Chỉ ảnh PNG với độ trong suốt mới có kênh Alpha.")
                return
            
            # Lấy kênh alpha
            if self.original_image.mode == 'RGBA':
                r, g, b, a = self.original_image.split()
            else:  # LA
                l, a = self.original_image.split()
            
            # Hiển thị kênh alpha dưới dạng ảnh xám
            self.current_image = a
            self.display_image(a)
            
            # Hiển thị ma trận alpha
            alpha_array = np.array(a)
            
            self.matrix_text.delete(1.0, tk.END)
            self.matrix_text.insert(tk.END, "=== KÊNH ALPHA ===\n\n")
            self.matrix_text.insert(tk.END, f"Kích thước: {alpha_array.shape}\n")
            self.matrix_text.insert(tk.END, f"Kiểu dữ liệu: {alpha_array.dtype}\n\n")
            
            # Hiển thị ma trận (giới hạn kích thước)
            if alpha_array.shape[0] > 50 or alpha_array.shape[1] > 50:
                self.matrix_text.insert(tk.END, 
                    f"Ma trận quá lớn để hiển thị đầy đủ ({alpha_array.shape[0]}x{alpha_array.shape[1]}).\n")
                self.matrix_text.insert(tk.END, "Hiển thị góc trên-trái (50x50):\n\n")
                display_array = alpha_array[:50, :50]
            else:
                display_array = alpha_array
            
            self.matrix_text.insert(tk.END, str(display_array))
            self.matrix_text.insert(tk.END, f"\n\n--- Thống kê Alpha ---\n")
            self.matrix_text.insert(tk.END, f"Min: {np.min(alpha_array)}\n")
            self.matrix_text.insert(tk.END, f"Max: {np.max(alpha_array)}\n")
            self.matrix_text.insert(tk.END, f"Mean: {np.mean(alpha_array):.2f}\n")
            
            # Chuyển tab sang ma trận
            self.display_notebook.select(1)
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể hiển thị kênh Alpha:\n{str(e)}")
    
    # === Chức năng tính toán chỉ số hình ảnh ===
    
    def calculate_brightness(self):
        """Tính độ sáng trung bình"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh để xử lý!")
            return
        
        try:
            # Chuyển sang grayscale
            gray_image = self.original_image.convert('L')
            gray_array = np.array(gray_image)
            
            # Tính độ sáng trung bình
            brightness = np.mean(gray_array)
            
            self.matrix_text.delete(1.0, tk.END)
            self.matrix_text.insert(tk.END, "=== ĐỘ SÁNG TRUNG BÌNH ===\n\n")
            self.matrix_text.insert(tk.END, f"Độ sáng trung bình: {brightness:.2f}\n")
            self.matrix_text.insert(tk.END, f"Khoảng giá trị: [0-255]\n\n")
            self.matrix_text.insert(tk.END, "Giải thích:\n")
            self.matrix_text.insert(tk.END, "- Độ sáng < 85: Ảnh tối\n")
            self.matrix_text.insert(tk.END, "- 85 ≤ Độ sáng < 170: Ảnh trung bình\n")
            self.matrix_text.insert(tk.END, "- Độ sáng ≥ 170: Ảnh sáng\n")
            
            # Chuyển tab
            self.display_notebook.select(1)
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tính độ sáng:\n{str(e)}")
    
    def calculate_contrast(self):
        """Tính độ tương phản"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh để xử lý!")
            return
        
        try:
            # Chuyển sang grayscale
            gray_image = self.original_image.convert('L')
            gray_array = np.array(gray_image)
            
            # Tính độ tương phản (độ lệch chuẩn)
            contrast = np.std(gray_array)
            
            # RMS contrast
            rms_contrast = np.sqrt(np.mean((gray_array - np.mean(gray_array)) ** 2))
            
            # Michelson contrast
            max_val = np.max(gray_array)
            min_val = np.min(gray_array)
            if max_val + min_val != 0:
                michelson = (max_val - min_val) / (max_val + min_val)
            else:
                michelson = 0
            
            self.matrix_text.delete(1.0, tk.END)
            self.matrix_text.insert(tk.END, "=== ĐỘ TƯƠNG PHẢN ===\n\n")
            self.matrix_text.insert(tk.END, f"Độ lệch chuẩn: {contrast:.2f}\n")
            self.matrix_text.insert(tk.END, f"RMS Contrast: {rms_contrast:.2f}\n")
            self.matrix_text.insert(tk.END, f"Michelson Contrast: {michelson:.4f}\n\n")
            self.matrix_text.insert(tk.END, "Giải thích:\n")
            self.matrix_text.insert(tk.END, "- Độ lệch chuẩn cao: Ảnh có độ tương phản cao\n")
            self.matrix_text.insert(tk.END, "- Độ lệch chuẩn thấp: Ảnh có độ tương phản thấp\n")
            
            # Chuyển tab
            self.display_notebook.select(1)
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tính độ tương phản:\n{str(e)}")
    
    def calculate_entropy(self):
        """Tính entropy của ảnh"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh để xử lý!")
            return
        
        try:
            # Chuyển sang grayscale
            gray_image = self.original_image.convert('L')
            gray_array = np.array(gray_image)
            
            # Tính histogram
            histogram, _ = np.histogram(gray_array, bins=256, range=(0, 256))
            
            # Chuẩn hóa histogram thành xác suất
            histogram = histogram / histogram.sum()
            
            # Tính entropy
            # Entropy = -sum(p * log2(p)) cho tất cả p > 0
            entropy = 0
            for prob in histogram:
                if prob > 0:
                    entropy -= prob * np.log2(prob)
            
            self.matrix_text.delete(1.0, tk.END)
            self.matrix_text.insert(tk.END, "=== ENTROPY ===\n\n")
            self.matrix_text.insert(tk.END, f"Entropy: {entropy:.4f} bits\n")
            self.matrix_text.insert(tk.END, f"Entropy tối đa (256 mức xám): 8 bits\n\n")
            self.matrix_text.insert(tk.END, "Giải thích:\n")
            self.matrix_text.insert(tk.END, "- Entropy đo lượng thông tin trong ảnh\n")
            self.matrix_text.insert(tk.END, "- Entropy cao: Ảnh có nhiều chi tiết, phân bố đều\n")
            self.matrix_text.insert(tk.END, "- Entropy thấp: Ảnh đơn giản, ít chi tiết\n")
            
            # Chuyển tab
            self.display_notebook.select(1)
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tính entropy:\n{str(e)}")
    
    def calculate_sharpness(self):
        """Tính độ sắc nét của ảnh"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh để xử lý!")
            return
        
        try:
            # Chuyển sang grayscale
            gray_image = self.original_image.convert('L')
            gray_array = np.array(gray_image, dtype=np.float64)
            
            # Tính gradient sử dụng Sobel
            # Gradient theo x
            gx = np.zeros_like(gray_array)
            gx[:, :-1] = np.diff(gray_array, axis=1)
            
            # Gradient theo y
            gy = np.zeros_like(gray_array)
            gy[:-1, :] = np.diff(gray_array, axis=0)
            
            # Magnitude của gradient
            gradient_magnitude = np.sqrt(gx**2 + gy**2)
            
            # Độ sắc nét là trung bình của gradient magnitude
            sharpness = np.mean(gradient_magnitude)
            
            # Variance of Laplacian (phương pháp khác)
            laplacian = np.zeros_like(gray_array)
            laplacian[1:-1, 1:-1] = (
                4 * gray_array[1:-1, 1:-1] -
                gray_array[:-2, 1:-1] - gray_array[2:, 1:-1] -
                gray_array[1:-1, :-2] - gray_array[1:-1, 2:]
            )
            laplacian_variance = np.var(laplacian)
            
            self.matrix_text.delete(1.0, tk.END)
            self.matrix_text.insert(tk.END, "=== ĐỘ SẮC NÉT ===\n\n")
            self.matrix_text.insert(tk.END, f"Độ sắc nét (Gradient): {sharpness:.2f}\n")
            self.matrix_text.insert(tk.END, f"Variance of Laplacian: {laplacian_variance:.2f}\n\n")
            self.matrix_text.insert(tk.END, "Giải thích:\n")
            self.matrix_text.insert(tk.END, "- Giá trị cao: Ảnh sắc nét, nhiều cạnh rõ ràng\n")
            self.matrix_text.insert(tk.END, "- Giá trị thấp: Ảnh mờ, ít cạnh\n")
            
            # Chuyển tab
            self.display_notebook.select(1)
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tính độ sắc nét:\n{str(e)}")
    
    def calculate_all_metrics(self):
        """Tính tất cả các chỉ số"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh để xử lý!")
            return
        
        try:
            # Chuyển sang grayscale
            gray_image = self.original_image.convert('L')
            gray_array = np.array(gray_image, dtype=np.float64)
            
            # 1. Độ sáng
            brightness = np.mean(gray_array)
            
            # 2. Độ tương phản
            contrast = np.std(gray_array)
            rms_contrast = np.sqrt(np.mean((gray_array - brightness) ** 2))
            
            # 3. Entropy
            histogram, _ = np.histogram(gray_array, bins=256, range=(0, 256))
            histogram = histogram / histogram.sum()
            entropy = 0
            for prob in histogram:
                if prob > 0:
                    entropy -= prob * np.log2(prob)
            
            # 4. Độ sắc nét
            gx = np.zeros_like(gray_array)
            gx[:, :-1] = np.diff(gray_array, axis=1)
            gy = np.zeros_like(gray_array)
            gy[:-1, :] = np.diff(gray_array, axis=0)
            gradient_magnitude = np.sqrt(gx**2 + gy**2)
            sharpness = np.mean(gradient_magnitude)
            
            # Hiển thị kết quả
            self.matrix_text.delete(1.0, tk.END)
            self.matrix_text.insert(tk.END, "=== TẤT CẢ CÁC CHỈ SỐ HÌNH ẢNH ===\n\n")
            
            self.matrix_text.insert(tk.END, "1. ĐỘ SÁNG TRUNG BÌNH:\n")
            self.matrix_text.insert(tk.END, f"   Giá trị: {brightness:.2f}\n")
            status = "Tối" if brightness < 85 else ("Trung bình" if brightness < 170 else "Sáng")
            self.matrix_text.insert(tk.END, f"   Đánh giá: {status}\n\n")
            
            self.matrix_text.insert(tk.END, "2. ĐỘ TƯƠNG PHẢN:\n")
            self.matrix_text.insert(tk.END, f"   Độ lệch chuẩn: {contrast:.2f}\n")
            self.matrix_text.insert(tk.END, f"   RMS Contrast: {rms_contrast:.2f}\n\n")
            
            self.matrix_text.insert(tk.END, "3. ENTROPY:\n")
            self.matrix_text.insert(tk.END, f"   Giá trị: {entropy:.4f} bits\n")
            self.matrix_text.insert(tk.END, f"   Tối đa: 8 bits\n\n")
            
            self.matrix_text.insert(tk.END, "4. ĐỘ SẮC NÉT:\n")
            self.matrix_text.insert(tk.END, f"   Gradient: {sharpness:.2f}\n\n")
            
            self.matrix_text.insert(tk.END, "--- THÔNG TIN ẢNH ---\n")
            self.matrix_text.insert(tk.END, f"Kích thước: {gray_array.shape}\n")
            self.matrix_text.insert(tk.END, f"Min: {np.min(gray_array):.0f}\n")
            self.matrix_text.insert(tk.END, f"Max: {np.max(gray_array):.0f}\n")
            
            # Chuyển tab
            self.display_notebook.select(1)
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tính các chỉ số:\n{str(e)}")
    
    # === Chức năng tăng cường chất lượng ảnh ===
    
    def create_negative(self):
        """Tạo ảnh âm bản: s = 255 - r"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh để xử lý!")
            return
        
        try:
            # Chuyển sang grayscale
            gray_image = self.original_image.convert('L')
            gray_array = np.array(gray_image)
            
            # Áp dụng công thức: s = 255 - r
            negative_array = 255 - gray_array
            
            # Chuyển về ảnh
            negative_image = Image.fromarray(negative_array.astype(np.uint8))
            self.current_image = negative_image
            self.display_image(negative_image)
            
            self.matrix_text.delete(1.0, tk.END)
            self.matrix_text.insert(tk.END, "=== ẢNH ÂM BẢN (NEGATIVE) ===\n\n")
            self.matrix_text.insert(tk.END, "Công thức: s = 255 - r\n\n")
            self.matrix_text.insert(tk.END, "Đã tạo ảnh âm bản thành công.\n")
            self.matrix_text.insert(tk.END, "Ảnh âm bản đảo ngược các giá trị pixel:\n")
            self.matrix_text.insert(tk.END, "- Vùng sáng → Tối\n")
            self.matrix_text.insert(tk.END, "- Vùng tối → Sáng\n")
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tạo ảnh âm bản:\n{str(e)}")
    
    def update_log_c_label(self, *args):
        """Cập nhật label cho log c"""
        c = self.log_c.get()
        self.log_c_label.config(text=f"c = {c:.2f}")
    
    def log_transform(self):
        """Biến đổi logarit cho ảnh thiếu sáng: s = c * log(1 + r)"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh để xử lý!")
            return
        
        try:
            # Chuyển sang grayscale
            gray_image = self.original_image.convert('L')
            gray_array = np.array(gray_image, dtype=np.float64)
            
            # Lấy giá trị c
            c = self.log_c.get()
            
            # Áp dụng công thức: s = c * log(1 + r)
            log_array = c * np.log1p(gray_array)
            
            # Chuẩn hóa về [0, 255]
            log_array = (log_array - np.min(log_array)) / (np.max(log_array) - np.min(log_array)) * 255
            
            # Chuyển về ảnh
            log_image = Image.fromarray(log_array.astype(np.uint8))
            self.current_image = log_image
            self.display_image(log_image)
            
            self.matrix_text.delete(1.0, tk.END)
            self.matrix_text.insert(tk.END, "=== BIẾN ĐỔI LOGARIT ===\n\n")
            self.matrix_text.insert(tk.END, f"Công thức: s = c * log(1 + r)\n")
            self.matrix_text.insert(tk.END, f"Hệ số c: {c:.2f}\n\n")
            self.matrix_text.insert(tk.END, "Ứng dụng: Tăng cường ảnh thiếu sáng\n")
            self.matrix_text.insert(tk.END, "- Làm sáng vùng tối\n")
            self.matrix_text.insert(tk.END, "- Nâng cao chi tiết trong vùng tối\n")
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể áp dụng biến đổi logarit:\n{str(e)}")
    
    def update_inv_log_c_label(self, *args):
        """Cập nhật label cho inverse log c"""
        c = self.inv_log_c.get()
        self.inv_log_c_label.config(text=f"c = {c:.2f}")
    
    def inverse_log_transform(self):
        """Biến đổi logarit ngược cho ảnh dư sáng: r = e^(s/c) - 1"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh để xử lý!")
            return
        
        try:
            # Chuyển sang grayscale
            gray_image = self.original_image.convert('L')
            gray_array = np.array(gray_image, dtype=np.float64)
            
            # Lấy giá trị c
            c = self.inv_log_c.get()
            
            # Chuẩn hóa về [0, 1]
            normalized = gray_array / 255.0
            
            # Áp dụng công thức: r = e^(s/c) - 1
            # Nhưng cần điều chỉnh để tránh overflow
            inv_log_array = np.expm1(normalized / c) if c > 0 else normalized
            
            # Chuẩn hóa về [0, 255]
            if np.max(inv_log_array) > np.min(inv_log_array):
                inv_log_array = (inv_log_array - np.min(inv_log_array)) / \
                                (np.max(inv_log_array) - np.min(inv_log_array)) * 255
            
            # Chuyển về ảnh
            inv_log_image = Image.fromarray(inv_log_array.astype(np.uint8))
            self.current_image = inv_log_image
            self.display_image(inv_log_image)
            
            self.matrix_text.delete(1.0, tk.END)
            self.matrix_text.insert(tk.END, "=== BIẾN ĐỔI LOGARIT NGƯỢC ===\n\n")
            self.matrix_text.insert(tk.END, f"Công thức: r = e^(s/c) - 1\n")
            self.matrix_text.insert(tk.END, f"Hệ số c: {c:.2f}\n\n")
            self.matrix_text.insert(tk.END, "Ứng dụng: Điều chỉnh ảnh dư sáng\n")
            self.matrix_text.insert(tk.END, "- Làm tối vùng sáng\n")
            self.matrix_text.insert(tk.END, "- Cân bằng độ sáng\n")
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể áp dụng biến đổi logarit ngược:\n{str(e)}")
    
    def update_gamma_label(self, *args):
        """Cập nhật label cho gamma"""
        gamma = self.gamma.get()
        self.gamma_label.config(text=f"γ = {gamma:.2f}")
    
    def gamma_transform(self):
        """Biến đổi gamma: s = c * r^γ"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh để xử lý!")
            return
        
        try:
            # Chuyển sang grayscale
            gray_image = self.original_image.convert('L')
            gray_array = np.array(gray_image, dtype=np.float64)
            
            # Lấy giá trị gamma
            gamma = self.gamma.get()
            
            # Chuẩn hóa về [0, 1]
            normalized = gray_array / 255.0
            
            # Áp dụng công thức: s = c * r^γ (với c = 1 cho đơn giản)
            gamma_array = np.power(normalized, gamma)
            
            # Chuyển về [0, 255]
            gamma_array = gamma_array * 255
            
            # Chuyển về ảnh
            gamma_image = Image.fromarray(gamma_array.astype(np.uint8))
            self.current_image = gamma_image
            self.display_image(gamma_image)
            
            self.matrix_text.delete(1.0, tk.END)
            self.matrix_text.insert(tk.END, "=== BIẾN ĐỔI GAMMA ===\n\n")
            self.matrix_text.insert(tk.END, f"Công thức: s = c * r^γ (c = 1)\n")
            self.matrix_text.insert(tk.END, f"Gamma (γ): {gamma:.2f}\n\n")
            self.matrix_text.insert(tk.END, "Ứng dụng: Điều chỉnh độ sáng tổng thể\n")
            
            if gamma < 1:
                self.matrix_text.insert(tk.END, "- γ < 1: Làm sáng ảnh\n")
                self.matrix_text.insert(tk.END, "- Tăng cường vùng tối\n")
            elif gamma > 1:
                self.matrix_text.insert(tk.END, "- γ > 1: Làm tối ảnh\n")
                self.matrix_text.insert(tk.END, "- Giảm độ sáng tổng thể\n")
            else:
                self.matrix_text.insert(tk.END, "- γ = 1: Không thay đổi\n")
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể áp dụng biến đổi gamma:\n{str(e)}")


def main():
    """Hàm main để chạy ứng dụng"""
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
