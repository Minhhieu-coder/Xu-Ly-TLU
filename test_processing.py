import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os
from image_processing import ImageProcessor


# Default noise probabilities for test images (higher than method defaults for visibility)
# Note: These are set higher than add_salt_pepper_noise defaults (0.02) to make 
# test images clearly show noise for filter comparison
DEFAULT_SALT_PROBABILITY = 0.05
DEFAULT_PEPPER_PROBABILITY = 0.05


def create_sample_images():
    """Create sample images for testing"""
    
    # Create sample_images directory if it doesn't exist
    os.makedirs('sample_images', exist_ok=True)
    
    # 1. Create a gradient image (low contrast)
    gradient = np.linspace(50, 150, 256, dtype=np.uint8).reshape(1, -1)
    gradient_img = np.repeat(gradient, 256, axis=0)
    cv2.imwrite('sample_images/gradient_low_contrast.png', gradient_img)
    print("Created: gradient_low_contrast.png")
    
    # 2. Create a checkerboard pattern
    checkerboard = np.zeros((256, 256), dtype=np.uint8)
    square_size = 32
    for i in range(0, 256, square_size):
        for j in range(0, 256, square_size):
            if (i // square_size + j // square_size) % 2 == 0:
                checkerboard[i:i+square_size, j:j+square_size] = 255
    cv2.imwrite('sample_images/checkerboard.png', checkerboard)
    print("Created: checkerboard.png")
    
    # 3. Create a circle image
    circle_img = np.zeros((256, 256), dtype=np.uint8)
    cv2.circle(circle_img, (128, 128), 80, 200, -1)
    cv2.circle(circle_img, (128, 128), 50, 100, -1)
    cv2.imwrite('sample_images/circle.png', circle_img)
    print("Created: circle.png")
    
    # 4. Create an image with rectangle
    rect_img = np.ones((256, 256), dtype=np.uint8) * 50
    cv2.rectangle(rect_img, (50, 50), (200, 200), 200, -1)
    cv2.imwrite('sample_images/rectangle.png', rect_img)
    print("Created: rectangle.png")
    
    # 5. Create a noisy image
    base_img = np.ones((256, 256), dtype=np.uint8) * 128
    cv2.circle(base_img, (128, 128), 60, 200, 2)
    noisy_img = ImageProcessor.add_salt_pepper_noise(
        base_img, DEFAULT_SALT_PROBABILITY, DEFAULT_PEPPER_PROBABILITY
    )
    cv2.imwrite('sample_images/noisy_circle.png', noisy_img)
    print("Created: noisy_circle.png")
    
    print("\nSample images created successfully in 'sample_images/' directory")


def test_image_processing():
    """Test core image processing functions"""
    
    print("\n=== Testing Image Processing Functions ===\n")
    
    # Load test image
    test_img = cv2.imread('sample_images/gradient_low_contrast.png', cv2.IMREAD_GRAYSCALE)
    if test_img is None:
        print("Error: Could not load test image. Please run create_sample_images() first.")
        return
    
    # Test Bài 4: Contrast Stretching
    print("Testing Bài 4: Contrast Stretching")
    stretched = ImageProcessor.contrast_stretching(test_img)
    print(f"  - Original range: [{test_img.min()}, {test_img.max()}]")
    print(f"  - Stretched range: [{stretched.min()}, {stretched.max()}]")
    assert stretched.min() == 0 and stretched.max() == 255, "Contrast stretching failed"
    print("  ✓ Linear stretching passed")
    
    clipped_t1 = ImageProcessor.contrast_clipping_type1(test_img, 75, 125)
    print(f"  - Type 1 clipped range: [{clipped_t1.min()}, {clipped_t1.max()}]")
    print("  ✓ Type 1 clipping passed")
    
    clipped_t2 = ImageProcessor.contrast_clipping_type2(test_img)
    print(f"  - Type 2 clipped range: [{clipped_t2.min()}, {clipped_t2.max()}]")
    print("  ✓ Type 2 clipping passed")
    
    # Test Bài 5: Histogram Equalization
    print("\nTesting Bài 5: Histogram Equalization")
    equalized, hist = ImageProcessor.histogram_equalization(test_img)
    print(f"  - Original histogram sum: {hist.sum()}")
    print(f"  - Equalized range: [{equalized.min()}, {equalized.max()}]")
    assert hist.sum() == test_img.size, "Histogram calculation failed"
    print("  ✓ Histogram equalization passed")
    
    # Test Bài 6: Adaptive Equalization
    print("\nTesting Bài 6: Adaptive Histogram Equalization")
    adaptive = ImageProcessor.adaptive_histogram_equalization(test_img)
    print(f"  - Adaptive equalized range: [{adaptive.min()}, {adaptive.max()}]")
    print("  ✓ Adaptive equalization passed")
    
    # Test Bài 7: Filters
    print("\nTesting Bài 7: Noise Removal Filters")
    noisy = ImageProcessor.add_salt_pepper_noise(test_img)
    avg_filtered = ImageProcessor.average_filter(noisy, 3)
    med_filtered = ImageProcessor.median_filter(noisy, 3)
    print(f"  - Noisy image created")
    print(f"  - Average filtered range: [{avg_filtered.min()}, {avg_filtered.max()}]")
    print(f"  - Median filtered range: [{med_filtered.min()}, {med_filtered.max()}]")
    print("  ✓ Average and median filters passed")
    
    # Test Bài 8: Edge Detection
    print("\nTesting Bài 8: Edge Detection")
    circle_img = cv2.imread('sample_images/circle.png', cv2.IMREAD_GRAYSCALE)
    
    sobel_mag, _, _ = ImageProcessor.sobel_edge_detection(circle_img)
    print(f"  - Sobel magnitude range: [{sobel_mag.min()}, {sobel_mag.max()}]")
    print("  ✓ Sobel edge detection passed")
    
    prewitt_mag, _, _ = ImageProcessor.prewitt_edge_detection(circle_img)
    print(f"  - Prewitt magnitude range: [{prewitt_mag.min()}, {prewitt_mag.max()}]")
    print("  ✓ Prewitt edge detection passed")
    
    roberts_mag, _, _ = ImageProcessor.roberts_edge_detection(circle_img)
    print(f"  - Roberts magnitude range: [{roberts_mag.min()}, {roberts_mag.max()}]")
    print("  ✓ Roberts edge detection passed")
    
    kirsch_mag = ImageProcessor.kirsch_edge_detection(circle_img)
    print(f"  - Kirsch magnitude range: [{kirsch_mag.min()}, {kirsch_mag.max()}]")
    print("  ✓ Kirsch edge detection passed")
    
    # Test Bài 9: Laplacian and Sharpening
    print("\nTesting Bài 9: Laplacian Edge Detection and Sharpening")
    
    lap4 = ImageProcessor.laplacian_4_neighbor(circle_img)
    print(f"  - Laplacian 4-neighbor range: [{lap4.min()}, {lap4.max()}]")
    print("  ✓ Laplacian 4-neighbor passed")
    
    lap8 = ImageProcessor.laplacian_8_neighbor(circle_img)
    print(f"  - Laplacian 8-neighbor range: [{lap8.min()}, {lap8.max()}]")
    print("  ✓ Laplacian 8-neighbor passed")
    
    log_edge = ImageProcessor.laplacian_of_gaussian(circle_img)
    print(f"  - LoG range: [{log_edge.min()}, {log_edge.max()}]")
    print("  ✓ Laplacian of Gaussian passed")
    
    sharpened = ImageProcessor.sharpen_image(circle_img, 'laplacian')
    print(f"  - Sharpened (Laplacian) range: [{sharpened.min()}, {sharpened.max()}]")
    print("  ✓ Sharpening (Laplacian) passed")
    
    sharpened_log = ImageProcessor.sharpen_image(circle_img, 'log')
    print(f"  - Sharpened (LoG) range: [{sharpened_log.min()}, {sharpened_log.max()}]")
    print("  ✓ Sharpening (LoG) passed")
    
    print("\n=== All tests passed successfully! ===\n")


def create_comparison_images():
    """Create comparison images showing before/after processing"""
    
    print("\n=== Creating Comparison Images ===\n")
    
    os.makedirs('sample_images/results', exist_ok=True)
    
    # 1. Contrast stretching comparison
    low_contrast = cv2.imread('sample_images/gradient_low_contrast.png', cv2.IMREAD_GRAYSCALE)
    stretched = ImageProcessor.contrast_stretching(low_contrast)
    comparison = np.hstack([low_contrast, stretched])
    cv2.imwrite('sample_images/results/contrast_stretching_comparison.png', comparison)
    print("Created: contrast_stretching_comparison.png")
    
    # 2. Histogram equalization comparison
    equalized, _ = ImageProcessor.histogram_equalization(low_contrast)
    comparison = np.hstack([low_contrast, equalized])
    cv2.imwrite('sample_images/results/histogram_equalization_comparison.png', comparison)
    print("Created: histogram_equalization_comparison.png")
    
    # 3. Noise removal comparison
    noisy = cv2.imread('sample_images/noisy_circle.png', cv2.IMREAD_GRAYSCALE)
    median_filtered = ImageProcessor.median_filter(noisy, 5)
    comparison = np.hstack([noisy, median_filtered])
    cv2.imwrite('sample_images/results/noise_removal_comparison.png', comparison)
    print("Created: noise_removal_comparison.png")
    
    # 4. Edge detection comparison
    circle = cv2.imread('sample_images/circle.png', cv2.IMREAD_GRAYSCALE)
    sobel_edge, _, _ = ImageProcessor.sobel_edge_detection(circle)
    comparison = np.hstack([circle, sobel_edge])
    cv2.imwrite('sample_images/results/edge_detection_comparison.png', comparison)
    print("Created: edge_detection_comparison.png")
    
    # 5. Sharpening comparison
    sharpened = ImageProcessor.sharpen_image(circle, 'laplacian')
    comparison = np.hstack([circle, sharpened])
    cv2.imwrite('sample_images/results/sharpening_comparison.png', comparison)
    print("Created: sharpening_comparison.png")
    
    print("\nComparison images created successfully in 'sample_images/results/' directory")


if __name__ == "__main__":
    print("Image Processing Test Suite")
    print("=" * 50)
    
    # Create sample images
    create_sample_images()
    
    # Test all functions
    test_image_processing()
    
    # Create comparison images
    create_comparison_images()
    
    print("\nAll operations completed successfully!")
    print("You can now run 'python main.py' to launch the GUI application.")
