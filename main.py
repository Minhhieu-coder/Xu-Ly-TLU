"""
Image Processing GUI Application
Main application window with all image processing features from Bài 4-9
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import os

from image_processing import ImageProcessor


class ImageProcessingApp:
    """Main GUI application for image processing"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng Xử lý Ảnh - Bài 4-9")
        self.root.geometry("1400x900")
        
        # Image data
        self.original_image = None
        self.processed_image = None
        self.current_display = None
        
        # Setup UI
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        
        # Main container
        main_container = ttk.Frame(self.root, padding="10")
        main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_container.columnconfigure(1, weight=1)
        main_container.rowconfigure(1, weight=1)
        
        # Left panel - Controls
        control_panel = ttk.Frame(main_container, padding="5")
        control_panel.grid(row=0, column=0, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # File operations
        file_frame = ttk.LabelFrame(control_panel, text="File Operations", padding="5")
        file_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(file_frame, text="Load Image", command=self.load_image).grid(row=0, column=0, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(file_frame, text="Save Result", command=self.save_image).grid(row=1, column=0, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(file_frame, text="Add Salt & Pepper Noise", command=self.add_noise).grid(row=2, column=0, pady=2, sticky=(tk.W, tk.E))
        
        # Bài 4: Contrast Stretching
        bai4_frame = ttk.LabelFrame(control_panel, text="Bài 4: Contrast Stretching", padding="5")
        bai4_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(bai4_frame, text="Linear Stretching", command=self.contrast_stretching).grid(row=0, column=0, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(bai4_frame, text="Type 1 Clipping", command=self.contrast_clipping_type1).grid(row=1, column=0, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(bai4_frame, text="Type 2 Clipping", command=self.contrast_clipping_type2).grid(row=2, column=0, pady=2, sticky=(tk.W, tk.E))
        
        # Bài 5: Histogram Equalization
        bai5_frame = ttk.LabelFrame(control_panel, text="Bài 5: Histogram Equalization", padding="5")
        bai5_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(bai5_frame, text="Standard Equalization", command=self.histogram_equalization).grid(row=0, column=0, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(bai5_frame, text="Show Histogram", command=self.show_histogram).grid(row=1, column=0, pady=2, sticky=(tk.W, tk.E))
        
        # Bài 6: Advanced Histogram
        bai6_frame = ttk.LabelFrame(control_panel, text="Bài 6: Advanced Histogram", padding="5")
        bai6_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(bai6_frame, text="Histogram Matching", command=self.histogram_matching).grid(row=0, column=0, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(bai6_frame, text="Adaptive Equalization", command=self.adaptive_equalization).grid(row=1, column=0, pady=2, sticky=(tk.W, tk.E))
        
        # Bài 7: Noise Removal
        bai7_frame = ttk.LabelFrame(control_panel, text="Bài 7: Noise Removal", padding="5")
        bai7_frame.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(bai7_frame, text="Average Filter 3x3", command=lambda: self.average_filter(3)).grid(row=0, column=0, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(bai7_frame, text="Average Filter 5x5", command=lambda: self.average_filter(5)).grid(row=1, column=0, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(bai7_frame, text="Median Filter 3x3", command=lambda: self.median_filter(3)).grid(row=2, column=0, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(bai7_frame, text="Median Filter 5x5", command=lambda: self.median_filter(5)).grid(row=3, column=0, pady=2, sticky=(tk.W, tk.E))
        
        # Bài 8: Edge Detection
        bai8_frame = ttk.LabelFrame(control_panel, text="Bài 8: Edge Detection", padding="5")
        bai8_frame.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(bai8_frame, text="Sobel", command=self.sobel_edge).grid(row=0, column=0, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(bai8_frame, text="Prewitt", command=self.prewitt_edge).grid(row=1, column=0, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(bai8_frame, text="Roberts", command=self.roberts_edge).grid(row=2, column=0, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(bai8_frame, text="Kirsch", command=self.kirsch_edge).grid(row=3, column=0, pady=2, sticky=(tk.W, tk.E))
        
        # Bài 9: Laplacian & Sharpening
        bai9_frame = ttk.LabelFrame(control_panel, text="Bài 9: Laplacian & Sharpening", padding="5")
        bai9_frame.grid(row=6, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(bai9_frame, text="Laplacian 4-neighbor", command=lambda: self.laplacian_edge(4)).grid(row=0, column=0, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(bai9_frame, text="Laplacian 8-neighbor", command=lambda: self.laplacian_edge(8)).grid(row=1, column=0, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(bai9_frame, text="LoG (Laplacian of Gaussian)", command=self.log_edge).grid(row=2, column=0, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(bai9_frame, text="Sharpen (Laplacian)", command=lambda: self.sharpen('laplacian')).grid(row=3, column=0, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(bai9_frame, text="Sharpen (LoG)", command=lambda: self.sharpen('log')).grid(row=4, column=0, pady=2, sticky=(tk.W, tk.E))
        
        # Right panel - Image display
        display_panel = ttk.Frame(main_container)
        display_panel.grid(row=0, column=1, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        
        # Image canvas
        self.canvas = tk.Canvas(display_panel, bg='gray')
        self.canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        display_panel.columnconfigure(0, weight=1)
        display_panel.rowconfigure(0, weight=1)
        
        # Status bar
        self.status_label = ttk.Label(main_container, text="Ready", relief=tk.SUNKEN)
        self.status_label.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))
    
    def load_image(self):
        """Load an image file"""
        filename = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                # Load image as grayscale
                self.original_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
                if self.original_image is None:
                    raise ValueError("Failed to load image")
                
                self.processed_image = self.original_image.copy()
                self.display_image(self.original_image)
                self.status_label.config(text=f"Loaded: {os.path.basename(filename)} - Size: {self.original_image.shape}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def save_image(self):
        """Save the processed image"""
        if self.processed_image is None:
            messagebox.showwarning("Warning", "No processed image to save")
            return
        
        filename = filedialog.asksaveasfilename(
            title="Save Image",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                cv2.imwrite(filename, self.processed_image)
                self.status_label.config(text=f"Saved: {os.path.basename(filename)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save image: {str(e)}")
    
    def display_image(self, image):
        """Display image on canvas"""
        if image is None:
            return
        
        # Convert to PIL Image
        if len(image.shape) == 2:
            pil_image = Image.fromarray(image)
        else:
            pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        # Resize to fit canvas
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        if canvas_width > 1 and canvas_height > 1:
            pil_image.thumbnail((canvas_width, canvas_height), Image.Resampling.LANCZOS)
        
        # Convert to PhotoImage and display
        self.current_display = ImageTk.PhotoImage(pil_image)
        self.canvas.delete("all")
        self.canvas.create_image(
            canvas_width // 2, canvas_height // 2,
            image=self.current_display,
            anchor=tk.CENTER
        )
    
    def add_noise(self):
        """Add salt and pepper noise to current image"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            noisy = ImageProcessor.add_salt_pepper_noise(self.original_image)
            self.processed_image = noisy
            self.display_image(noisy)
            self.status_label.config(text="Added salt & pepper noise")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add noise: {str(e)}")
    
    # Bài 4 methods
    def contrast_stretching(self):
        """Apply linear contrast stretching"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            result = ImageProcessor.contrast_stretching(self.processed_image)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="Applied linear contrast stretching")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply contrast stretching: {str(e)}")
    
    def contrast_clipping_type1(self):
        """Apply type 1 contrast clipping"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            # Simple dialog for thresholds
            dialog = tk.Toplevel(self.root)
            dialog.title("Type 1 Clipping Parameters")
            dialog.geometry("300x150")
            
            ttk.Label(dialog, text="Low Threshold (0-255):").grid(row=0, column=0, padx=5, pady=5)
            low_var = tk.IntVar(value=50)
            ttk.Entry(dialog, textvariable=low_var).grid(row=0, column=1, padx=5, pady=5)
            
            ttk.Label(dialog, text="High Threshold (0-255):").grid(row=1, column=0, padx=5, pady=5)
            high_var = tk.IntVar(value=200)
            ttk.Entry(dialog, textvariable=high_var).grid(row=1, column=1, padx=5, pady=5)
            
            def apply():
                result = ImageProcessor.contrast_clipping_type1(
                    self.processed_image, low_var.get(), high_var.get()
                )
                self.processed_image = result
                self.display_image(result)
                self.status_label.config(text=f"Applied Type 1 clipping [{low_var.get()}, {high_var.get()}]")
                dialog.destroy()
            
            ttk.Button(dialog, text="Apply", command=apply).grid(row=2, column=0, columnspan=2, pady=10)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply Type 1 clipping: {str(e)}")
    
    def contrast_clipping_type2(self):
        """Apply type 2 contrast clipping"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            result = ImageProcessor.contrast_clipping_type2(self.processed_image)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="Applied Type 2 region-based clipping")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply Type 2 clipping: {str(e)}")
    
    # Bài 5 methods
    def histogram_equalization(self):
        """Apply standard histogram equalization"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            result, hist = ImageProcessor.histogram_equalization(self.processed_image)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="Applied histogram equalization")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply histogram equalization: {str(e)}")
    
    def show_histogram(self):
        """Show histogram comparison"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            # Create new window for histogram
            hist_window = tk.Toplevel(self.root)
            hist_window.title("Histogram Analysis")
            hist_window.geometry("1000x400")
            
            fig = Figure(figsize=(10, 4))
            
            # Original histogram
            ax1 = fig.add_subplot(121)
            hist_orig = ImageProcessor.calculate_histogram(self.original_image)
            ax1.bar(range(256), hist_orig, color='blue', alpha=0.7)
            ax1.set_title('Original Image Histogram')
            ax1.set_xlabel('Pixel Intensity')
            ax1.set_ylabel('Frequency')
            ax1.grid(True, alpha=0.3)
            
            # Processed histogram
            ax2 = fig.add_subplot(122)
            hist_proc = ImageProcessor.calculate_histogram(self.processed_image)
            ax2.bar(range(256), hist_proc, color='green', alpha=0.7)
            ax2.set_title('Processed Image Histogram')
            ax2.set_xlabel('Pixel Intensity')
            ax2.set_ylabel('Frequency')
            ax2.grid(True, alpha=0.3)
            
            fig.tight_layout()
            
            canvas = FigureCanvasTkAgg(fig, master=hist_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to show histogram: {str(e)}")
    
    # Bài 6 methods
    def histogram_matching(self):
        """Apply histogram matching"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            # For demonstration, create a reference histogram (bell curve)
            x = np.arange(256)
            reference_hist = np.exp(-((x - 128) ** 2) / (2 * 50 ** 2))
            reference_hist = (reference_hist / reference_hist.sum() * 
                            self.processed_image.size).astype(np.uint64)
            
            result = ImageProcessor.histogram_matching(self.processed_image, reference_hist)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="Applied histogram matching (Gaussian reference)")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply histogram matching: {str(e)}")
    
    def adaptive_equalization(self):
        """Apply adaptive histogram equalization (CLAHE)"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            result = ImageProcessor.adaptive_histogram_equalization(self.processed_image)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="Applied adaptive histogram equalization (CLAHE)")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply adaptive equalization: {str(e)}")
    
    # Bài 7 methods
    def average_filter(self, kernel_size):
        """Apply average filter"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            result = ImageProcessor.average_filter(self.processed_image, kernel_size)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text=f"Applied average filter {kernel_size}x{kernel_size}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply average filter: {str(e)}")
    
    def median_filter(self, kernel_size):
        """Apply median filter"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            result = ImageProcessor.median_filter(self.processed_image, kernel_size)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text=f"Applied median filter {kernel_size}x{kernel_size}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply median filter: {str(e)}")
    
    # Bài 8 methods
    def sobel_edge(self):
        """Apply Sobel edge detection"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            magnitude, _, _ = ImageProcessor.sobel_edge_detection(self.processed_image)
            self.processed_image = magnitude
            self.display_image(magnitude)
            self.status_label.config(text="Applied Sobel edge detection")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply Sobel: {str(e)}")
    
    def prewitt_edge(self):
        """Apply Prewitt edge detection"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            magnitude, _, _ = ImageProcessor.prewitt_edge_detection(self.processed_image)
            self.processed_image = magnitude
            self.display_image(magnitude)
            self.status_label.config(text="Applied Prewitt edge detection")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply Prewitt: {str(e)}")
    
    def roberts_edge(self):
        """Apply Roberts edge detection"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            magnitude, _, _ = ImageProcessor.roberts_edge_detection(self.processed_image)
            self.processed_image = magnitude
            self.display_image(magnitude)
            self.status_label.config(text="Applied Roberts edge detection")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply Roberts: {str(e)}")
    
    def kirsch_edge(self):
        """Apply Kirsch edge detection"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            magnitude = ImageProcessor.kirsch_edge_detection(self.processed_image)
            self.processed_image = magnitude
            self.display_image(magnitude)
            self.status_label.config(text="Applied Kirsch edge detection")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply Kirsch: {str(e)}")
    
    # Bài 9 methods
    def laplacian_edge(self, neighbors):
        """Apply Laplacian edge detection"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            if neighbors == 4:
                result = ImageProcessor.laplacian_4_neighbor(self.processed_image)
                msg = "Applied Laplacian 4-neighbor"
            else:
                result = ImageProcessor.laplacian_8_neighbor(self.processed_image)
                msg = "Applied Laplacian 8-neighbor"
            
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text=msg)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply Laplacian: {str(e)}")
    
    def log_edge(self):
        """Apply Laplacian of Gaussian edge detection"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            result = ImageProcessor.laplacian_of_gaussian(self.processed_image)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text="Applied Laplacian of Gaussian (LoG)")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply LoG: {str(e)}")
    
    def sharpen(self, method):
        """Apply image sharpening"""
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            result = ImageProcessor.sharpen_image(self.processed_image, method)
            self.processed_image = result
            self.display_image(result)
            self.status_label.config(text=f"Applied sharpening ({method})")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to sharpen image: {str(e)}")


def main():
    """Main entry point"""
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
