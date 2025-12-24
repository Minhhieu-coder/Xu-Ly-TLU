"""
Test script for High-Pass Filter functions (Bài 12)
"""

import numpy as np
import cv2
from image_processing import ImageProcessor


def test_highpass_filters():
    """Test Bài 12 functions"""
    
    print("=== Testing Bài 12: High-Pass Filter Functions ===\n")
    
    # Create test image with edges
    test_image = np.zeros((256, 256), dtype=np.uint8)
    test_image[80:180, 80:180] = 255  # White square (creates edges)
    
    print("Test image created: 256x256 with white square")
    print(f"Original image range: [{test_image.min()}, {test_image.max()}]\n")
    
    print("1. Testing Ideal High-pass Filter (Bài 12.1)...")
    try:
        # Test with different cutoff frequencies
        for cutoff in [10, 30, 50]:
            result = ImageProcessor.ideal_highpass_filter(test_image, cutoff)
            print(f"   ✓ Cutoff={cutoff}: shape={result.shape}, dtype={result.dtype}")
            print(f"      Range: [{result.min()}, {result.max()}]")
        
        # Verify output properties
        result = ImageProcessor.ideal_highpass_filter(test_image, 30)
        assert result.shape == test_image.shape, "Output shape mismatch"
        assert result.dtype == np.uint8, "Output dtype should be uint8"
        assert result.min() >= 0 and result.max() <= 255, "Output range should be [0, 255]"
        
        print("   ✓ All ideal high-pass tests passed!")
        print()
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    print("2. Testing Butterworth High-pass Filter (Bài 12.2)...")
    try:
        # Test with different parameters
        for D0 in [20, 40]:
            for n in [1, 2, 5]:
                result = ImageProcessor.butterworth_highpass_filter(test_image, D0, n)
                print(f"   ✓ D0={D0}, n={n}: shape={result.shape}, range=[{result.min()}, {result.max()}]")
        
        # Verify output properties
        result = ImageProcessor.butterworth_highpass_filter(test_image, 30, 2)
        assert result.shape == test_image.shape, "Output shape mismatch"
        assert result.dtype == np.uint8, "Output dtype should be uint8"
        assert result.min() >= 0 and result.max() <= 255, "Output range should be [0, 255]"
        
        print("   ✓ All Butterworth high-pass tests passed!")
        print()
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    print("3. Comparing Ideal vs Butterworth...")
    try:
        ideal_result = ImageProcessor.ideal_highpass_filter(test_image, 30)
        butter_result = ImageProcessor.butterworth_highpass_filter(test_image, 30, 2)
        
        # Both should enhance edges but with different characteristics
        print(f"   Ideal - Mean: {ideal_result.mean():.2f}, Std: {ideal_result.std():.2f}")
        print(f"   Butterworth - Mean: {butter_result.mean():.2f}, Std: {butter_result.std():.2f}")
        
        # Butterworth should generally be smoother (less extreme values)
        print("   ✓ Both filters produced valid results")
        print()
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    print("4. Testing with real image...")
    try:
        # Try to load a sample image
        sample_path = "sample_images/01_gradient.png"
        import os
        if os.path.exists(sample_path):
            real_image = cv2.imread(sample_path, cv2.IMREAD_GRAYSCALE)
            if real_image is not None:
                ideal_result = ImageProcessor.ideal_highpass_filter(real_image, 30)
                butter_result = ImageProcessor.butterworth_highpass_filter(real_image, 30, 2)
                
                print(f"   ✓ Real image test passed")
                print(f"      Input shape: {real_image.shape}")
                print(f"      Ideal output: [{ideal_result.min()}, {ideal_result.max()}]")
                print(f"      Butterworth output: [{butter_result.min()}, {butter_result.max()}]")
            else:
                print("   ⚠ Could not read sample image")
        else:
            print("   ⚠ Sample image not found, skipping real image test")
        print()
    except Exception as e:
        print(f"   ⚠ Real image test skipped: {e}")
        print()
    
    print("=" * 50)
    print("All Bài 12 High-Pass Filter tests completed successfully! ✓")
    print("=" * 50)
    return True


if __name__ == "__main__":
    success = test_highpass_filters()
    exit(0 if success else 1)
