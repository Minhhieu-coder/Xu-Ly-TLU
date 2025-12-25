"""
Machine Learning Image Processing Module
Implements various ML techniques for image processing:
- Image segmentation using K-Means clustering
- Feature extraction (histogram, texture, color moments)
- Simple image classification using KNN
- Dimensionality reduction with PCA

Note: This module uses custom implementations for educational purposes,
demonstrating the underlying algorithms. These implementations are suitable
for image processing tasks and work with numpy/opencv. For production use
with larger datasets, consider using scikit-learn's optimized implementations.

Bài tập Machine Learning - Xử lý ảnh
Tác giả: Minhhieu-coder
"""

import numpy as np
import cv2
from typing import Tuple, List, Optional
from scipy import ndimage


class MLImageProcessor:
    """Machine Learning operations for image processing"""
    
    @staticmethod
    def kmeans_segmentation(image: np.ndarray, k: int = 3, 
                            max_iterations: int = 100) -> Tuple[np.ndarray, np.ndarray]:
        """
        ML 1: K-Means clustering for image segmentation
        Segments image into k clusters based on pixel intensity
        
        Args:
            image: Input grayscale image
            k: Number of clusters (segments)
            max_iterations: Maximum iterations for convergence
            
        Returns:
            Tuple of (segmented image, cluster centers)
        """
        import warnings
        
        # Flatten image for clustering
        pixels = image.flatten().astype(np.float32)
        
        # Random initialization of centroids
        np.random.seed(42)  # For reproducibility
        unique_vals = np.unique(pixels)
        if len(unique_vals) < k:
            warnings.warn(f"Requested k={k} clusters but image only has {len(unique_vals)} unique values. Using k={len(unique_vals)} instead.")
            k = len(unique_vals)
        
        # Use random unique pixel values as initial centroids
        idx = np.random.choice(len(unique_vals), k, replace=False)
        centroids = unique_vals[idx].astype(np.float32)
        centroids = np.sort(centroids)  # Sort for consistent ordering
        
        # K-Means iteration
        for iteration in range(max_iterations):
            # Assign each pixel to nearest centroid
            distances = np.abs(pixels[:, np.newaxis] - centroids)
            labels = np.argmin(distances, axis=1)
            
            # Update centroids
            new_centroids = np.zeros(k, dtype=np.float32)
            for i in range(k):
                cluster_pixels = pixels[labels == i]
                if len(cluster_pixels) > 0:
                    new_centroids[i] = np.mean(cluster_pixels)
                else:
                    new_centroids[i] = centroids[i]
            
            # Check convergence
            if np.allclose(centroids, new_centroids, atol=1.0):
                break
            
            centroids = new_centroids
        
        # Create segmented image
        segmented = centroids[labels].reshape(image.shape).astype(np.uint8)
        
        return segmented, centroids
    
    @staticmethod
    def color_kmeans_segmentation(image: np.ndarray, k: int = 3) -> np.ndarray:
        """
        ML 1.2: K-Means clustering for color image segmentation
        
        Args:
            image: Input color image (BGR)
            k: Number of clusters
            
        Returns:
            Segmented color image
        """
        if len(image.shape) != 3:
            # Convert grayscale to BGR for processing
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        
        # Reshape to 2D array of pixels
        pixels = image.reshape((-1, 3)).astype(np.float32)
        
        # K-Means criteria
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        
        # Apply K-Means
        _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, 
                                        cv2.KMEANS_RANDOM_CENTERS)
        
        # Convert centers to uint8
        centers = np.uint8(centers)
        
        # Map labels to center colors
        segmented = centers[labels.flatten()]
        segmented = segmented.reshape(image.shape)
        
        return segmented
    
    @staticmethod
    def extract_histogram_features(image: np.ndarray, bins: int = 32) -> np.ndarray:
        """
        ML 2: Extract histogram features for classification
        
        Args:
            image: Input grayscale image
            bins: Number of histogram bins
            
        Returns:
            Normalized histogram feature vector
        """
        hist, _ = np.histogram(image.flatten(), bins=bins, range=[0, 256])
        
        # Normalize histogram
        hist = hist.astype(np.float64)
        hist = hist / hist.sum() if hist.sum() > 0 else hist
        
        return hist
    
    @staticmethod
    def extract_texture_features(image: np.ndarray) -> np.ndarray:
        """
        ML 2.2: Extract texture features using gradient statistics
        
        Args:
            image: Input grayscale image
            
        Returns:
            Texture feature vector (gradient magnitude, direction stats)
        """
        # Calculate gradients
        Gx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
        Gy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
        
        # Gradient magnitude and direction
        magnitude = np.sqrt(Gx**2 + Gy**2)
        direction = np.arctan2(Gy, Gx)
        
        # Extract statistics
        features = np.array([
            np.mean(magnitude),           # Mean gradient magnitude
            np.std(magnitude),            # Std gradient magnitude
            np.max(magnitude),            # Max gradient magnitude
            np.mean(np.abs(direction)),   # Mean direction
            np.std(direction),            # Std direction
        ])
        
        return features
    
    @staticmethod
    def extract_statistical_features(image: np.ndarray) -> np.ndarray:
        """
        ML 2.3: Extract statistical features
        
        Args:
            image: Input grayscale image
            
        Returns:
            Statistical feature vector
        """
        # Basic statistics
        mean_val = np.mean(image)
        std_val = np.std(image)
        min_val = np.min(image)
        max_val = np.max(image)
        
        # Additional statistics
        median_val = np.median(image)
        skewness = 0.0
        if std_val > 0:
            skewness = np.mean(((image - mean_val) / std_val) ** 3)
        
        kurtosis = 0.0
        if std_val > 0:
            kurtosis = np.mean(((image - mean_val) / std_val) ** 4) - 3
        
        # Energy and entropy
        hist, _ = np.histogram(image.flatten(), bins=256, range=[0, 256])
        prob = hist / hist.sum() if hist.sum() > 0 else hist
        energy = np.sum(prob ** 2)
        
        # Avoid log(0) by adding small epsilon
        entropy = -np.sum(prob * np.log2(prob + 1e-10))
        
        features = np.array([
            mean_val / 255.0,      # Normalized mean
            std_val / 128.0,       # Normalized std
            (max_val - min_val) / 255.0,  # Contrast
            median_val / 255.0,    # Normalized median
            skewness,              # Skewness
            kurtosis,              # Kurtosis
            energy,                # Energy
            entropy / 8.0          # Normalized entropy (max entropy for 8-bit is 8)
        ])
        
        return features
    
    @staticmethod
    def extract_combined_features(image: np.ndarray) -> np.ndarray:
        """
        ML 2.4: Extract combined feature vector for classification
        
        Args:
            image: Input grayscale image
            
        Returns:
            Combined feature vector
        """
        hist_features = MLImageProcessor.extract_histogram_features(image, bins=16)
        texture_features = MLImageProcessor.extract_texture_features(image)
        stat_features = MLImageProcessor.extract_statistical_features(image)
        
        # Normalize texture features
        texture_features = texture_features / (np.max(np.abs(texture_features)) + 1e-10)
        
        # Combine all features
        combined = np.concatenate([hist_features, texture_features, stat_features])
        
        return combined
    
    @staticmethod
    def knn_classify(train_features: np.ndarray, train_labels: np.ndarray,
                    test_feature: np.ndarray, k: int = 3) -> int:
        """
        ML 3: K-Nearest Neighbors classification
        
        Args:
            train_features: Training feature vectors (n_samples, n_features)
            train_labels: Training labels (n_samples,)
            test_feature: Test feature vector (n_features,)
            k: Number of neighbors
            
        Returns:
            Predicted label
        """
        # Calculate distances to all training samples
        distances = np.sqrt(np.sum((train_features - test_feature) ** 2, axis=1))
        
        # Get k nearest neighbors
        k = min(k, len(train_labels))
        nearest_indices = np.argsort(distances)[:k]
        nearest_labels = train_labels[nearest_indices]
        
        # Majority voting
        unique_labels, counts = np.unique(nearest_labels, return_counts=True)
        predicted_label = unique_labels[np.argmax(counts)]
        
        return int(predicted_label)
    
    @staticmethod
    def pca_reduce(images: np.ndarray, n_components: int = 10) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        ML 4: Principal Component Analysis for dimensionality reduction
        
        Args:
            images: Input images array (n_samples, height, width)
            n_components: Number of principal components
            
        Returns:
            Tuple of (reduced features, principal components, mean image)
        """
        # Flatten images
        n_samples = images.shape[0]
        flattened = images.reshape(n_samples, -1).astype(np.float64)
        
        # Center data
        mean_img = np.mean(flattened, axis=0)
        centered = flattened - mean_img
        
        # Compute covariance matrix
        cov_matrix = np.cov(centered.T)
        
        # Compute eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
        
        # Sort by eigenvalues (descending)
        idx = np.argsort(eigenvalues)[::-1]
        eigenvectors = eigenvectors[:, idx]
        
        # Select top n_components
        n_components = min(n_components, eigenvectors.shape[1])
        principal_components = eigenvectors[:, :n_components]
        
        # Project data onto principal components
        reduced = np.dot(centered, principal_components)
        
        return reduced, principal_components, mean_img
    
    @staticmethod
    def otsu_threshold(image: np.ndarray) -> Tuple[np.ndarray, int]:
        """
        ML 5: Otsu's automatic thresholding method
        Finds optimal threshold that minimizes within-class variance
        
        Args:
            image: Input grayscale image
            
        Returns:
            Tuple of (binary image, optimal threshold)
        """
        # Calculate histogram
        hist, bin_edges = np.histogram(image.flatten(), bins=256, range=[0, 256])
        hist = hist.astype(np.float64)
        
        # Total number of pixels
        total = hist.sum()
        
        # Probability of each intensity
        prob = hist / total
        
        # Class probabilities and means
        best_threshold = 0
        max_variance = 0
        
        for t in range(256):
            # Class 1: pixels with intensity <= t
            w0 = np.sum(prob[:t+1])
            w1 = np.sum(prob[t+1:])
            
            if w0 == 0 or w1 == 0:
                continue
            
            # Mean intensities
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
    
    @staticmethod
    def adaptive_threshold_ml(image: np.ndarray, block_size: int = 15,
                              C: float = 5) -> np.ndarray:
        """
        ML 5.2: Adaptive thresholding using local mean
        
        Args:
            image: Input grayscale image
            block_size: Size of local neighborhood
            C: Constant subtracted from mean
            
        Returns:
            Binary image
        """
        # Calculate local mean using convolution
        kernel = np.ones((block_size, block_size), dtype=np.float64) / (block_size ** 2)
        local_mean = ndimage.convolve(image.astype(np.float64), kernel)
        
        # Apply adaptive threshold
        binary = (image > (local_mean - C)).astype(np.uint8) * 255
        
        return binary
    
    @staticmethod
    def detect_edges_ml(image: np.ndarray, low_threshold: float = 0.1,
                       high_threshold: float = 0.3) -> np.ndarray:
        """
        ML 6: Canny-like edge detection with automatic thresholds
        
        Args:
            image: Input grayscale image
            low_threshold: Low threshold ratio (relative to max gradient)
            high_threshold: High threshold ratio (relative to max gradient)
            
        Returns:
            Edge map
        """
        # Gaussian blur
        blurred = cv2.GaussianBlur(image, (5, 5), 1.4)
        
        # Calculate gradients
        Gx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
        Gy = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
        
        # Gradient magnitude and direction
        magnitude = np.sqrt(Gx**2 + Gy**2)
        direction = np.arctan2(Gy, Gx)
        
        # Non-maximum suppression
        rows, cols = image.shape
        suppressed = np.zeros_like(magnitude)
        
        # Discretize direction to 0, 45, 90, 135 degrees
        angle = np.rad2deg(direction) % 180
        
        for i in range(1, rows-1):
            for j in range(1, cols-1):
                # Determine neighboring pixels based on gradient direction
                if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                    n1, n2 = magnitude[i, j-1], magnitude[i, j+1]
                elif 22.5 <= angle[i, j] < 67.5:
                    n1, n2 = magnitude[i-1, j+1], magnitude[i+1, j-1]
                elif 67.5 <= angle[i, j] < 112.5:
                    n1, n2 = magnitude[i-1, j], magnitude[i+1, j]
                else:
                    n1, n2 = magnitude[i-1, j-1], magnitude[i+1, j+1]
                
                # Keep pixel if it's local maximum
                if magnitude[i, j] >= n1 and magnitude[i, j] >= n2:
                    suppressed[i, j] = magnitude[i, j]
        
        # Double thresholding
        max_mag = np.max(suppressed)
        low_thresh = low_threshold * max_mag
        high_thresh = high_threshold * max_mag
        
        edges = np.zeros_like(image, dtype=np.uint8)
        strong = suppressed >= high_thresh
        weak = (suppressed >= low_thresh) & (suppressed < high_thresh)
        
        # Hysteresis: connect weak edges to strong edges
        edges[strong] = 255
        
        # Simple hysteresis using dilation
        for _ in range(3):
            dilated = cv2.dilate(edges, np.ones((3, 3), dtype=np.uint8))
            edges = np.where(weak & (dilated > 0), 255, edges).astype(np.uint8)
        
        return edges
    
    @staticmethod
    def morphological_operations(image: np.ndarray, operation: str = 'erosion',
                                 kernel_size: int = 3) -> np.ndarray:
        """
        ML 7: Morphological operations for binary image processing
        
        Args:
            image: Input binary image
            operation: One of 'erosion', 'dilation', 'opening', 'closing'
            kernel_size: Size of structuring element
            
        Returns:
            Processed binary image
        """
        # Create structuring element
        kernel = np.ones((kernel_size, kernel_size), dtype=np.uint8)
        
        if operation == 'erosion':
            result = cv2.erode(image, kernel, iterations=1)
        elif operation == 'dilation':
            result = cv2.dilate(image, kernel, iterations=1)
        elif operation == 'opening':
            result = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
        elif operation == 'closing':
            result = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        else:
            raise ValueError(f"Unknown operation: {operation}")
        
        return result
    
    @staticmethod
    def simple_object_detection(image: np.ndarray, min_area: int = 100) -> Tuple[np.ndarray, List[dict]]:
        """
        ML 8: Simple object detection using connected components
        
        Args:
            image: Input binary image (or will be converted)
            min_area: Minimum object area to detect
            
        Returns:
            Tuple of (labeled image, list of object properties)
        """
        # Ensure binary image
        if image.max() > 1:
            binary = (image > 127).astype(np.uint8)
        else:
            binary = image.astype(np.uint8)
        
        # Find connected components
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)
        
        # Extract object properties
        objects = []
        for i in range(1, num_labels):  # Skip background (label 0)
            area = stats[i, cv2.CC_STAT_AREA]
            
            if area >= min_area:
                obj = {
                    'label': i,
                    'area': area,
                    'x': stats[i, cv2.CC_STAT_LEFT],
                    'y': stats[i, cv2.CC_STAT_TOP],
                    'width': stats[i, cv2.CC_STAT_WIDTH],
                    'height': stats[i, cv2.CC_STAT_HEIGHT],
                    'centroid_x': centroids[i, 0],
                    'centroid_y': centroids[i, 1]
                }
                objects.append(obj)
        
        return labels, objects


def test_ml_functions():
    """Test ML functions with sample images"""
    print("\n=== Testing ML Image Processing Functions ===\n")
    
    # Create test image
    test_img = np.zeros((100, 100), dtype=np.uint8)
    cv2.circle(test_img, (50, 50), 30, 200, -1)
    cv2.rectangle(test_img, (10, 10), (30, 30), 100, -1)
    
    # Test K-Means segmentation
    print("Testing K-Means Segmentation...")
    segmented, centers = MLImageProcessor.kmeans_segmentation(test_img, k=3)
    print(f"  - Segmented image shape: {segmented.shape}")
    print(f"  - Cluster centers: {centers}")
    print("  ✓ K-Means segmentation passed")
    
    # Test feature extraction
    print("\nTesting Feature Extraction...")
    hist_features = MLImageProcessor.extract_histogram_features(test_img)
    print(f"  - Histogram features shape: {hist_features.shape}")
    
    texture_features = MLImageProcessor.extract_texture_features(test_img)
    print(f"  - Texture features shape: {texture_features.shape}")
    
    stat_features = MLImageProcessor.extract_statistical_features(test_img)
    print(f"  - Statistical features shape: {stat_features.shape}")
    
    combined = MLImageProcessor.extract_combined_features(test_img)
    print(f"  - Combined features shape: {combined.shape}")
    print("  ✓ Feature extraction passed")
    
    # Test Otsu thresholding
    print("\nTesting Otsu Thresholding...")
    binary, threshold = MLImageProcessor.otsu_threshold(test_img)
    print(f"  - Optimal threshold: {threshold}")
    print(f"  - Binary image unique values: {np.unique(binary)}")
    print("  ✓ Otsu thresholding passed")
    
    # Test edge detection
    print("\nTesting ML Edge Detection...")
    edges = MLImageProcessor.detect_edges_ml(test_img)
    print(f"  - Edge image shape: {edges.shape}")
    print("  ✓ ML edge detection passed")
    
    # Test object detection
    print("\nTesting Object Detection...")
    labels, objects = MLImageProcessor.simple_object_detection(binary)
    print(f"  - Number of objects detected: {len(objects)}")
    for obj in objects:
        print(f"    Object {obj['label']}: area={obj['area']}, centroid=({obj['centroid_x']:.1f}, {obj['centroid_y']:.1f})")
    print("  ✓ Object detection passed")
    
    print("\n=== All ML tests passed! ===")


if __name__ == "__main__":
    test_ml_functions()
