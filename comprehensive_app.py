"""
Ứng dụng Xử lý Ảnh Toàn diện - Bài 1-12 + Machine Learning
Comprehensive Image Processing Application - Exercises 1-12 + ML

Tác giả: Minhhieu-coder
Tích hợp tất cả các chức năng từ Bài 1 đến Bài 12 và Machine Learning
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from PIL import Image, ImageTk
import numpy as np
import cv2
import math
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from image_processing import ImageProcessor
from ml_processing import MLImageProcessor


class ComprehensiveImageApp:
    """
    Ứng dụng xử lý ảnh tích hợp đầy đủ các bài tập 1-12 và Machine Learning
    
    Comprehensive Image Processing Application integrating all exercises 1-12 and ML.
    Provides a unified GUI for all image processing operations including:
    - Basic conversions (grayscale, binary, channel split)
    - Contrast stretching and histogram processing
    - Noise removal and edge detection
    - Fourier transforms and frequency domain filtering (low-pass and high-pass)
    - Machine Learning: K-Means segmentation, feature extraction, object detection
    """
    
    # Constants
    MATRIX_DISPLAY_LIMIT = 50  # Maximum rows/cols to display in matrix view
    
    def __init__(self, root):
        """Khởi tạo ứng dụng"""
        self.root = root
        self.root.title("Ứng dụng Xử lý Ảnh Toàn diện - Bài 1-12 + ML")
        self.root.geometry("1600x900")
        
        # Biến lưu trữ ảnh
        self.original_image = None  # PIL Image (màu gốc)
        self.original_gray = None   # NumPy array (grayscale)
        self.processed_image = None # NumPy array (đã xử lý)
        self.current_display = None # Để hiển thị
        self.image_path = None
        
        # Tạo giao diện
        self.create_gui()
        
    def create_gui(self):
        """Tạo giao diện người dùng"""
        
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Left panel - Controls
        left_panel = ttk.Frame(main_frame, width=350)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 5))
        left_panel.pack_propagate(False)
        
        # File operations
        file_frame = ttk.LabelFrame(left_panel, text="📁 Tải và Lưu", padding=10)
        file_frame.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Button(file_frame, text="📂 Tải Ảnh", command=self.load_image, width=30).pack(pady=2)
        ttk.Button(file_frame, text="💾 Lưu Ảnh", command=self.save_image, width=30).pack(pady=2)
        ttk.Button(file_frame, text="🔄 Hiển thị Ảnh Gốc", command=self.show_original, width=30).pack(pady=2)
        
        self.image_info_label = ttk.Label(file_frame, text="Chưa có ảnh", font=("Arial", 9))
        self.image_info_label.pack(pady=5)
        
        # Create notebook for different exercise groups
        self.notebook = ttk.Notebook(left_panel)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=(0, 5))
        
        # Bài 1-3: Basic conversions
        self.create_bai1_3_tab()
        
        # Bài 4-6: Contrast and Histogram
        self.create_bai4_6_tab()
        
        # Bài 7-9: Filtering and Edge Detection
        self.create_bai7_9_tab()
        
        # Bài 10-11: Fourier Transform and Frequency Filters
        self.create_bai10_11_tab()
        
        # Bài 12: High-Pass Filters
        self.create_bai12_tab()
        
        # Machine Learning Tab
        self.create_ml_tab()
        
        # Right panel - Display
        right_panel = ttk.Frame(main_frame)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Display notebook
        self.display_notebook = ttk.Notebook(right_panel)
        self.display_notebook.pack(fill=tk.BOTH, expand=True)
        
        # Image display tab
        image_tab = ttk.Frame(self.display_notebook)
        self.display_notebook.add(image_tab, text="Hiển thị Ảnh")
        
        self.canvas = tk.Canvas(image_tab, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Info/Matrix tab
        info_tab = ttk.Frame(self.display_notebook)
        self.display_notebook.add(info_tab, text="Thông tin / Ma trận")
        
        self.info_text = scrolledtext.ScrolledText(info_tab, wrap=tk.WORD, font=("Courier", 9))
        self.info_text.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_label = ttk.Label(self.root, text="Sẵn sàng", relief=tk.SUNKEN)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)
    
    def create_bai1_3_tab(self):
        """Tạo tab cho Bài 1-3: Chuyển đổi cơ bản"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Bài 1-3: Cơ bản")
        
        # Scrollable frame
        canvas = tk.Canvas(tab)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Content
        ttk.Label(scrollable_frame, text="Chuyển đổi ảnh:", font=("Arial", 10, "bold")).pack(pady=5)
        ttk.Button(scrollable_frame, text="⚫ Ảnh Xám", command=self.convert_grayscale, width=28).pack(pady=2)
        
        ttk.Label(scrollable_frame, text="Ngưỡng nhị phân:").pack(pady=(10, 0))
        self.binary_threshold = tk.IntVar(value=127)
        threshold_slider = ttk.Scale(scrollable_frame, from_=0, to=255, 
                                     variable=self.binary_threshold, orient=tk.HORIZONTAL)
        threshold_slider.pack(fill=tk.X, padx=10, pady=2)
        self.threshold_label = ttk.Label(scrollable_frame, text="Ngưỡng: 127")
        self.threshold_label.pack()
        self.binary_threshold.trace_add("write", self.update_threshold_label)
        
        ttk.Button(scrollable_frame, text="⚪ Ảnh Nhị phân", command=self.convert_binary, width=28).pack(pady=2)
        
        ttk.Label(scrollable_frame, text="Tách kênh màu:", font=("Arial", 10, "bold")).pack(pady=(10, 5))
        ttk.Button(scrollable_frame, text="🔴 Kênh Đỏ", command=lambda: self.show_channel('R'), width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="🟢 Kênh Xanh lá", command=lambda: self.show_channel('G'), width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="🔵 Kênh Xanh dương", command=lambda: self.show_channel('B'), width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="👁️ Kênh Alpha", command=self.show_alpha_channel, width=28).pack(pady=2)
        
        ttk.Label(scrollable_frame, text="Ma trận:", font=("Arial", 10, "bold")).pack(pady=(10, 5))
        ttk.Button(scrollable_frame, text="📊 Ma trận Ảnh Xám", command=self.show_matrix, width=28).pack(pady=2)
    
    def create_bai4_6_tab(self):
        """Tạo tab cho Bài 4-6: Contrast và Histogram"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Bài 4-6: Contrast")
        
        # Scrollable frame
        canvas = tk.Canvas(tab)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bài 4
        ttk.Label(scrollable_frame, text="Bài 4: Contrast Stretching", font=("Arial", 10, "bold")).pack(pady=5)
        ttk.Button(scrollable_frame, text="Kéo dãn tuyến tính", command=self.contrast_stretching, width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Type 1 Clipping", command=self.contrast_clipping_t1, width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Type 2 Clipping", command=self.contrast_clipping_t2, width=28).pack(pady=2)
        
        # Bài 5
        ttk.Label(scrollable_frame, text="Bài 5: Histogram", font=("Arial", 10, "bold")).pack(pady=(10, 5))
        ttk.Button(scrollable_frame, text="Cân bằng Histogram", command=self.histogram_equalization, width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Hiển thị Histogram", command=self.show_histogram, width=28).pack(pady=2)
        
        # Bài 6
        ttk.Label(scrollable_frame, text="Bài 6: Advanced", font=("Arial", 10, "bold")).pack(pady=(10, 5))
        ttk.Button(scrollable_frame, text="Histogram Matching", command=self.histogram_matching, width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Adaptive (CLAHE)", command=self.adaptive_equalization, width=28).pack(pady=2)
    
    def create_bai7_9_tab(self):
        """Tạo tab cho Bài 7-9: Filters và Edge Detection"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Bài 7-9: Filters")
        
        # Scrollable frame
        canvas = tk.Canvas(tab)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bài 7
        ttk.Label(scrollable_frame, text="Bài 7: Noise Removal", font=("Arial", 10, "bold")).pack(pady=5)
        ttk.Button(scrollable_frame, text="➕ Thêm Nhiễu", command=self.add_noise, width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Average Filter 3x3", command=lambda: self.average_filter(3), width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Average Filter 5x5", command=lambda: self.average_filter(5), width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Median Filter 3x3", command=lambda: self.median_filter(3), width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Median Filter 5x5", command=lambda: self.median_filter(5), width=28).pack(pady=2)
        
        # Bài 8
        ttk.Label(scrollable_frame, text="Bài 8: Edge Detection", font=("Arial", 10, "bold")).pack(pady=(10, 5))
        ttk.Button(scrollable_frame, text="Sobel", command=self.sobel_edge, width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Prewitt", command=self.prewitt_edge, width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Roberts", command=self.roberts_edge, width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Kirsch", command=self.kirsch_edge, width=28).pack(pady=2)
        
        # Bài 9
        ttk.Label(scrollable_frame, text="Bài 9: Laplacian", font=("Arial", 10, "bold")).pack(pady=(10, 5))
        ttk.Button(scrollable_frame, text="Laplacian 4-neighbor", command=lambda: self.laplacian(4), width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Laplacian 8-neighbor", command=lambda: self.laplacian(8), width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="LoG (Gaussian)", command=self.log_edge, width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Sharpen (Laplacian)", command=lambda: self.sharpen('laplacian'), width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Sharpen (LoG)", command=lambda: self.sharpen('log'), width=28).pack(pady=2)
    
    def create_bai10_11_tab(self):
        """Tạo tab cho Bài 10-11: Fourier Transform"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Bài 10-11: Fourier")
        
        # Scrollable frame
        canvas = tk.Canvas(tab)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bài 10
        ttk.Label(scrollable_frame, text="Bài 10: Fourier Transform", font=("Arial", 10, "bold")).pack(pady=5)
        ttk.Button(scrollable_frame, text="🔄 FFT (Magnitude Spectrum)", 
                  command=self.show_fft, width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="↩️ Inverse FFT", 
                  command=self.inverse_fft, width=28).pack(pady=2)
        
        # Bài 11
        ttk.Label(scrollable_frame, text="Bài 11: Frequency Filters", font=("Arial", 10, "bold")).pack(pady=(10, 5))
        
        ttk.Label(scrollable_frame, text="Ideal Low-pass (Cutoff):").pack(pady=(5, 0))
        self.ideal_cutoff = tk.IntVar(value=30)
        cutoff_slider = ttk.Scale(scrollable_frame, from_=5, to=100, 
                                 variable=self.ideal_cutoff, orient=tk.HORIZONTAL)
        cutoff_slider.pack(fill=tk.X, padx=10, pady=2)
        self.cutoff_label = ttk.Label(scrollable_frame, text="Cutoff: 30")
        self.cutoff_label.pack()
        self.ideal_cutoff.trace_add("write", self.update_cutoff_label)
        
        ttk.Button(scrollable_frame, text="Ideal Low-pass Filter", 
                  command=self.ideal_lowpass, width=28).pack(pady=2)
        
        ttk.Label(scrollable_frame, text="Gaussian Low-pass (Sigma):").pack(pady=(10, 0))
        self.gaussian_sigma = tk.DoubleVar(value=30.0)
        sigma_slider = ttk.Scale(scrollable_frame, from_=5.0, to=100.0, 
                                variable=self.gaussian_sigma, orient=tk.HORIZONTAL)
        sigma_slider.pack(fill=tk.X, padx=10, pady=2)
        self.sigma_label = ttk.Label(scrollable_frame, text="Sigma: 30.0")
        self.sigma_label.pack()
        self.gaussian_sigma.trace_add("write", self.update_sigma_label)
        
        ttk.Button(scrollable_frame, text="Gaussian Low-pass Filter", 
                  command=self.gaussian_lowpass, width=28).pack(pady=2)
    
    def create_bai12_tab(self):
        """Tạo tab cho Bài 12: High-Pass Filters"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Bài 12: High-Pass")
        
        # Scrollable frame
        canvas = tk.Canvas(tab)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bài 12.1: Ideal High-pass
        ttk.Label(scrollable_frame, text="Bài 12.1: Ideal High-pass Filter", 
                 font=("Arial", 10, "bold")).pack(pady=5)
        
        ttk.Label(scrollable_frame, text="Cutoff Radius D0:").pack(pady=(5, 0))
        self.ideal_hp_cutoff = tk.IntVar(value=30)
        ideal_hp_slider = ttk.Scale(scrollable_frame, from_=10, to=100, 
                                    variable=self.ideal_hp_cutoff, orient=tk.HORIZONTAL)
        ideal_hp_slider.pack(fill=tk.X, padx=10, pady=2)
        self.ideal_hp_label = ttk.Label(scrollable_frame, text="D0: 30")
        self.ideal_hp_label.pack()
        self.ideal_hp_cutoff.trace_add("write", self.update_ideal_hp_label)
        
        ttk.Button(scrollable_frame, text="Apply Ideal High-pass", 
                  command=self.ideal_highpass, width=28).pack(pady=2)
        
        # Bài 12.2: Butterworth High-pass
        ttk.Label(scrollable_frame, text="Bài 12.2: Butterworth High-pass Filter", 
                 font=("Arial", 10, "bold")).pack(pady=(15, 5))
        
        ttk.Label(scrollable_frame, text="Cutoff Frequency D0:").pack(pady=(5, 0))
        self.butter_hp_d0 = tk.IntVar(value=30)
        butter_d0_slider = ttk.Scale(scrollable_frame, from_=10, to=100, 
                                     variable=self.butter_hp_d0, orient=tk.HORIZONTAL)
        butter_d0_slider.pack(fill=tk.X, padx=10, pady=2)
        self.butter_hp_d0_label = ttk.Label(scrollable_frame, text="D0: 30")
        self.butter_hp_d0_label.pack()
        self.butter_hp_d0.trace_add("write", self.update_butter_hp_d0_label)
        
        ttk.Label(scrollable_frame, text="Order (n):").pack(pady=(10, 0))
        self.butter_hp_n = tk.IntVar(value=2)
        butter_n_slider = ttk.Scale(scrollable_frame, from_=1, to=10, 
                                    variable=self.butter_hp_n, orient=tk.HORIZONTAL)
        butter_n_slider.pack(fill=tk.X, padx=10, pady=2)
        self.butter_hp_n_label = ttk.Label(scrollable_frame, text="n: 2")
        self.butter_hp_n_label.pack()
        self.butter_hp_n.trace_add("write", self.update_butter_hp_n_label)
        
        ttk.Button(scrollable_frame, text="Apply Butterworth High-pass", 
                  command=self.butterworth_highpass, width=28).pack(pady=2)
        
        # Info label
        info_text = ("High-pass filters enhance edges and details.\n"
                    "Butterworth provides smoother transition,\n"
                    "reducing ringing artifacts vs. Ideal filter.")
        ttk.Label(scrollable_frame, text=info_text, font=("Arial", 8), 
                 foreground="gray").pack(pady=(10, 5))
    
    def create_ml_tab(self):
        """Tạo tab cho Machine Learning"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="🤖 ML")
        
        # Scrollable frame
        canvas = tk.Canvas(tab)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # ML 1: K-Means Segmentation
        ttk.Label(scrollable_frame, text="ML 1: K-Means Segmentation", 
                 font=("Arial", 10, "bold")).pack(pady=5)
        
        ttk.Label(scrollable_frame, text="Số cụm (K):").pack(pady=(5, 0))
        self.kmeans_k = tk.IntVar(value=3)
        kmeans_slider = ttk.Scale(scrollable_frame, from_=2, to=10, 
                                  variable=self.kmeans_k, orient=tk.HORIZONTAL)
        kmeans_slider.pack(fill=tk.X, padx=10, pady=2)
        self.kmeans_k_label = ttk.Label(scrollable_frame, text="K: 3")
        self.kmeans_k_label.pack()
        self.kmeans_k.trace_add("write", self.update_kmeans_k_label)
        
        ttk.Button(scrollable_frame, text="K-Means Segmentation", 
                  command=self.kmeans_segment, width=28).pack(pady=2)
        
        # ML 2: Otsu Thresholding
        ttk.Label(scrollable_frame, text="ML 2: Otsu Thresholding", 
                 font=("Arial", 10, "bold")).pack(pady=(15, 5))
        
        ttk.Button(scrollable_frame, text="Otsu Auto Threshold", 
                  command=self.otsu_threshold, width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Adaptive Threshold", 
                  command=self.adaptive_threshold_ml, width=28).pack(pady=2)
        
        # ML 3: Edge Detection (ML version)
        ttk.Label(scrollable_frame, text="ML 3: ML Edge Detection", 
                 font=("Arial", 10, "bold")).pack(pady=(15, 5))
        
        ttk.Button(scrollable_frame, text="Canny-like Edge", 
                  command=self.ml_edge_detection, width=28).pack(pady=2)
        
        # ML 4: Feature Extraction
        ttk.Label(scrollable_frame, text="ML 4: Feature Extraction", 
                 font=("Arial", 10, "bold")).pack(pady=(15, 5))
        
        ttk.Button(scrollable_frame, text="Extract Features", 
                  command=self.extract_features, width=28).pack(pady=2)
        
        # ML 5: Object Detection
        ttk.Label(scrollable_frame, text="ML 5: Object Detection", 
                 font=("Arial", 10, "bold")).pack(pady=(15, 5))
        
        ttk.Button(scrollable_frame, text="Detect Objects", 
                  command=self.detect_objects, width=28).pack(pady=2)
        
        # ML 6: Morphological Operations
        ttk.Label(scrollable_frame, text="ML 6: Morphology", 
                 font=("Arial", 10, "bold")).pack(pady=(15, 5))
        
        ttk.Button(scrollable_frame, text="Erosion", 
                  command=lambda: self.morphological_op('erosion'), width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Dilation", 
                  command=lambda: self.morphological_op('dilation'), width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Opening", 
                  command=lambda: self.morphological_op('opening'), width=28).pack(pady=2)
        ttk.Button(scrollable_frame, text="Closing", 
                  command=lambda: self.morphological_op('closing'), width=28).pack(pady=2)
        
        # Info label
        info_text = ("Machine Learning cho Xử lý Ảnh:\n"
                    "• K-Means: Phân đoạn ảnh thành các vùng\n"
                    "• Otsu: Tự động tìm ngưỡng tối ưu\n"
                    "• Feature: Trích xuất đặc trưng ảnh")
        ttk.Label(scrollable_frame, text=info_text, font=("Arial", 8), 
                 foreground="gray").pack(pady=(10, 5))
    
    # ===== File Operations =====
    
    def load_image(self):
        """Tải ảnh"""
        filename = filedialog.askopenfilename(
            title="Chọn ảnh",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff"),
                ("All files", "*.*")
            ]
        )
        
        if filename:
            try:
                # Load as PIL for color channels
                self.original_image = Image.open(filename)
                self.image_path = filename
                
                # Convert to grayscale numpy array for processing
                self.original_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
                if self.original_gray is None:
                    # Fallback to PIL conversion
                    gray_pil = self.original_image.convert('L')
                    self.original_gray = np.array(gray_pil)
                
                self.processed_image = self.original_gray.copy()
                
                # Display
                self.display_image(self.original_image)
                
                # Update info
                width, height = self.original_image.size
                mode = self.original_image.mode
                filename_short = os.path.basename(filename)
                info = f"{filename_short}\n{width}x{height}\nMode: {mode}"
                self.image_info_label.config(text=info)
                self.status_label.config(text=f"Đã tải: {filename_short}")
                
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể tải ảnh:\n{str(e)}")
    
    def save_image(self):
        """Lưu ảnh"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Không có ảnh để lưu!")
            return
        
        filename = filedialog.asksaveasfilename(
            title="Lưu ảnh",
            defaultextension=".png",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg"),
                ("BMP files", "*.bmp"),
                ("All files", "*.*")
            ]
        )
        
        if filename:
            try:
                # Save using cv2
                cv2.imwrite(filename, self.processed_image)
                self.status_label.config(text=f"Đã lưu: {os.path.basename(filename)}")
                messagebox.showinfo("Thành công", "Đã lưu ảnh!")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể lưu ảnh:\n{str(e)}")
    
    def show_original(self):
        """Hiển thị ảnh gốc"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        self.processed_image = self.original_gray.copy()
        self.display_image(self.original_image)
        self.status_label.config(text="Hiển thị ảnh gốc")
    
    def display_image(self, image):
        """Hiển thị ảnh trên canvas"""
        if image is None:
            return
        
        # Convert to PIL if needed
        if isinstance(image, np.ndarray):
            if len(image.shape) == 2:
                pil_image = Image.fromarray(image)
            else:
                pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        else:
            pil_image = image
        
        # Get canvas size
        self.canvas.update()
        canvas_width = max(self.canvas.winfo_width(), 100)
        canvas_height = max(self.canvas.winfo_height(), 100)
        
        # Resize to fit
        img_copy = pil_image.copy()
        img_copy.thumbnail((canvas_width - 20, canvas_height - 20), Image.Resampling.LANCZOS)
        
        # Display
        self.current_display = ImageTk.PhotoImage(img_copy)
        self.canvas.delete("all")
        self.canvas.create_image(
            canvas_width // 2, canvas_height // 2,
            image=self.current_display, anchor=tk.CENTER
        )
    
    # ===== Bài 1-3 Methods =====
    
    def convert_grayscale(self):
        """Chuyển sang ảnh xám"""
        if self.original_gray is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        self.processed_image = self.original_gray.copy()
        self.display_image(self.processed_image)
        self.status_label.config(text="Chuyển sang ảnh xám")
    
    def update_threshold_label(self, *args):
        """Cập nhật label ngưỡng"""
        val = self.binary_threshold.get()
        self.threshold_label.config(text=f"Ngưỡng: {val}")
    
    def convert_binary(self):
        """Chuyển sang ảnh nhị phân"""
        if self.original_gray is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            threshold = self.binary_threshold.get()
            binary = (self.original_gray > threshold) * 255
            self.processed_image = binary.astype(np.uint8)
            self.display_image(self.processed_image)
            self.status_label.config(text=f"Ảnh nhị phân (ngưỡng={threshold})")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def show_channel(self, channel):
        """Hiển thị kênh màu"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            # Convert to RGB if needed
            if self.original_image.mode != 'RGB':
                rgb_img = self.original_image.convert('RGB')
            else:
                rgb_img = self.original_image
            
            r, g, b = rgb_img.split()
            
            # Create single channel image
            if channel == 'R':
                display = Image.merge('RGB', (r, Image.new('L', r.size), Image.new('L', r.size)))
                self.processed_image = np.array(r)
                name = "Đỏ"
            elif channel == 'G':
                display = Image.merge('RGB', (Image.new('L', g.size), g, Image.new('L', g.size)))
                self.processed_image = np.array(g)
                name = "Xanh lá"
            else:  # B
                display = Image.merge('RGB', (Image.new('L', b.size), Image.new('L', b.size), b))
                self.processed_image = np.array(b)
                name = "Xanh dương"
            
            self.display_image(display)
            self.status_label.config(text=f"Kênh {name}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def show_alpha_channel(self):
        """Hiển thị kênh Alpha"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        if self.original_image.mode not in ('RGBA', 'LA'):
            messagebox.showinfo("Thông tin", "Ảnh này không có kênh Alpha")
            return
        
        try:
            if self.original_image.mode == 'RGBA':
                r, g, b, a = self.original_image.split()
            else:
                l, a = self.original_image.split()
            
            self.processed_image = np.array(a)
            self.display_image(a)
            self.status_label.config(text="Kênh Alpha")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def show_matrix(self):
        """Hiển thị ma trận ảnh xám"""
        if self.original_gray is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, "=== MA TRẬN ẢNH XÁM ===\n\n")
            self.info_text.insert(tk.END, f"Kích thước: {self.original_gray.shape}\n")
            self.info_text.insert(tk.END, f"Kiểu: {self.original_gray.dtype}\n\n")
            
            # Show limited matrix
            limit = self.MATRIX_DISPLAY_LIMIT
            if self.original_gray.shape[0] > limit or self.original_gray.shape[1] > limit:
                self.info_text.insert(tk.END, f"Ma trận lớn, hiển thị {limit}x{limit} đầu:\n\n")
                display = self.original_gray[:limit, :limit]
            else:
                display = self.original_gray
            
            self.info_text.insert(tk.END, str(display))
            self.info_text.insert(tk.END, f"\n\n--- Thống kê ---\n")
            self.info_text.insert(tk.END, f"Min: {self.original_gray.min()}\n")
            self.info_text.insert(tk.END, f"Max: {self.original_gray.max()}\n")
            self.info_text.insert(tk.END, f"Mean: {self.original_gray.mean():.2f}\n")
            self.info_text.insert(tk.END, f"Std: {self.original_gray.std():.2f}\n")
            
            self.display_notebook.select(1)
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    # ===== Bài 4-6 Methods =====
    
    def contrast_stretching(self):
        """Kéo dãn tương phản tuyến tính"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            result = ImageProcessor.contrast_stretching(self.processed_image)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="Đã kéo dãn tương phản tuyến tính")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def contrast_clipping_t1(self):
        """Type 1 clipping"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            result = ImageProcessor.contrast_clipping_type1(self.processed_image, 50, 200)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="Type 1 Clipping [50, 200]")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def contrast_clipping_t2(self):
        """Type 2 clipping"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            result = ImageProcessor.contrast_clipping_type2(self.processed_image)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="Type 2 Region-based Clipping")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def histogram_equalization(self):
        """Cân bằng histogram"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            result, _ = ImageProcessor.histogram_equalization(self.processed_image)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="Cân bằng Histogram")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def show_histogram(self):
        """Hiển thị histogram"""
        if self.original_gray is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            # Create window
            hist_window = tk.Toplevel(self.root)
            hist_window.title("Histogram")
            hist_window.geometry("1000x400")
            
            fig = Figure(figsize=(10, 4))
            
            # Original
            ax1 = fig.add_subplot(121)
            hist_orig = ImageProcessor.calculate_histogram(self.original_gray)
            ax1.bar(range(256), hist_orig, color='blue', alpha=0.7)
            ax1.set_title('Original')
            ax1.set_xlabel('Intensity')
            ax1.set_ylabel('Frequency')
            ax1.grid(True, alpha=0.3)
            
            # Processed
            ax2 = fig.add_subplot(122)
            hist_proc = ImageProcessor.calculate_histogram(self.processed_image)
            ax2.bar(range(256), hist_proc, color='green', alpha=0.7)
            ax2.set_title('Processed')
            ax2.set_xlabel('Intensity')
            ax2.set_ylabel('Frequency')
            ax2.grid(True, alpha=0.3)
            
            fig.tight_layout()
            
            canvas = FigureCanvasTkAgg(fig, master=hist_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def histogram_matching(self):
        """Histogram matching"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            # Gaussian reference
            x = np.arange(256)
            ref_hist = np.exp(-((x - 128) ** 2) / (2 * 50 ** 2))
            ref_hist = (ref_hist / ref_hist.sum() * self.processed_image.size).astype(np.uint64)
            
            result = ImageProcessor.histogram_matching(self.processed_image, ref_hist)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="Histogram Matching (Gaussian)")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def adaptive_equalization(self):
        """CLAHE"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            result = ImageProcessor.adaptive_histogram_equalization(self.processed_image)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="Adaptive Equalization (CLAHE)")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    # ===== Bài 7-9 Methods =====
    
    def add_noise(self):
        """Thêm nhiễu"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            result = ImageProcessor.add_salt_pepper_noise(self.processed_image)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="Đã thêm nhiễu salt & pepper")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def average_filter(self, size):
        """Average filter"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            result = ImageProcessor.average_filter(self.processed_image, size)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text=f"Average Filter {size}x{size}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def median_filter(self, size):
        """Median filter"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            result = ImageProcessor.median_filter(self.processed_image, size)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text=f"Median Filter {size}x{size}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def sobel_edge(self):
        """Sobel"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            magnitude, _, _ = ImageProcessor.sobel_edge_detection(self.processed_image)
            self.processed_image = magnitude
            self.display_image(magnitude)
            self.status_label.config(text="Sobel Edge Detection")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def prewitt_edge(self):
        """Prewitt"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            magnitude, _, _ = ImageProcessor.prewitt_edge_detection(self.processed_image)
            self.processed_image = magnitude
            self.display_image(magnitude)
            self.status_label.config(text="Prewitt Edge Detection")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def roberts_edge(self):
        """Roberts"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            magnitude, _, _ = ImageProcessor.roberts_edge_detection(self.processed_image)
            self.processed_image = magnitude
            self.display_image(magnitude)
            self.status_label.config(text="Roberts Edge Detection")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def kirsch_edge(self):
        """Kirsch"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            magnitude = ImageProcessor.kirsch_edge_detection(self.processed_image)
            self.processed_image = magnitude
            self.display_image(magnitude)
            self.status_label.config(text="Kirsch Edge Detection")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def laplacian(self, neighbors):
        """Laplacian"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            if neighbors == 4:
                result = ImageProcessor.laplacian_4_neighbor(self.processed_image)
            else:
                result = ImageProcessor.laplacian_8_neighbor(self.processed_image)
            
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text=f"Laplacian {neighbors}-neighbor")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def log_edge(self):
        """LoG"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            result = ImageProcessor.laplacian_of_gaussian(self.processed_image)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="Laplacian of Gaussian (LoG)")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def sharpen(self, method):
        """Sharpen"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            result = ImageProcessor.sharpen_image(self.processed_image, method)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text=f"Sharpen ({method})")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    # ===== Bài 10-11 Methods =====
    
    def show_fft(self):
        """Hiển thị FFT magnitude spectrum"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            magnitude, phase = ImageProcessor.fourier_transform(self.processed_image)
            
            # Store for inverse
            self.fft_magnitude = magnitude
            self.fft_phase = phase
            
            # Display magnitude spectrum
            magnitude_display = ImageProcessor.get_magnitude_spectrum_display(magnitude)
            self.display_image(magnitude_display)
            
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, "=== FOURIER TRANSFORM ===\n\n")
            self.info_text.insert(tk.END, "Đã tính toán Fourier Transform\n")
            self.info_text.insert(tk.END, f"Magnitude shape: {magnitude.shape}\n")
            self.info_text.insert(tk.END, f"Magnitude range: [{magnitude.min():.2f}, {magnitude.max():.2f}]\n\n")
            self.info_text.insert(tk.END, "Hiển thị: Magnitude Spectrum (log scale)\n")
            self.info_text.insert(tk.END, "Tần số thấp ở giữa, tần số cao ở rìa\n")
            self.display_notebook.select(1)
            
            self.status_label.config(text="FFT Magnitude Spectrum")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def inverse_fft(self):
        """Inverse FFT"""
        if not hasattr(self, 'fft_magnitude') or not hasattr(self, 'fft_phase'):
            messagebox.showwarning("Cảnh báo", "Chưa có FFT! Hãy chạy FFT trước.")
            return
        
        try:
            result = ImageProcessor.inverse_fourier_transform(self.fft_magnitude, self.fft_phase)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="Inverse FFT (Reconstructed)")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def update_cutoff_label(self, *args):
        """Cập nhật label cutoff"""
        val = self.ideal_cutoff.get()
        self.cutoff_label.config(text=f"Cutoff: {val}")
    
    def ideal_lowpass(self):
        """Ideal low-pass filter"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            cutoff = self.ideal_cutoff.get()
            result = ImageProcessor.ideal_lowpass_filter(self.processed_image, cutoff)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text=f"Ideal Low-pass (cutoff={cutoff})")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def update_sigma_label(self, *args):
        """Cập nhật label sigma"""
        val = self.gaussian_sigma.get()
        self.sigma_label.config(text=f"Sigma: {val:.1f}")
    
    def gaussian_lowpass(self):
        """Gaussian low-pass filter"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            sigma = self.gaussian_sigma.get()
            result = ImageProcessor.gaussian_lowpass_filter(self.processed_image, sigma)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text=f"Gaussian Low-pass (sigma={sigma:.1f})")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    # ===== Bài 12 Methods =====
    
    def update_ideal_hp_label(self, *args):
        """Cập nhật label cho Ideal High-pass cutoff"""
        val = self.ideal_hp_cutoff.get()
        self.ideal_hp_label.config(text=f"D0: {val}")
    
    def update_butter_hp_d0_label(self, *args):
        """Cập nhật label cho Butterworth High-pass D0"""
        val = self.butter_hp_d0.get()
        self.butter_hp_d0_label.config(text=f"D0: {val}")
    
    def update_butter_hp_n_label(self, *args):
        """Cập nhật label cho Butterworth High-pass n"""
        val = self.butter_hp_n.get()
        self.butter_hp_n_label.config(text=f"n: {val}")
    
    def ideal_highpass(self):
        """Bài 12.1: Ideal high-pass filter"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            cutoff = self.ideal_hp_cutoff.get()
            result = ImageProcessor.ideal_highpass_filter(self.processed_image, cutoff)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text=f"Ideal High-pass (D0={cutoff})")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def butterworth_highpass(self):
        """Bài 12.2: Butterworth high-pass filter"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            D0 = self.butter_hp_d0.get()
            n = self.butter_hp_n.get()
            result = ImageProcessor.butterworth_highpass_filter(self.processed_image, D0, n)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text=f"Butterworth High-pass (D0={D0}, n={n})")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    # ===== Machine Learning Methods =====
    
    def update_kmeans_k_label(self, *args):
        """Cập nhật label cho K-Means K"""
        val = self.kmeans_k.get()
        self.kmeans_k_label.config(text=f"K: {val}")
    
    def kmeans_segment(self):
        """ML 1: K-Means image segmentation"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            k = self.kmeans_k.get()
            result, centers = MLImageProcessor.kmeans_segmentation(self.processed_image, k)
            self.processed_image = result
            self.display_image(result)
            
            # Show info
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, "=== K-MEANS SEGMENTATION ===\n\n")
            self.info_text.insert(tk.END, f"Số cụm (K): {k}\n")
            self.info_text.insert(tk.END, f"Cluster centers: {centers}\n\n")
            self.info_text.insert(tk.END, "Mô tả:\n")
            self.info_text.insert(tk.END, "K-Means phân đoạn ảnh thành K vùng\n")
            self.info_text.insert(tk.END, "dựa trên độ sáng pixel.\n")
            self.display_notebook.select(1)
            
            self.status_label.config(text=f"K-Means Segmentation (K={k})")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def otsu_threshold(self):
        """ML 2: Otsu automatic thresholding"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            result, threshold = MLImageProcessor.otsu_threshold(self.processed_image)
            self.processed_image = result
            self.display_image(result)
            
            # Show info
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, "=== OTSU THRESHOLDING ===\n\n")
            self.info_text.insert(tk.END, f"Ngưỡng tối ưu: {threshold}\n\n")
            self.info_text.insert(tk.END, "Mô tả:\n")
            self.info_text.insert(tk.END, "Otsu tự động tìm ngưỡng tối ưu\n")
            self.info_text.insert(tk.END, "để phân chia foreground/background\n")
            self.info_text.insert(tk.END, "bằng cách minimize within-class variance.\n")
            self.display_notebook.select(1)
            
            self.status_label.config(text=f"Otsu Threshold = {threshold}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def adaptive_threshold_ml(self):
        """ML 2.2: Adaptive thresholding"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            result = MLImageProcessor.adaptive_threshold_ml(self.processed_image)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="Adaptive Threshold (ML)")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def ml_edge_detection(self):
        """ML 3: ML-based edge detection"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            result = MLImageProcessor.detect_edges_ml(self.processed_image)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="ML Edge Detection (Canny-like)")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def extract_features(self):
        """ML 4: Extract image features"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            # Extract all feature types
            hist_features = MLImageProcessor.extract_histogram_features(self.processed_image)
            texture_features = MLImageProcessor.extract_texture_features(self.processed_image)
            stat_features = MLImageProcessor.extract_statistical_features(self.processed_image)
            combined = MLImageProcessor.extract_combined_features(self.processed_image)
            
            # Show info
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, "=== FEATURE EXTRACTION ===\n\n")
            
            self.info_text.insert(tk.END, "--- Histogram Features (16 bins) ---\n")
            self.info_text.insert(tk.END, f"Shape: {hist_features.shape}\n")
            self.info_text.insert(tk.END, f"Values: {np.round(hist_features, 4)}\n\n")
            
            self.info_text.insert(tk.END, "--- Texture Features ---\n")
            self.info_text.insert(tk.END, f"Shape: {texture_features.shape}\n")
            self.info_text.insert(tk.END, f"Mean gradient: {texture_features[0]:.4f}\n")
            self.info_text.insert(tk.END, f"Std gradient: {texture_features[1]:.4f}\n")
            self.info_text.insert(tk.END, f"Max gradient: {texture_features[2]:.4f}\n\n")
            
            self.info_text.insert(tk.END, "--- Statistical Features ---\n")
            self.info_text.insert(tk.END, f"Shape: {stat_features.shape}\n")
            self.info_text.insert(tk.END, f"Mean: {stat_features[0]:.4f}\n")
            self.info_text.insert(tk.END, f"Std: {stat_features[1]:.4f}\n")
            self.info_text.insert(tk.END, f"Contrast: {stat_features[2]:.4f}\n")
            self.info_text.insert(tk.END, f"Skewness: {stat_features[4]:.4f}\n")
            self.info_text.insert(tk.END, f"Kurtosis: {stat_features[5]:.4f}\n")
            self.info_text.insert(tk.END, f"Energy: {stat_features[6]:.4f}\n")
            self.info_text.insert(tk.END, f"Entropy: {stat_features[7]:.4f}\n\n")
            
            self.info_text.insert(tk.END, "--- Combined Feature Vector ---\n")
            self.info_text.insert(tk.END, f"Total features: {combined.shape[0]}\n")
            
            self.display_notebook.select(1)
            self.status_label.config(text="Extracted image features")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def detect_objects(self):
        """ML 5: Simple object detection"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            # First apply Otsu to get binary image
            binary, threshold = MLImageProcessor.otsu_threshold(self.processed_image)
            
            # Detect objects
            labels, objects = MLImageProcessor.simple_object_detection(binary, min_area=50)
            
            # Create visualization
            if len(self.processed_image.shape) == 2:
                vis = cv2.cvtColor(self.processed_image, cv2.COLOR_GRAY2BGR)
            else:
                vis = self.processed_image.copy()
            
            # Draw bounding boxes
            for obj in objects:
                x, y = obj['x'], obj['y']
                w, h = obj['width'], obj['height']
                cx, cy = int(obj['centroid_x']), int(obj['centroid_y'])
                
                cv2.rectangle(vis, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.circle(vis, (cx, cy), 3, (255, 0, 0), -1)
            
            self.display_image(vis)
            
            # Show info
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, "=== OBJECT DETECTION ===\n\n")
            self.info_text.insert(tk.END, f"Otsu threshold used: {threshold}\n")
            self.info_text.insert(tk.END, f"Objects detected: {len(objects)}\n\n")
            
            for i, obj in enumerate(objects):
                self.info_text.insert(tk.END, f"--- Object {i+1} ---\n")
                self.info_text.insert(tk.END, f"  Area: {obj['area']} pixels\n")
                self.info_text.insert(tk.END, f"  Position: ({obj['x']}, {obj['y']})\n")
                self.info_text.insert(tk.END, f"  Size: {obj['width']} x {obj['height']}\n")
                self.info_text.insert(tk.END, f"  Centroid: ({obj['centroid_x']:.1f}, {obj['centroid_y']:.1f})\n\n")
            
            self.display_notebook.select(1)
            self.status_label.config(text=f"Detected {len(objects)} objects")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    
    def morphological_op(self, operation: str):
        """ML 6: Morphological operations"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh!")
            return
        
        try:
            result = MLImageProcessor.morphological_operations(self.processed_image, operation)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text=f"Morphology: {operation}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))


def main():
    """Main entry point"""
    root = tk.Tk()
    app = ComprehensiveImageApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
