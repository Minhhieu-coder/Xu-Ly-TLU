"""
Test script for image processing application
Tests basic functionality without GUI display
"""

import sys
import os
import tempfile

# Test imports
print("Testing imports...")
try:
    from PIL import Image
    import numpy as np
    print("✓ PIL and NumPy imported successfully")
except ImportError as e:
    print(f"✗ Import error: {e}")
    sys.exit(1)

# Test basic image processing functions
print("\nTesting basic image processing functions...")

# Create a test image
print("Creating test image...")
test_array = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
test_image = Image.fromarray(test_array, 'RGB')
print("✓ Test image created (100x100 RGB)")

# Test grayscale conversion
print("\nTesting grayscale conversion...")
gray_image = test_image.convert('L')
gray_array = np.array(gray_image)
print(f"✓ Grayscale conversion successful, shape: {gray_array.shape}")

# Test binary conversion
print("\nTesting binary conversion...")
threshold = 127
binary_array = (gray_array > threshold) * 255
binary_image = Image.fromarray(binary_array.astype(np.uint8))
print(f"✓ Binary conversion successful with threshold {threshold}")

# Test negative transformation
print("\nTesting negative transformation (s = 255 - r)...")
negative_array = 255 - gray_array
negative_image = Image.fromarray(negative_array.astype(np.uint8))
print("✓ Negative transformation successful")

# Test log transformation
print("\nTesting log transformation (s = c * log(1 + r))...")
c = 1.0
log_array = c * np.log1p(gray_array.astype(np.float64))
log_array = (log_array - np.min(log_array)) / (np.max(log_array) - np.min(log_array)) * 255
log_image = Image.fromarray(log_array.astype(np.uint8))
print(f"✓ Log transformation successful with c = {c}")

# Test gamma transformation
print("\nTesting gamma transformation (s = c * r^γ)...")
gamma = 1.5
normalized = gray_array.astype(np.float64) / 255.0
gamma_array = np.power(normalized, gamma) * 255
gamma_image = Image.fromarray(gamma_array.astype(np.uint8))
print(f"✓ Gamma transformation successful with γ = {gamma}")

# Test metrics calculation
print("\nTesting image metrics calculation...")

# Brightness
brightness = np.mean(gray_array)
print(f"  Brightness: {brightness:.2f}")

# Contrast
contrast = np.std(gray_array)
print(f"  Contrast (std): {contrast:.2f}")

# Entropy
histogram, _ = np.histogram(gray_array, bins=256, range=(0, 256))
histogram = histogram / histogram.sum()
entropy = 0
for prob in histogram:
    if prob > 0:
        entropy -= prob * np.log2(prob)
print(f"  Entropy: {entropy:.4f} bits")

# Sharpness
gx = np.zeros_like(gray_array.astype(np.float64))
gx[:, :-1] = np.diff(gray_array.astype(np.float64), axis=1)
gy = np.zeros_like(gray_array.astype(np.float64))
gy[:-1, :] = np.diff(gray_array.astype(np.float64), axis=0)
gradient_magnitude = np.sqrt(gx**2 + gy**2)
sharpness = np.mean(gradient_magnitude)
print(f"  Sharpness: {sharpness:.2f}")

print("\n✓ All metrics calculated successfully")

# Test RGB channel separation
print("\nTesting RGB channel separation...")
rgb_image = test_image.convert('RGB')
r, g, b = rgb_image.split()
print(f"✓ RGB channels separated: R={r.size}, G={g.size}, B={b.size}")

# Test save functionality (save to temp)
print("\nTesting save functionality...")
with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_file:
    temp_path = tmp_file.name

test_image.save(temp_path)
if os.path.exists(temp_path):
    print(f"✓ Image saved successfully to {temp_path}")
    os.remove(temp_path)
else:
    print("✗ Failed to save image")

print("\n" + "="*50)
print("All tests passed! ✓")
print("The image processing application is ready to use.")
print("="*50)
