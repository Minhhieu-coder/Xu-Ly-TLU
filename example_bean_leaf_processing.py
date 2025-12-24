#!/usr/bin/env python3
"""
Example script demonstrating how to use the Bean Leaf Lesions dataset
with the image processing tools in this repository.

This script shows:
1. Loading images from the dataset
2. Applying various image processing techniques
3. Saving processed results
4. Batch processing multiple images

Requirements:
    - Download the dataset first: python download_dataset.py
    - Install dependencies: pip install numpy opencv-python pillow matplotlib scipy

Usage:
    python example_bean_leaf_processing.py
"""

import os
import cv2
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

# Import image processing functions from the repository
try:
    from image_processing import (
        convert_to_grayscale,
        apply_median_filter,
        sobel_edge_detection,
        apply_gaussian_blur,
        histogram_equalization,
        linear_contrast_stretching
    )
    PROCESSING_AVAILABLE = True
except ImportError:
    print("Warning: Could not import image_processing module")
    print("Some features may not be available")
    PROCESSING_AVAILABLE = False


def check_dataset_exists():
    """Check if the bean leaf dataset has been downloaded."""
    dataset_dir = Path(__file__).parent / "data" / "bean-leaf-lesions"
    
    if not dataset_dir.exists():
        print("❌ Dataset directory not found!")
        print(f"   Expected location: {dataset_dir}")
        print("\n📖 Please download the dataset first:")
        print("   python download_dataset.py")
        return False
    
    # Check for expected subdirectories
    expected_dirs = ["train", "test", "validation"]
    found_dirs = [d for d in expected_dirs if (dataset_dir / d).exists()]
    
    if not found_dirs:
        print("❌ Dataset appears to be empty!")
        print(f"   Expected subdirectories: {', '.join(expected_dirs)}")
        print("\n📖 Please download the dataset first:")
        print("   python download_dataset.py")
        return False
    
    print(f"✓ Dataset found at: {dataset_dir}")
    print(f"  Available directories: {', '.join(found_dirs)}")
    return True


def get_sample_images(category="angular_leaf_spot", split="train", max_images=5):
    """
    Get sample images from the dataset.
    
    Args:
        category: Disease category (angular_leaf_spot, bean_rust, healthy)
        split: Dataset split (train, test, validation)
        max_images: Maximum number of images to return
    
    Returns:
        List of image file paths
    """
    dataset_dir = Path(__file__).parent / "data" / "bean-leaf-lesions"
    category_dir = dataset_dir / split / category
    
    if not category_dir.exists():
        print(f"❌ Category directory not found: {category_dir}")
        return []
    
    # Get image files
    image_extensions = ['.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG']
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(category_dir.glob(f"*{ext}"))
    
    # Return up to max_images
    return sorted(image_files)[:max_images]


def process_single_image(image_path, output_dir):
    """
    Process a single image and save results.
    
    Args:
        image_path: Path to input image
        output_dir: Directory to save processed images
    """
    print(f"\n📸 Processing: {image_path.name}")
    
    # Load image
    img = cv2.imread(str(image_path))
    if img is None:
        print(f"  ❌ Could not load image: {image_path}")
        return
    
    print(f"  Image size: {img.shape[1]}x{img.shape[0]}")
    
    # Create output directory
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Base name for output files
    base_name = image_path.stem
    
    # 1. Grayscale conversion
    if PROCESSING_AVAILABLE:
        gray = convert_to_grayscale(img)
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cv2.imwrite(str(output_dir / f"{base_name}_grayscale.jpg"), gray)
    print(f"  ✓ Saved grayscale version")
    
    # 2. Histogram equalization (enhances contrast)
    if PROCESSING_AVAILABLE:
        enhanced = histogram_equalization(gray)
    else:
        enhanced = cv2.equalizeHist(gray)
    
    cv2.imwrite(str(output_dir / f"{base_name}_enhanced.jpg"), enhanced)
    print(f"  ✓ Saved enhanced version")
    
    # 3. Edge detection (useful for lesion boundary detection)
    if PROCESSING_AVAILABLE:
        edges = sobel_edge_detection(gray)
    else:
        # Simple Sobel edge detection
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        edges = np.sqrt(sobelx**2 + sobely**2)
        # Prevent division by zero
        edges = np.uint8(edges / edges.max() * 255) if edges.max() > 0 else edges.astype(np.uint8)
    
    cv2.imwrite(str(output_dir / f"{base_name}_edges.jpg"), edges)
    print(f"  ✓ Saved edge detection")
    
    # 4. Median filter (noise reduction)
    if PROCESSING_AVAILABLE:
        denoised = apply_median_filter(gray, kernel_size=5)
    else:
        denoised = cv2.medianBlur(gray, 5)
    
    cv2.imwrite(str(output_dir / f"{base_name}_denoised.jpg"), denoised)
    print(f"  ✓ Saved denoised version")
    
    print(f"  ✅ Processing complete!")


