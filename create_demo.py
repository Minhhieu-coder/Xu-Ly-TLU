"""
Create visual demonstration of all image processing features
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os
from image_processing import ImageProcessor


def create_demo_visualization():
    """Create comprehensive demonstration visualization"""
    
    os.makedirs('demo_results', exist_ok=True)
    
    # Load test images
    gradient = cv2.imread('sample_images/gradient_low_contrast.png', cv2.IMREAD_GRAYSCALE)
    circle = cv2.imread('sample_images/circle.png', cv2.IMREAD_GRAYSCALE)
    noisy = cv2.imread('sample_images/noisy_circle.png', cv2.IMREAD_GRAYSCALE)
    
    print("Creating demonstration visualizations...")
    
    # ===== Bài 4: Contrast Stretching =====
    print("\n1. Bài 4: Contrast Stretching")
    fig = plt.figure(figsize=(15, 5))
    fig.suptitle('Bài 4: Contrast Stretching', fontsize=16, fontweight='bold')
    
    # Original
    ax1 = plt.subplot(1, 4, 1)
    plt.imshow(gradient, cmap='gray')
    plt.title(f'Original\nRange: [{gradient.min()}, {gradient.max()}]')
    plt.axis('off')
    
    # Linear stretching
    stretched = ImageProcessor.contrast_stretching(gradient)
    ax2 = plt.subplot(1, 4, 2)
    plt.imshow(stretched, cmap='gray')
    plt.title(f'Linear Stretching\nRange: [{stretched.min()}, {stretched.max()}]')
    plt.axis('off')
    
    # Type 1 clipping
    clipped1 = ImageProcessor.contrast_clipping_type1(gradient, 75, 125)
    ax3 = plt.subplot(1, 4, 3)
    plt.imshow(clipped1, cmap='gray')
    plt.title(f'Type 1 Clipping [75,125]\nRange: [{clipped1.min()}, {clipped1.max()}]')
    plt.axis('off')
    
    # Type 2 clipping
    clipped2 = ImageProcessor.contrast_clipping_type2(gradient)
    ax4 = plt.subplot(1, 4, 4)
    plt.imshow(clipped2, cmap='gray')
    plt.title(f'Type 2 Region Clipping\nRange: [{clipped2.min()}, {clipped2.max()}]')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('demo_results/bai4_contrast_stretching.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("  ✓ Saved: bai4_contrast_stretching.png")
    
    # ===== Bài 5: Histogram Equalization =====
    print("\n2. Bài 5: Histogram Equalization")
    equalized, hist_orig = ImageProcessor.histogram_equalization(gradient)
    hist_eq = ImageProcessor.calculate_histogram(equalized)
    
    fig = plt.figure(figsize=(12, 8))
    fig.suptitle('Bài 5: Histogram Equalization', fontsize=16, fontweight='bold')
    
    gs = GridSpec(2, 2, figure=fig)
    
    # Original image
    ax1 = fig.add_subplot(gs[0, 0])
    plt.imshow(gradient, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    
    # Original histogram
    ax2 = fig.add_subplot(gs[1, 0])
    plt.bar(range(256), hist_orig, color='blue', alpha=0.7, width=1)
    plt.title('Original Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    # Equalized image
    ax3 = fig.add_subplot(gs[0, 1])
    plt.imshow(equalized, cmap='gray')
    plt.title('Equalized Image')
    plt.axis('off')
    
    # Equalized histogram
    ax4 = fig.add_subplot(gs[1, 1])
    plt.bar(range(256), hist_eq, color='green', alpha=0.7, width=1)
    plt.title('Equalized Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('demo_results/bai5_histogram_equalization.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("  ✓ Saved: bai5_histogram_equalization.png")
    
    # ===== Bài 6: Advanced Histogram =====
    print("\n3. Bài 6: Histogram Matching & Adaptive Equalization")
    
    # Create reference histogram (Gaussian distribution)
    x = np.arange(256)
    reference_hist = np.exp(-((x - 128) ** 2) / (2 * 50 ** 2))
    reference_hist = (reference_hist / reference_hist.sum() * gradient.size).astype(np.uint64)
    
    matched = ImageProcessor.histogram_matching(gradient, reference_hist)
    adaptive = ImageProcessor.adaptive_histogram_equalization(gradient)
    
    fig = plt.figure(figsize=(15, 5))
    fig.suptitle('Bài 6: Histogram Matching & Adaptive Equalization', fontsize=16, fontweight='bold')
    
    ax1 = plt.subplot(1, 3, 1)
    plt.imshow(gradient, cmap='gray')
    plt.title('Original')
    plt.axis('off')
    
    ax2 = plt.subplot(1, 3, 2)
    plt.imshow(matched, cmap='gray')
    plt.title('Histogram Matching\n(Gaussian Reference)')
    plt.axis('off')
    
    ax3 = plt.subplot(1, 3, 3)
    plt.imshow(adaptive, cmap='gray')
    plt.title('Adaptive Equalization\n(CLAHE)')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('demo_results/bai6_advanced_histogram.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("  ✓ Saved: bai6_advanced_histogram.png")
    
    # ===== Bài 7: Noise Removal =====
    print("\n4. Bài 7: Convolution & Noise Removal")
    
    avg3 = ImageProcessor.average_filter(noisy, 3)
    avg5 = ImageProcessor.average_filter(noisy, 5)
    med3 = ImageProcessor.median_filter(noisy, 3)
    med5 = ImageProcessor.median_filter(noisy, 5)
    
    fig = plt.figure(figsize=(15, 10))
    fig.suptitle('Bài 7: Noise Removal Filters Comparison', fontsize=16, fontweight='bold')
    
    images = [
        (circle, 'Original (No Noise)'),
        (noisy, 'Noisy (Salt & Pepper)'),
        (avg3, 'Average Filter 3x3'),
        (avg5, 'Average Filter 5x5'),
        (med3, 'Median Filter 3x3'),
        (med5, 'Median Filter 5x5')
    ]
    
    for idx, (img, title) in enumerate(images):
        ax = plt.subplot(2, 3, idx + 1)
        plt.imshow(img, cmap='gray')
        plt.title(title)
        plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('demo_results/bai7_noise_removal.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("  ✓ Saved: bai7_noise_removal.png")
    
    # ===== Bài 8: Edge Detection =====
    print("\n5. Bài 8: Edge Detection Operators")
    
    sobel, _, _ = ImageProcessor.sobel_edge_detection(circle)
    prewitt, _, _ = ImageProcessor.prewitt_edge_detection(circle)
    roberts, _, _ = ImageProcessor.roberts_edge_detection(circle)
    kirsch = ImageProcessor.kirsch_edge_detection(circle)
    
    fig = plt.figure(figsize=(15, 10))
    fig.suptitle('Bài 8: Edge Detection Operators Comparison', fontsize=16, fontweight='bold')
    
    images = [
        (circle, 'Original'),
        (sobel, 'Sobel Operator'),
        (prewitt, 'Prewitt Operator'),
        (roberts, 'Roberts Operator'),
        (kirsch, 'Kirsch Operator (8-directional)')
    ]
    
    for idx, (img, title) in enumerate(images):
        ax = plt.subplot(2, 3, idx + 1)
        plt.imshow(img, cmap='gray')
        plt.title(title)
        plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('demo_results/bai8_edge_detection.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("  ✓ Saved: bai8_edge_detection.png")
    
    # ===== Bài 9: Laplacian & Sharpening =====
    print("\n6. Bài 9: Laplacian Edge Detection & Sharpening")
    
    lap4 = ImageProcessor.laplacian_4_neighbor(circle)
    lap8 = ImageProcessor.laplacian_8_neighbor(circle)
    log = ImageProcessor.laplacian_of_gaussian(circle)
    sharp_lap = ImageProcessor.sharpen_image(circle, 'laplacian')
    sharp_log = ImageProcessor.sharpen_image(circle, 'log')
    
    fig = plt.figure(figsize=(15, 10))
    fig.suptitle('Bài 9: Laplacian Edge Detection & Image Sharpening', fontsize=16, fontweight='bold')
    
    images = [
        (circle, 'Original'),
        (lap4, 'Laplacian 4-neighbor'),
        (lap8, 'Laplacian 8-neighbor'),
        (log, 'Laplacian of Gaussian (LoG)'),
        (sharp_lap, 'Sharpened (Laplacian)'),
        (sharp_log, 'Sharpened (LoG)')
    ]
    
    for idx, (img, title) in enumerate(images):
        ax = plt.subplot(2, 3, idx + 1)
        plt.imshow(img, cmap='gray')
        plt.title(title)
        plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('demo_results/bai9_laplacian_sharpening.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("  ✓ Saved: bai9_laplacian_sharpening.png")
    
    # ===== Complete Workflow Demo =====
    print("\n7. Creating Complete Workflow Demonstration")
    
    # Test with checkerboard
    checkerboard = cv2.imread('sample_images/checkerboard.png', cv2.IMREAD_GRAYSCALE)
    
    # Apply various processing steps
    cb_stretched = ImageProcessor.contrast_stretching(checkerboard)
    cb_equalized, _ = ImageProcessor.histogram_equalization(checkerboard)
    cb_sobel, _, _ = ImageProcessor.sobel_edge_detection(checkerboard)
    cb_sharpened = ImageProcessor.sharpen_image(checkerboard, 'laplacian')
    
    fig = plt.figure(figsize=(15, 10))
    fig.suptitle('Complete Workflow: Checkerboard Processing', fontsize=16, fontweight='bold')
    
    workflow = [
        (checkerboard, 'Original'),
        (cb_stretched, 'Contrast Stretched'),
        (cb_equalized, 'Histogram Equalized'),
        (cb_sobel, 'Sobel Edge Detection'),
        (cb_sharpened, 'Sharpened')
    ]
    
    for idx, (img, title) in enumerate(workflow):
        ax = plt.subplot(2, 3, idx + 1)
        plt.imshow(img, cmap='gray')
        plt.title(title)
        plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('demo_results/complete_workflow.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("  ✓ Saved: complete_workflow.png")
    
    print("\n" + "="*60)
    print("All demonstration images created successfully!")
    print("Location: demo_results/")
    print("="*60)


if __name__ == "__main__":
    create_demo_visualization()
