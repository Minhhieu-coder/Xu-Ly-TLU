"""
Image Processing Core Functions
Implements various image processing techniques including:
- Contrast stretching (Bài 4)
- Histogram equalization (Bài 5)
- Histogram matching and adaptive equalization (Bài 6)
- Convolution and noise removal (Bài 7)
- Edge detection (Bài 8)
- Laplacian edge detection and sharpening (Bài 9)
"""

import numpy as np
import cv2
from scipy import ndimage
from typing import Tuple, Optional


class ImageProcessor:
    """Core image processing operations"""
    
    @staticmethod
    def contrast_stretching(image: np.ndarray, r_min: Optional[int] = None, 
                          r_max: Optional[int] = None) -> np.ndarray:
        """
        Bài 4: Linear contrast stretching
        Formula: s = (r - r_min) / (r_max - r_min) * 255
        
        Args:
            image: Input grayscale image
            r_min: Minimum intensity (auto-detect if None)
            r_max: Maximum intensity (auto-detect if None)
            
        Returns:
            Stretched image with values in [0, 255]
        """
        if r_min is None:
            r_min = np.min(image)
        if r_max is None:
            r_max = np.max(image)
            
        if r_max == r_min:
            return image
            
        # Apply linear transformation
        stretched = ((image - r_min) / (r_max - r_min) * 255).astype(np.uint8)
        return stretched
    
    @staticmethod
    def contrast_clipping_type1(image: np.ndarray, low_threshold: int, 
                               high_threshold: int) -> np.ndarray:
        """
        Bài 4: Type 1 intensity clipping with adjustable thresholds
        
        Args:
            image: Input grayscale image
            low_threshold: Lower bound for clipping
            high_threshold: Upper bound for clipping
            
        Returns:
            Clipped and stretched image
        """
        clipped = np.clip(image, low_threshold, high_threshold)
        return ImageProcessor.contrast_stretching(clipped, low_threshold, high_threshold)
    
    @staticmethod
    def contrast_clipping_type2(image: np.ndarray, 
                               dark_threshold: int = 85,
                               mid_threshold: int = 170) -> np.ndarray:
        """
        Bài 4: Type 2 region-based intensity clipping
        Processes different intensity regions separately
        
        Args:
            image: Input grayscale image
            dark_threshold: Threshold separating dark region
            mid_threshold: Threshold separating mid region
            
        Returns:
            Processed image with enhanced regions
        """
        result = np.zeros_like(image)
        
        # Dark region [0, dark_threshold]
        dark_mask = image <= dark_threshold
        if np.any(dark_mask):
            dark_region = image[dark_mask]
            dark_min, dark_max = np.min(dark_region), np.max(dark_region)
            if dark_max > dark_min:
                result[dark_mask] = ((dark_region - dark_min) / 
                                    (dark_max - dark_min) * 85).astype(np.uint8)
        
        # Mid region (dark_threshold, mid_threshold]
        mid_mask = (image > dark_threshold) & (image <= mid_threshold)
        if np.any(mid_mask):
            mid_region = image[mid_mask]
            mid_min, mid_max = np.min(mid_region), np.max(mid_region)
            if mid_max > mid_min:
                result[mid_mask] = (85 + (mid_region - mid_min) / 
                                   (mid_max - mid_min) * 85).astype(np.uint8)
        
        # Bright region (mid_threshold, 255]
        bright_mask = image > mid_threshold
        if np.any(bright_mask):
            bright_region = image[bright_mask]
            bright_min, bright_max = np.min(bright_region), np.max(bright_region)
            if bright_max > bright_min:
                result[bright_mask] = (170 + (bright_region - bright_min) / 
                                      (bright_max - bright_min) * 85).astype(np.uint8)
        
        return result
    
    @staticmethod
    def calculate_histogram(image: np.ndarray) -> np.ndarray:
        """
        Bài 5: Calculate histogram of grayscale image
        
        Args:
            image: Input grayscale image
            
        Returns:
            Histogram array of size 256
        """
        hist, _ = np.histogram(image.flatten(), bins=256, range=[0, 256])
        return hist
    
    @staticmethod
    def histogram_equalization(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Bài 5: Standard histogram equalization
        
        Args:
            image: Input grayscale image
            
        Returns:
            Tuple of (equalized image, histogram of original)
        """
        # Calculate histogram
        hist = ImageProcessor.calculate_histogram(image)
        
        # Check if image has uniform intensity (only one unique value)
        if image.max() == image.min():
            return image.copy(), hist
        
        # Calculate CDF (Cumulative Distribution Function)
        cdf = hist.cumsum()
        
        # Mask out zero values in CDF
        cdf_masked = np.ma.masked_equal(cdf, 0)
        
        # Normalize CDF to [0, 255]
        cdf_normalized = (cdf_masked - cdf_masked.min()) * 255 / (cdf_masked.max() - cdf_masked.min())
        cdf_normalized = np.ma.filled(cdf_normalized, 0).astype(np.uint8)
        
        # Map the pixel values using CDF
        equalized = cdf_normalized[image.flatten()]
        equalized = equalized.reshape(image.shape)
        
        return equalized, hist
    
    @staticmethod
    def histogram_matching(image: np.ndarray, 
                          reference_hist: np.ndarray) -> np.ndarray:
        """
        Bài 6: Histogram matching (specification)
        Transform image to match reference histogram
        
        Args:
            image: Input grayscale image
            reference_hist: Reference histogram to match
            
        Returns:
            Matched image
        """
        # Equalize source image
        source_equalized, _ = ImageProcessor.histogram_equalization(image)
        
        # Calculate CDF of reference histogram
        ref_cdf = reference_hist.cumsum()
        ref_cdf_normalized = (ref_cdf - ref_cdf.min()) * 255 / (ref_cdf.max() - ref_cdf.min())
        
        # Create lookup table for inverse mapping
        lookup_table = np.zeros(256, dtype=np.uint8)
        g_values = np.arange(256)
        
        for s in range(256):
            # Find the closest reference CDF value
            j = np.argmin(np.abs(ref_cdf_normalized - s))
            lookup_table[s] = j
        
        # Apply lookup table
        matched = lookup_table[source_equalized.flatten()]
        matched = matched.reshape(image.shape)
        
        return matched
    
    @staticmethod
    def adaptive_histogram_equalization(image: np.ndarray, 
                                       clip_limit: float = 2.0,
                                       tile_grid_size: Tuple[int, int] = (8, 8)) -> np.ndarray:
        """
        Bài 6: Adaptive/Local histogram equalization (CLAHE)
        
        Args:
            image: Input grayscale image
            clip_limit: Threshold for contrast limiting
            tile_grid_size: Size of grid for local equalization
            
        Returns:
            Adaptively equalized image
        """
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
        return clahe.apply(image)
    
    @staticmethod
    def convolution2d(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
        """
        Bài 7: Custom 2D convolution implementation
        
        Args:
            image: Input image
            kernel: Convolution kernel/mask
            
        Returns:
            Convolved image
        """
        # Pad the image
        kernel_size = kernel.shape[0]
        pad_size = kernel_size // 2
        padded = np.pad(image, pad_size, mode='edge')
        
        # Perform convolution
        result = np.zeros_like(image, dtype=np.float64)
        
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                region = padded[i:i+kernel_size, j:j+kernel_size]
                result[i, j] = np.sum(region * kernel)
        
        # Clip and convert to uint8
        result = np.clip(result, 0, 255).astype(np.uint8)
        return result
    
    @staticmethod
    def average_filter(image: np.ndarray, kernel_size: int = 3) -> np.ndarray:
        """
        Bài 7: Average filter for noise removal
        
        Args:
            image: Input noisy image
            kernel_size: Size of averaging kernel (3 or 5)
            
        Returns:
            Filtered image
        """
        kernel = np.ones((kernel_size, kernel_size), dtype=np.float64) / (kernel_size ** 2)
        return ImageProcessor.convolution2d(image, kernel)
    
    @staticmethod
    def median_filter(image: np.ndarray, kernel_size: int = 3) -> np.ndarray:
        """
        Bài 7: Median filter for salt-pepper noise removal
        
        Args:
            image: Input noisy image
            kernel_size: Size of median filter window (3 or 5)
            
        Returns:
            Filtered image
        """
        return cv2.medianBlur(image, kernel_size)
    
    @staticmethod
    def add_salt_pepper_noise(image: np.ndarray, salt_prob: float = 0.02,
                             pepper_prob: float = 0.02) -> np.ndarray:
        """
        Add salt and pepper noise to image for testing
        
        Args:
            image: Input image
            salt_prob: Probability of salt noise
            pepper_prob: Probability of pepper noise
            
        Returns:
            Noisy image
        """
        noisy = image.copy()
        
        # Salt noise (white pixels)
        salt_mask = np.random.random(image.shape) < salt_prob
        noisy[salt_mask] = 255
        
        # Pepper noise (black pixels)
        pepper_mask = np.random.random(image.shape) < pepper_prob
        noisy[pepper_mask] = 0
        
        return noisy
    
    @staticmethod
    def sobel_edge_detection(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Bài 8: Sobel edge detection operator
        
        Args:
            image: Input grayscale image
            
        Returns:
            Tuple of (gradient magnitude, Gx, Gy)
        """
        # Sobel kernels
        sobel_x = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]], dtype=np.float64)
        
        sobel_y = np.array([[-1, -2, -1],
                           [0, 0, 0],
                           [1, 2, 1]], dtype=np.float64)
        
        # Compute gradients
        Gx = ndimage.convolve(image.astype(np.float64), sobel_x)
        Gy = ndimage.convolve(image.astype(np.float64), sobel_y)
        
        # Compute gradient magnitude
        magnitude = np.sqrt(Gx**2 + Gy**2)
        magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)
        
        return magnitude, Gx, Gy
    
    @staticmethod
    def prewitt_edge_detection(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Bài 8: Prewitt edge detection operator
        
        Args:
            image: Input grayscale image
            
        Returns:
            Tuple of (gradient magnitude, Gx, Gy)
        """
        # Prewitt kernels
        prewitt_x = np.array([[-1, 0, 1],
                             [-1, 0, 1],
                             [-1, 0, 1]], dtype=np.float64)
        
        prewitt_y = np.array([[-1, -1, -1],
                             [0, 0, 0],
                             [1, 1, 1]], dtype=np.float64)
        
        # Compute gradients
        Gx = ndimage.convolve(image.astype(np.float64), prewitt_x)
        Gy = ndimage.convolve(image.astype(np.float64), prewitt_y)
        
        # Compute gradient magnitude
        magnitude = np.sqrt(Gx**2 + Gy**2)
        magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)
        
        return magnitude, Gx, Gy
    
    @staticmethod
    def roberts_edge_detection(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Bài 8: Roberts edge detection operator
        
        Args:
            image: Input grayscale image
            
        Returns:
            Tuple of (gradient magnitude, Gx, Gy)
        """
        # Roberts kernels
        roberts_x = np.array([[1, 0],
                             [0, -1]], dtype=np.float64)
        
        roberts_y = np.array([[0, 1],
                             [-1, 0]], dtype=np.float64)
        
        # Compute gradients
        Gx = ndimage.convolve(image.astype(np.float64), roberts_x)
        Gy = ndimage.convolve(image.astype(np.float64), roberts_y)
        
        # Compute gradient magnitude
        magnitude = np.sqrt(Gx**2 + Gy**2)
        magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)
        
        return magnitude, Gx, Gy
    
    @staticmethod
    def kirsch_edge_detection(image: np.ndarray) -> np.ndarray:
        """
        Bài 8: Kirsch edge detection operator (8 directional kernels)
        
        Args:
            image: Input grayscale image
            
        Returns:
            Edge magnitude image
        """
        # 8 Kirsch kernels for different directions
        kirsch_kernels = [
            np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]]),  # North
            np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]]),  # Northeast
            np.array([[5, -3, -3], [5, 0, -3], [5, -3, -3]]),  # East
            np.array([[-3, -3, -3], [5, 0, -3], [5, 5, -3]]),  # Southeast
            np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]]),  # South
            np.array([[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]]),  # Southwest
            np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]]),  # West
            np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]])   # Northwest
        ]
        
        # Apply all kernels and take maximum response
        responses = []
        for kernel in kirsch_kernels:
            response = np.abs(ndimage.convolve(image.astype(np.float64), kernel))
            responses.append(response)
        
        # Maximum response across all directions
        magnitude = np.max(responses, axis=0)
        magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)
        
        return magnitude
    
    @staticmethod
    def laplacian_4_neighbor(image: np.ndarray) -> np.ndarray:
        """
        Bài 9: Laplacian edge detection with 4-neighbor kernel
        
        Args:
            image: Input grayscale image
            
        Returns:
            Laplacian filtered image
        """
        # 4-neighbor Laplacian kernel
        kernel = np.array([[0, 1, 0],
                          [1, -4, 1],
                          [0, 1, 0]], dtype=np.float64)
        
        result = ndimage.convolve(image.astype(np.float64), kernel)
        result = np.clip(np.abs(result), 0, 255).astype(np.uint8)
        
        return result
    
    @staticmethod
    def laplacian_8_neighbor(image: np.ndarray) -> np.ndarray:
        """
        Bài 9: Laplacian edge detection with 8-neighbor kernel
        
        Args:
            image: Input grayscale image
            
        Returns:
            Laplacian filtered image
        """
        # 8-neighbor Laplacian kernel
        kernel = np.array([[1, 1, 1],
                          [1, -8, 1],
                          [1, 1, 1]], dtype=np.float64)
        
        result = ndimage.convolve(image.astype(np.float64), kernel)
        result = np.clip(np.abs(result), 0, 255).astype(np.uint8)
        
        return result
    
    @staticmethod
    def laplacian_of_gaussian(image: np.ndarray, sigma: float = 1.4) -> np.ndarray:
        """
        Bài 9: Laplacian of Gaussian (LoG) edge detection
        Applies Gaussian smoothing before Laplacian
        
        Args:
            image: Input grayscale image
            sigma: Standard deviation for Gaussian kernel
            
        Returns:
            LoG filtered image
        """
        # Apply Gaussian smoothing
        smoothed = cv2.GaussianBlur(image, (5, 5), sigma)
        
        # Apply Laplacian
        laplacian = ImageProcessor.laplacian_8_neighbor(smoothed)
        
        return laplacian
    
    @staticmethod
    def sharpen_image(image: np.ndarray, method: str = 'laplacian') -> np.ndarray:
        """
        Bài 9: Image sharpening by adding Laplacian to original
        
        Args:
            image: Input grayscale image
            method: Sharpening method ('laplacian', 'log')
            
        Returns:
            Sharpened image
        """
        if method == 'laplacian':
            # Use 8-neighbor Laplacian
            kernel = np.array([[1, 1, 1],
                              [1, -8, 1],
                              [1, 1, 1]], dtype=np.float64)
            laplacian = ndimage.convolve(image.astype(np.float64), kernel)
            
        elif method == 'log':
            # Use Laplacian of Gaussian
            smoothed = cv2.GaussianBlur(image, (5, 5), 1.4)
            kernel = np.array([[1, 1, 1],
                              [1, -8, 1],
                              [1, 1, 1]], dtype=np.float64)
            laplacian = ndimage.convolve(smoothed.astype(np.float64), kernel)
        else:
            raise ValueError(f"Unknown sharpening method: {method}")
        
        # Add Laplacian to original (subtract because kernel is negative)
        sharpened = image.astype(np.float64) - laplacian
        sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)
        
        return sharpened
    
    @staticmethod
    def fourier_transform(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Bài 10: Forward Fourier Transform (DFT)
        
        Args:
            image: Input grayscale image
            
        Returns:
            Tuple of (magnitude spectrum, phase spectrum)
        """
        # Apply FFT (faster than DFT)
        f_transform = np.fft.fft2(image)
        f_shift = np.fft.fftshift(f_transform)  # Shift zero frequency to center
        
        # Calculate magnitude and phase
        magnitude = np.abs(f_shift)
        phase = np.angle(f_shift)
        
        return magnitude, phase
    
    @staticmethod
    def inverse_fourier_transform(magnitude: np.ndarray, 
                                  phase: np.ndarray) -> np.ndarray:
        """
        Bài 10: Inverse Fourier Transform (IDFT)
        
        Args:
            magnitude: Magnitude spectrum
            phase: Phase spectrum
            
        Returns:
            Reconstructed image
        """
        # Reconstruct complex spectrum
        f_shift = magnitude * np.exp(1j * phase)
        
        # Inverse shift
        f_transform = np.fft.ifftshift(f_shift)
        
        # Apply inverse FFT
        image_reconstructed = np.fft.ifft2(f_transform)
        image_reconstructed = np.abs(image_reconstructed)
        
        # Clip and convert
        image_reconstructed = np.clip(image_reconstructed, 0, 255).astype(np.uint8)
        
        return image_reconstructed
    
    @staticmethod
    def get_magnitude_spectrum_display(magnitude: np.ndarray) -> np.ndarray:
        """
        Convert magnitude spectrum for display (log scale)
        
        Args:
            magnitude: Magnitude spectrum
            
        Returns:
            Display-ready magnitude spectrum
        """
        # Use log scale for better visualization
        magnitude_display = np.log1p(magnitude)
        
        # Normalize to [0, 255]
        min_val = magnitude_display.min()
        max_val = magnitude_display.max()
        
        if max_val > min_val:
            magnitude_display = (magnitude_display - min_val) / (max_val - min_val) * 255
        else:
            # Handle uniform images
            magnitude_display = np.zeros_like(magnitude_display)
        
        magnitude_display = magnitude_display.astype(np.uint8)
        
        return magnitude_display
    
    @staticmethod
    def ideal_lowpass_filter(image: np.ndarray, cutoff_frequency: int) -> np.ndarray:
        """
        Bài 10-11: Ideal Low-pass Filter in frequency domain
        
        Args:
            image: Input grayscale image
            cutoff_frequency: Cutoff frequency (radius)
            
        Returns:
            Filtered image
        """
        # Get image dimensions
        rows, cols = image.shape
        crow, ccol = rows // 2, cols // 2
        
        # Create ideal low-pass filter mask
        mask = np.zeros((rows, cols), dtype=np.float64)
        y, x = np.ogrid[:rows, :cols]
        distance = np.sqrt((x - ccol)**2 + (y - crow)**2)
        mask[distance <= cutoff_frequency] = 1
        
        # Apply Fourier transform
        f_transform = np.fft.fft2(image)
        f_shift = np.fft.fftshift(f_transform)
        
        # Apply filter in frequency domain
        f_filtered = f_shift * mask
        
        # Inverse Fourier transform
        f_ishift = np.fft.ifftshift(f_filtered)
        image_filtered = np.fft.ifft2(f_ishift)
        image_filtered = np.abs(image_filtered)
        
        # Clip and convert
        image_filtered = np.clip(image_filtered, 0, 255).astype(np.uint8)
        
        return image_filtered
    
    @staticmethod
    def gaussian_lowpass_filter(image: np.ndarray, sigma: float = 30.0) -> np.ndarray:
        """
        Bài 11: Gaussian Low-pass Filter in frequency domain
        
        Args:
            image: Input grayscale image
            sigma: Standard deviation for Gaussian filter
            
        Returns:
            Filtered image
        """
        # Get image dimensions
        rows, cols = image.shape
        crow, ccol = rows // 2, cols // 2
        
        # Create Gaussian low-pass filter mask
        y, x = np.ogrid[:rows, :cols]
        distance_sq = (x - ccol)**2 + (y - crow)**2
        mask = np.exp(-distance_sq / (2 * sigma**2))
        
        # Apply Fourier transform
        f_transform = np.fft.fft2(image)
        f_shift = np.fft.fftshift(f_transform)
        
        # Apply filter in frequency domain
        f_filtered = f_shift * mask
        
        # Inverse Fourier transform
        f_ishift = np.fft.ifftshift(f_filtered)
        image_filtered = np.fft.ifft2(f_ishift)
        image_filtered = np.abs(image_filtered)
        
        # Clip and convert
        image_filtered = np.clip(image_filtered, 0, 255).astype(np.uint8)
        
        return image_filtered
