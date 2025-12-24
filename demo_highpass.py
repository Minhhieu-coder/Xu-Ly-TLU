"""
Demo script to visualize high-pass filter results (Bài 12)
This script generates comparison images showing the effects of both filters
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
from image_processing import ImageProcessor
import os


def demo_highpass_filters():
    """Demonstrate high-pass filters with visual output"""
    
    print("=== Bài 12: High-Pass Filter Demonstration ===\n")
    
    # Try to load a sample image, or create one
    sample_path = "sample_images/06_shapes.png"
    if os.path.exists(sample_path):
        print(f"Loading sample image: {sample_path}")
        test_image = cv2.imread(sample_path, cv2.IMREAD_GRAYSCALE)
    else:
        print("Creating test image with geometric shapes...")
        # Create a more interesting test image
        test_image = np.zeros((256, 256), dtype=np.uint8)
        # Add circle
        cv2.circle(test_image, (128, 128), 50, 255, -1)
        # Add rectangle
        cv2.rectangle(test_image, (50, 50), (100, 100), 200, -1)
        # Add some noise for texture
        noise = np.random.normal(0, 10, test_image.shape)
        test_image = np.clip(test_image.astype(float) + noise, 0, 255).astype(np.uint8)
    
    print(f"Test image shape: {test_image.shape}")
    print(f"Test image range: [{test_image.min()}, {test_image.max()}]\n")
    
    # Apply filters with different parameters
    print("Applying Ideal High-pass Filter with different cutoff values...")
    ideal_d0_10 = ImageProcessor.ideal_highpass_filter(test_image, 10)
    ideal_d0_30 = ImageProcessor.ideal_highpass_filter(test_image, 30)
    ideal_d0_50 = ImageProcessor.ideal_highpass_filter(test_image, 50)
    print("✓ Ideal filters applied\n")
    
    print("Applying Butterworth High-pass Filter with different parameters...")
    butter_n1 = ImageProcessor.butterworth_highpass_filter(test_image, 30, 1)
    butter_n2 = ImageProcessor.butterworth_highpass_filter(test_image, 30, 2)
    butter_n5 = ImageProcessor.butterworth_highpass_filter(test_image, 30, 5)
    print("✓ Butterworth filters applied\n")
    
    # Create comparison figure 1: Ideal High-pass with different cutoffs
    print("Creating visualization 1: Ideal High-pass comparison...")
    fig1, axes1 = plt.subplots(2, 2, figsize=(12, 10))
    fig1.suptitle('Bài 12.1: Ideal High-Pass Filter - Different Cutoff Values', 
                  fontsize=14, fontweight='bold')
    
    axes1[0, 0].imshow(test_image, cmap='gray')
    axes1[0, 0].set_title('Original Image')
    axes1[0, 0].axis('off')
    
    axes1[0, 1].imshow(ideal_d0_10, cmap='gray')
    axes1[0, 1].set_title('Ideal High-pass (D0=10)\nSharp transition, more edges')
    axes1[0, 1].axis('off')
    
    axes1[1, 0].imshow(ideal_d0_30, cmap='gray')
    axes1[1, 0].set_title('Ideal High-pass (D0=30)\nMedium transition')
    axes1[1, 0].axis('off')
    
    axes1[1, 1].imshow(ideal_d0_50, cmap='gray')
    axes1[1, 1].set_title('Ideal High-pass (D0=50)\nSoft transition, subtle edges')
    axes1[1, 1].axis('off')
    
    plt.tight_layout()
    output1 = 'bai12_ideal_highpass_comparison.png'
    plt.savefig(output1, dpi=150, bbox_inches='tight')
    print(f"✓ Saved: {output1}\n")
    plt.close()
    
    # Create comparison figure 2: Butterworth High-pass with different orders
    print("Creating visualization 2: Butterworth High-pass comparison...")
    fig2, axes2 = plt.subplots(2, 2, figsize=(12, 10))
    fig2.suptitle('Bài 12.2: Butterworth High-Pass Filter - Different Orders (D0=30)', 
                  fontsize=14, fontweight='bold')
    
    axes2[0, 0].imshow(test_image, cmap='gray')
    axes2[0, 0].set_title('Original Image')
    axes2[0, 0].axis('off')
    
    axes2[0, 1].imshow(butter_n1, cmap='gray')
    axes2[0, 1].set_title('Butterworth (n=1)\nVery smooth transition')
    axes2[0, 1].axis('off')
    
    axes2[1, 0].imshow(butter_n2, cmap='gray')
    axes2[1, 0].set_title('Butterworth (n=2)\nModerate transition')
    axes2[1, 0].axis('off')
    
    axes2[1, 1].imshow(butter_n5, cmap='gray')
    axes2[1, 1].set_title('Butterworth (n=5)\nSharper transition')
    axes2[1, 1].axis('off')
    
    plt.tight_layout()
    output2 = 'bai12_butterworth_highpass_comparison.png'
    plt.savefig(output2, dpi=150, bbox_inches='tight')
    print(f"✓ Saved: {output2}\n")
    plt.close()
    
    # Create comparison figure 3: Ideal vs Butterworth
    print("Creating visualization 3: Ideal vs Butterworth comparison...")
    fig3, axes3 = plt.subplots(2, 3, figsize=(15, 10))
    fig3.suptitle('Bài 12: Ideal vs Butterworth High-Pass Filters (D0=30)', 
                  fontsize=14, fontweight='bold')
    
    axes3[0, 0].imshow(test_image, cmap='gray')
    axes3[0, 0].set_title('Original Image')
    axes3[0, 0].axis('off')
    
    axes3[0, 1].imshow(ideal_d0_30, cmap='gray')
    axes3[0, 1].set_title('Ideal High-pass\n(Sharp cutoff, may have ringing)')
    axes3[0, 1].axis('off')
    
    axes3[0, 2].imshow(butter_n2, cmap='gray')
    axes3[0, 2].set_title('Butterworth High-pass (n=2)\n(Smooth transition, less ringing)')
    axes3[0, 2].axis('off')
    
    # Show histograms
    axes3[1, 0].hist(test_image.ravel(), bins=50, color='blue', alpha=0.7)
    axes3[1, 0].set_title('Original Histogram')
    axes3[1, 0].set_xlim([0, 255])
    
    axes3[1, 1].hist(ideal_d0_30.ravel(), bins=50, color='red', alpha=0.7)
    axes3[1, 1].set_title('Ideal High-pass Histogram')
    axes3[1, 1].set_xlim([0, 255])
    
    axes3[1, 2].hist(butter_n2.ravel(), bins=50, color='green', alpha=0.7)
    axes3[1, 2].set_title('Butterworth Histogram')
    axes3[1, 2].set_xlim([0, 255])
    
    plt.tight_layout()
    output3 = 'bai12_ideal_vs_butterworth.png'
    plt.savefig(output3, dpi=150, bbox_inches='tight')
    print(f"✓ Saved: {output3}\n")
    plt.close()
    
    print("=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)
    print("\nGenerated files:")
    print(f"  1. {output1}")
    print(f"  2. {output2}")
    print(f"  3. {output3}")
    print("\nKey observations:")
    print("  • Ideal High-pass: Sharp frequency cutoff, may show ringing")
    print("  • Butterworth High-pass: Smooth transition, reduces artifacts")
    print("  • Higher order (n) in Butterworth → sharper transition")
    print("  • Larger D0 → passes more low frequencies → subtler edges")


if __name__ == "__main__":
    demo_highpass_filters()