def create_visualization(image_paths, output_file):
    """
    Create a visualization comparing original and processed images.
    
    Args:
        image_paths: List of image paths to visualize
        output_file: Path to save the visualization
    """
    if not image_paths:
        print("No images to visualize")
        return
    
    # Limit to 3 images for visualization
    image_paths = image_paths[:3]
    
    fig, axes = plt.subplots(len(image_paths), 5, figsize=(15, 3*len(image_paths)))
    if len(image_paths) == 1:
        axes = axes.reshape(1, -1)
    
    for idx, img_path in enumerate(image_paths):
        # Load original
        img = cv2.imread(str(img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Enhanced
        enhanced = cv2.equalizeHist(gray)
        
        # Edges
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        edges = np.sqrt(sobelx**2 + sobely**2)
        # Prevent division by zero
        edges = np.uint8(edges / edges.max() * 255) if edges.max() > 0 else edges.astype(np.uint8)
        
        # Denoised
        denoised = cv2.medianBlur(gray, 5)
        
        # Plot
        axes[idx, 0].imshow(img_rgb)
        axes[idx, 0].set_title(f'Original\n{img_path.name}', fontsize=8)
        axes[idx, 0].axis('off')
        
        axes[idx, 1].imshow(gray, cmap='gray')
        axes[idx, 1].set_title('Grayscale', fontsize=8)
        axes[idx, 1].axis('off')
        
        axes[idx, 2].imshow(enhanced, cmap='gray')
        axes[idx, 2].set_title('Enhanced', fontsize=8)
        axes[idx, 2].axis('off')
        
        axes[idx, 3].imshow(edges, cmap='gray')
        axes[idx, 3].set_title('Edges', fontsize=8)
        axes[idx, 3].axis('off')
        
        axes[idx, 4].imshow(denoised, cmap='gray')
        axes[idx, 4].set_title('Denoised', fontsize=8)
        axes[idx, 4].axis('off')
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"\n📊 Visualization saved: {output_file}")
    plt.close()


def main():
    """Main function."""
    print("=" * 70)
    print("Bean Leaf Lesions Dataset - Image Processing Example")
    print("=" * 70)
    
    # Check if dataset exists
    if not check_dataset_exists():
        return
    
    print("\n🔍 Available disease categories:")
    print("  1. angular_leaf_spot - Angular leaf spot disease")
    print("  2. bean_rust - Bean rust disease")
    print("  3. healthy - Healthy bean leaves")
    
    # Get sample images from different categories
    categories = ["angular_leaf_spot", "bean_rust", "healthy"]
    all_samples = []
    
    for category in categories:
        print(f"\n📂 Getting samples from: {category}")
        samples = get_sample_images(category=category, split="train", max_images=2)
        
        if samples:
            print(f"  Found {len(samples)} sample images")
            all_samples.extend(samples)
        else:
            print(f"  ⚠️  No images found in this category")
    
    if not all_samples:
        print("\n❌ No images found to process!")
        print("   Please ensure the dataset is properly downloaded and extracted.")
        return
    
    # Process images
    output_dir = Path(__file__).parent / "bean_leaf_processed"
    print(f"\n🔄 Processing images...")
    print(f"📁 Output directory: {output_dir}")
    
    for img_path in all_samples:
        process_single_image(img_path, output_dir)
    
    # Create visualization
    print("\n📊 Creating visualization...")
    viz_file = output_dir / "processing_comparison.png"
    create_visualization(all_samples[:3], viz_file)
    
    print("\n" + "=" * 70)
    print("✅ Processing Complete!")
    print("=" * 70)
    print(f"\n📁 Processed images saved to: {output_dir}")
    print(f"📊 Visualization: {viz_file}")
    print("\n💡 Next steps:")
    print("   - Check the output directory for processed images")
    print("   - Open comprehensive_app.py for interactive processing")
    print("   - Experiment with different processing techniques")


if __name__ == "__main__":
    main()
