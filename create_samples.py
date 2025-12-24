"""
Demo script to create sample images for testing the application
Creates various test images to demonstrate all features
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

# Create output directory
output_dir = "sample_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created directory: {output_dir}")

print("Creating sample images for testing...\n")

# 1. Simple gradient image
print("1. Creating gradient image...")
width, height = 400, 300
gradient = np.zeros((height, width), dtype=np.uint8)
for i in range(height):
    gradient[i, :] = int(255 * i / height)
gradient_img = Image.fromarray(gradient)
gradient_img.save(f"{output_dir}/01_gradient.png")
print(f"   Saved: {output_dir}/01_gradient.png")

# 2. RGB color image
print("2. Creating RGB color image...")
rgb_array = np.zeros((300, 400, 3), dtype=np.uint8)
# Red gradient on left
rgb_array[:, :133, 0] = gradient[:, :133]
# Green gradient in middle
rgb_array[:, 133:266, 1] = gradient[:, 133:266]
# Blue gradient on right
rgb_array[:, 266:, 2] = gradient[:, 266:]
rgb_img = Image.fromarray(rgb_array)
rgb_img.save(f"{output_dir}/02_rgb_colors.png")
print(f"   Saved: {output_dir}/02_rgb_colors.png")

# 3. Dark image (underexposed)
print("3. Creating dark/underexposed image...")
dark_array = np.random.randint(0, 80, (300, 400), dtype=np.uint8)
# Add some structure
for i in range(0, 400, 40):
    dark_array[:, i:i+20] = np.minimum(dark_array[:, i:i+20] + 30, 255)
dark_img = Image.fromarray(dark_array)
dark_img.save(f"{output_dir}/03_dark_image.png")
print(f"   Saved: {output_dir}/03_dark_image.png")

# 4. Bright image (overexposed)
print("4. Creating bright/overexposed image...")
bright_array = np.random.randint(175, 256, (300, 400), dtype=np.uint8)
# Add some structure
for i in range(0, 300, 30):
    bright_array[i:i+15, :] = np.maximum(bright_array[i:i+15, :] - 30, 0)
bright_img = Image.fromarray(bright_array)
bright_img.save(f"{output_dir}/04_bright_image.png")
print(f"   Saved: {output_dir}/04_bright_image.png")

# 5. Checkerboard pattern
print("5. Creating checkerboard pattern...")
checkerboard = np.zeros((300, 400), dtype=np.uint8)
square_size = 30
for i in range(0, 300, square_size):
    for j in range(0, 400, square_size):
        if ((i // square_size) + (j // square_size)) % 2 == 0:
            checkerboard[i:i+square_size, j:j+square_size] = 255
checker_img = Image.fromarray(checkerboard)
checker_img.save(f"{output_dir}/05_checkerboard.png")
print(f"   Saved: {output_dir}/05_checkerboard.png")

# 6. Geometric shapes
print("6. Creating geometric shapes...")
shapes_img = Image.new('RGB', (400, 300), color='white')
draw = ImageDraw.Draw(shapes_img)
# Red circle
draw.ellipse([50, 50, 150, 150], fill='red', outline='black')
# Green rectangle
draw.rectangle([200, 50, 350, 150], fill='green', outline='black')
# Blue triangle
draw.polygon([(100, 200), (200, 270), (0, 270)], fill='blue', outline='black')
# Yellow star-like shape
draw.polygon([(300, 200), (320, 250), (370, 250), (330, 270), 
              (350, 290), (300, 270), (250, 290), (270, 270), 
              (230, 250), (280, 250)], fill='yellow', outline='black')
shapes_img.save(f"{output_dir}/06_shapes.png")
print(f"   Saved: {output_dir}/06_shapes.png")

# 7. PNG with alpha channel (transparency)
print("7. Creating PNG with alpha channel...")
alpha_img = Image.new('RGBA', (400, 300), color=(255, 255, 255, 0))
draw = ImageDraw.Draw(alpha_img)
# Semi-transparent red circle
for alpha in range(0, 256, 51):
    radius = 40 - alpha // 15
    draw.ellipse([200-radius, 150-radius, 200+radius, 150+radius], 
                 fill=(255, 0, 0, alpha))
# Solid blue rectangle
draw.rectangle([50, 50, 150, 100], fill=(0, 0, 255, 255))
# Transparent green rectangle
draw.rectangle([250, 200, 350, 250], fill=(0, 255, 0, 128))
alpha_img.save(f"{output_dir}/07_alpha_transparency.png")
print(f"   Saved: {output_dir}/07_alpha_transparency.png")

# 8. High contrast image
print("8. Creating high contrast image...")
high_contrast = np.zeros((300, 400), dtype=np.uint8)
# Black and white stripes
for i in range(0, 400, 20):
    if (i // 20) % 2 == 0:
        high_contrast[:, i:i+20] = 255
    else:
        high_contrast[:, i:i+20] = 0
contrast_img = Image.fromarray(high_contrast)
contrast_img.save(f"{output_dir}/08_high_contrast.png")
print(f"   Saved: {output_dir}/08_high_contrast.png")

# 9. Low contrast image
print("9. Creating low contrast image...")
low_contrast = np.random.randint(100, 156, (300, 400), dtype=np.uint8)
low_img = Image.fromarray(low_contrast)
low_img.save(f"{output_dir}/09_low_contrast.png")
print(f"   Saved: {output_dir}/09_low_contrast.png")

# 10. Detailed image (high entropy)
print("10. Creating detailed/complex image...")
np.random.seed(42)
complex_array = np.random.randint(0, 256, (300, 400), dtype=np.uint8)
complex_img = Image.fromarray(complex_array)
complex_img.save(f"{output_dir}/10_complex_detailed.png")
print(f"   Saved: {output_dir}/10_complex_detailed.png")

print("\n" + "="*60)
print(f"✓ Successfully created 10 sample images in '{output_dir}/' directory")
print("="*60)
print("\nYou can now use these images to test all features:")
print("  - Load images from the 'sample_images' folder")
print("  - Test grayscale conversion")
print("  - Test binary conversion with different thresholds")
print("  - Test RGB channel separation")
print("  - Test alpha channel (use 07_alpha_transparency.png)")
print("  - Test metrics calculation")
print("  - Test image enhancement functions")
print("\nRecommended test images:")
print("  - Dark image enhancement: 03_dark_image.png")
print("  - Bright image adjustment: 04_bright_image.png")
print("  - High contrast analysis: 08_high_contrast.png")
print("  - Low contrast analysis: 09_low_contrast.png")
print("  - Alpha channel test: 07_alpha_transparency.png")
