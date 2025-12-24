"""
Simple example demonstrating Bài 12 high-pass filters
Quick start guide for using the high-pass filters
"""

import cv2
import numpy as np
from image_processing import ImageProcessor

def simple_example():
    """Simple example showing how to use high-pass filters"""
    
    print("=== Bài 12: High-Pass Filter Simple Example ===\n")
    
    # 1. Load an image (or create a test image)
    # Replace 'your_image.jpg' with your actual image path
    image_path = 'sample_images/06_shapes.png'
    
    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise ValueError("Could not load image")
        print(f"✓ Loaded image: {image_path}")
        print(f"  Size: {image.shape[1]}x{image.shape[0]}")
    except:
        # If no image available, create a simple test image
        print("Creating test image...")
        image = np.zeros((256, 256), dtype=np.uint8)
        cv2.rectangle(image, (50, 50), (200, 200), 255, -1)
        cv2.circle(image, (128, 128), 40, 128, -1)
    
    print()
    
    # 2. Apply Ideal High-pass Filter
    print("Applying Ideal High-pass Filter...")
    ideal_result = ImageProcessor.ideal_highpass_filter(image, cutoff_frequency=30)
    print(f"✓ Ideal filter applied")
    print(f"  Output range: [{ideal_result.min()}, {ideal_result.max()}]")
    print()
    
    # 3. Apply Butterworth High-pass Filter
    print("Applying Butterworth High-pass Filter...")
    butter_result = ImageProcessor.butterworth_highpass_filter(image, D0=30, n=2)
    print(f"✓ Butterworth filter applied")
    print(f"  Output range: [{butter_result.min()}, {butter_result.max()}]")
    print()
    
    # 4. Save results
    cv2.imwrite('output_ideal_highpass.png', ideal_result)
    cv2.imwrite('output_butterworth_highpass.png', butter_result)
    
    print("=" * 60)
    print("Results saved:")
    print("  - output_ideal_highpass.png")
    print("  - output_butterworth_highpass.png")
    print("=" * 60)
    print()
    print("Tips:")
    print("  • Larger D0 → passes more low freq → subtler edges")
    print("  • Smaller D0 → blocks more low freq → stronger edges")
    print("  • Higher n in Butterworth → sharper transition")
    print("  • Butterworth reduces ringing compared to Ideal")


if __name__ == "__main__":
    simple_example()
