"""
Demo script to generate sample images for testing
Tạo ảnh mẫu để test các chức năng
"""

import numpy as np
import cv2
import os

def create_sample_images():
    """Create sample images for testing"""
    
    # Create sample_images directory if it doesn't exist
    os.makedirs("sample_images", exist_ok=True)
    
    print("Tạo ảnh mẫu / Creating sample images...")
    
    # 1. Gradient image (for contrast stretching)
    gradient = np.linspace(0, 255, 256).astype(np.uint8)
    gradient_img = np.tile(gradient, (256, 1))
    cv2.imwrite("sample_images/gradient.png", gradient_img)
    print("✓ Created gradient.png")
    
    # 2. Low contrast image (for histogram equalization)
    low_contrast = np.random.randint(80, 120, (256, 256), dtype=np.uint8)
    cv2.imwrite("sample_images/low_contrast.png", low_contrast)
    print("✓ Created low_contrast.png")
    
    # 3. Checkerboard (for edge detection)
    checkerboard = np.zeros((256, 256), dtype=np.uint8)
    square_size = 32
    for i in range(0, 256, square_size):
        for j in range(0, 256, square_size):
            if ((i // square_size) + (j // square_size)) % 2 == 0:
                checkerboard[i:i+square_size, j:j+square_size] = 255
    cv2.imwrite("sample_images/checkerboard.png", checkerboard)
    print("✓ Created checkerboard.png")
    
    # 4. Circle (for Fourier transform)
    circle = np.zeros((256, 256), dtype=np.uint8)
    cv2.circle(circle, (128, 128), 60, 255, -1)
    cv2.imwrite("sample_images/circle.png", circle)
    print("✓ Created circle.png")
    
    # 5. Noisy image (for filter testing)
    clean = np.ones((256, 256), dtype=np.uint8) * 128
    noisy = clean.copy()
    # Add salt and pepper noise
    num_salt = int(0.02 * 256 * 256)
    num_pepper = int(0.02 * 256 * 256)
    
    # Salt
    coords = [np.random.randint(0, i - 1, num_salt) for i in noisy.shape]
    noisy[coords[0], coords[1]] = 255
    
    # Pepper
    coords = [np.random.randint(0, i - 1, num_pepper) for i in noisy.shape]
    noisy[coords[0], coords[1]] = 0
    
    cv2.imwrite("sample_images/noisy.png", noisy)
    print("✓ Created noisy.png")
    
    # 6. Real-world test image (Lena-like pattern)
    # Create a simple pattern
    test_img = np.zeros((256, 256), dtype=np.uint8)
    
    # Background
    test_img[:] = 100
    
    # Add some shapes
    cv2.circle(test_img, (64, 64), 40, 200, -1)
    cv2.rectangle(test_img, (150, 50), (230, 130), 150, -1)
    cv2.circle(test_img, (128, 200), 30, 50, -1)
    
    cv2.imwrite("sample_images/test_image.png", test_img)
    print("✓ Created test_image.png")
    
    # 7. Color image (RGB)
    color_img = np.zeros((256, 256, 3), dtype=np.uint8)
    color_img[:, :85, 0] = 255  # Red
    color_img[:, 85:170, 1] = 255  # Green
    color_img[:, 170:, 2] = 255  # Blue
    cv2.imwrite("sample_images/color_bars.png", color_img)
    print("✓ Created color_bars.png")
    
    print("\nHoàn thành! Tất cả ảnh mẫu đã được tạo trong thư mục 'sample_images/'")
    print("Completed! All sample images created in 'sample_images/' directory")
    print("\nCác ảnh tạo ra / Images created:")
    print("1. gradient.png - Test contrast stretching")
    print("2. low_contrast.png - Test histogram equalization")
    print("3. checkerboard.png - Test edge detection")
    print("4. circle.png - Test Fourier transform")
    print("5. noisy.png - Test noise filters")
    print("6. test_image.png - General testing")
    print("7. color_bars.png - Test RGB channel separation")

if __name__ == "__main__":
    create_sample_images()
