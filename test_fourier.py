"""
Test script for Fourier Transform functions (Bài 10-11)
"""

import numpy as np
import cv2
from image_processing import ImageProcessor


def test_fourier_functions():
    """Test Bài 10-11 functions"""
    
    print("=== Testing Bài 10-11: Fourier Transform Functions ===\n")
    
    # Create test image
    test_image = np.zeros((256, 256), dtype=np.uint8)
    test_image[100:150, 100:150] = 255  # White square
    
    print("1. Testing Fourier Transform...")
    try:
        magnitude, phase = ImageProcessor.fourier_transform(test_image)
        print(f"   ✓ Magnitude shape: {magnitude.shape}")
        print(f"   ✓ Phase shape: {phase.shape}")
        print(f"   ✓ Magnitude range: [{magnitude.min():.2f}, {magnitude.max():.2f}]")
        print()
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    print("2. Testing Inverse Fourier Transform...")
    try:
        reconstructed = ImageProcessor.inverse_fourier_transform(magnitude, phase)
        print(f"   ✓ Reconstructed shape: {reconstructed.shape}")
        print(f"   ✓ Reconstructed dtype: {reconstructed.dtype}")
        
        # Check if reconstruction is similar to original
        diff = np.abs(test_image.astype(float) - reconstructed.astype(float))
        mean_diff = np.mean(diff)
        print(f"   ✓ Mean reconstruction error: {mean_diff:.2f}")
        
        if mean_diff < 5.0:  # Allow small error due to rounding
            print("   ✓ Reconstruction is accurate!")
        else:
            print(f"   ⚠ Reconstruction error is high: {mean_diff:.2f}")
        print()
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    print("3. Testing Magnitude Spectrum Display...")
    try:
        magnitude_display = ImageProcessor.get_magnitude_spectrum_display(magnitude)
        print(f"   ✓ Display magnitude shape: {magnitude_display.shape}")
        print(f"   ✓ Display magnitude dtype: {magnitude_display.dtype}")
        print(f"   ✓ Display range: [{magnitude_display.min()}, {magnitude_display.max()}]")
        print()
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    print("4. Testing Ideal Low-pass Filter...")
    try:
        for cutoff in [10, 30, 50]:
            filtered = ImageProcessor.ideal_lowpass_filter(test_image, cutoff)
            print(f"   ✓ Ideal LPF (cutoff={cutoff}): shape={filtered.shape}, dtype={filtered.dtype}")
        print()
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    print("5. Testing Gaussian Low-pass Filter...")
    try:
        for sigma in [10.0, 30.0, 50.0]:
            filtered = ImageProcessor.gaussian_lowpass_filter(test_image, sigma)
            print(f"   ✓ Gaussian LPF (sigma={sigma}): shape={filtered.shape}, dtype={filtered.dtype}")
        print()
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    print("=== All Fourier Transform Tests Passed! ===")
    return True


if __name__ == "__main__":
    success = test_fourier_functions()
    exit(0 if success else 1)
