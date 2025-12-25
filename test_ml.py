"""
Test suite for Machine Learning Image Processing Module
Tests all ML functions with sample images

Bài kiểm tra Machine Learning - Xử lý ảnh
"""

import numpy as np
import cv2
import os
from ml_processing import MLImageProcessor


def create_test_image():
    """Create a test image for ML testing"""
    # Create a 100x100 test image with shapes
    test_img = np.zeros((100, 100), dtype=np.uint8)
    
    # Add a circle
    cv2.circle(test_img, (50, 50), 30, 200, -1)
    
    # Add a rectangle
    cv2.rectangle(test_img, (10, 10), (30, 30), 100, -1)
    
    # Add some gradient background
    for i in range(100):
        for j in range(100):
            if test_img[i, j] == 0:
                test_img[i, j] = 50 + int(i * 0.3)
    
    return test_img


def test_kmeans_segmentation():
    """Test K-Means segmentation"""
    print("Testing K-Means Segmentation...")
    
    test_img = create_test_image()
    
    # Test with K=3
    segmented, centers = MLImageProcessor.kmeans_segmentation(test_img, k=3)
    
    assert segmented.shape == test_img.shape, "Output shape mismatch"
    assert len(centers) == 3, "Should have 3 cluster centers"
    assert segmented.dtype == np.uint8, "Output should be uint8"
    
    # Test with K=5
    segmented5, centers5 = MLImageProcessor.kmeans_segmentation(test_img, k=5)
    assert len(centers5) == 5, "Should have 5 cluster centers"
    
    print("  ✓ K-Means segmentation passed")


def test_feature_extraction():
    """Test feature extraction functions"""
    print("\nTesting Feature Extraction...")
    
    test_img = create_test_image()
    
    # Histogram features
    hist_features = MLImageProcessor.extract_histogram_features(test_img)
    assert hist_features.shape == (32,), f"Histogram features should be (32,), got {hist_features.shape}"
    assert np.isclose(hist_features.sum(), 1.0), "Histogram should be normalized"
    
    # Texture features
    texture_features = MLImageProcessor.extract_texture_features(test_img)
    assert texture_features.shape == (5,), f"Texture features should be (5,), got {texture_features.shape}"
    
    # Statistical features
    stat_features = MLImageProcessor.extract_statistical_features(test_img)
    assert stat_features.shape == (8,), f"Statistical features should be (8,), got {stat_features.shape}"
    
    # Combined features
    combined = MLImageProcessor.extract_combined_features(test_img)
    expected_size = 16 + 5 + 8  # 16 histogram + 5 texture + 8 statistical
    assert combined.shape == (expected_size,), f"Combined features should be ({expected_size},), got {combined.shape}"
    
    print("  ✓ Feature extraction passed")


def test_knn_classifier():
    """Test KNN classifier"""
    print("\nTesting KNN Classifier...")
    
    # Create simple training data
    train_features = np.array([
        [0, 0],
        [1, 0],
        [0, 1],
        [10, 10],
        [11, 10],
        [10, 11]
    ], dtype=np.float64)
    
    train_labels = np.array([0, 0, 0, 1, 1, 1])
    
    # Test point near class 0
    test_feature1 = np.array([0.5, 0.5])
    predicted1 = MLImageProcessor.knn_classify(train_features, train_labels, test_feature1, k=3)
    assert predicted1 == 0, f"Should predict class 0, got {predicted1}"
    
    # Test point near class 1
    test_feature2 = np.array([10.5, 10.5])
    predicted2 = MLImageProcessor.knn_classify(train_features, train_labels, test_feature2, k=3)
    assert predicted2 == 1, f"Should predict class 1, got {predicted2}"
    
    print("  ✓ KNN classifier passed")


def test_otsu_threshold():
    """Test Otsu thresholding"""
    print("\nTesting Otsu Thresholding...")
    
    test_img = create_test_image()
    
    binary, threshold = MLImageProcessor.otsu_threshold(test_img)
    
    assert binary.shape == test_img.shape, "Output shape mismatch"
    assert np.unique(binary).tolist() in [[0, 255], [0], [255]], "Should be binary image"
    assert 0 <= threshold <= 255, f"Threshold should be in [0, 255], got {threshold}"
    
    print(f"  - Optimal threshold: {threshold}")
    print("  ✓ Otsu thresholding passed")


def test_adaptive_threshold():
    """Test adaptive thresholding"""
    print("\nTesting Adaptive Thresholding...")
    
    test_img = create_test_image()
    
    binary = MLImageProcessor.adaptive_threshold_ml(test_img)
    
    assert binary.shape == test_img.shape, "Output shape mismatch"
    assert binary.dtype == np.uint8, "Output should be uint8"
    
    print("  ✓ Adaptive thresholding passed")


def test_ml_edge_detection():
    """Test ML edge detection"""
    print("\nTesting ML Edge Detection...")
    
    test_img = create_test_image()
    
    edges = MLImageProcessor.detect_edges_ml(test_img)
    
    assert edges.shape == test_img.shape, "Output shape mismatch"
    assert edges.dtype == np.uint8, "Output should be uint8"
    
    print("  ✓ ML edge detection passed")


def test_morphological_operations():
    """Test morphological operations"""
    print("\nTesting Morphological Operations...")
    
    # Create binary test image
    test_img = np.zeros((50, 50), dtype=np.uint8)
    cv2.circle(test_img, (25, 25), 15, 255, -1)
    
    # Test erosion
    eroded = MLImageProcessor.morphological_operations(test_img, 'erosion')
    assert eroded.shape == test_img.shape, "Erosion output shape mismatch"
    assert np.sum(eroded) < np.sum(test_img), "Eroded image should have fewer white pixels"
    
    # Test dilation
    dilated = MLImageProcessor.morphological_operations(test_img, 'dilation')
    assert np.sum(dilated) > np.sum(test_img), "Dilated image should have more white pixels"
    
    # Test opening
    opened = MLImageProcessor.morphological_operations(test_img, 'opening')
    assert opened.shape == test_img.shape, "Opening output shape mismatch"
    
    # Test closing
    closed = MLImageProcessor.morphological_operations(test_img, 'closing')
    assert closed.shape == test_img.shape, "Closing output shape mismatch"
    
    print("  ✓ Morphological operations passed")


def test_object_detection():
    """Test object detection"""
    print("\nTesting Object Detection...")
    
    # Create binary image with multiple objects
    test_img = np.zeros((100, 100), dtype=np.uint8)
    cv2.circle(test_img, (30, 30), 15, 255, -1)  # Object 1
    cv2.rectangle(test_img, (60, 60), (90, 90), 255, -1)  # Object 2
    
    labels, objects = MLImageProcessor.simple_object_detection(test_img, min_area=50)
    
    assert labels.shape == test_img.shape, "Labels shape mismatch"
    assert len(objects) == 2, f"Should detect 2 objects, got {len(objects)}"
    
    for obj in objects:
        assert 'area' in obj, "Object should have 'area'"
        assert 'centroid_x' in obj, "Object should have 'centroid_x'"
        assert 'centroid_y' in obj, "Object should have 'centroid_y'"
        print(f"  - Object {obj['label']}: area={obj['area']}, centroid=({obj['centroid_x']:.1f}, {obj['centroid_y']:.1f})")
    
    print("  ✓ Object detection passed")


def test_pca_reduce():
    """Test PCA dimensionality reduction"""
    print("\nTesting PCA Reduction...")
    
    # Create multiple test images
    n_samples = 5
    height, width = 32, 32
    images = np.random.randint(0, 256, (n_samples, height, width), dtype=np.uint8)
    
    reduced, components, mean_img = MLImageProcessor.pca_reduce(images, n_components=3)
    
    assert reduced.shape == (n_samples, 3), f"Reduced should be (5, 3), got {reduced.shape}"
    assert mean_img.shape == (height * width,), f"Mean image shape mismatch"
    
    print(f"  - Reduced from {height*width} to 3 dimensions")
    print("  ✓ PCA reduction passed")


def run_all_tests():
    """Run all ML tests"""
    print("\n" + "=" * 50)
    print("Machine Learning Image Processing Test Suite")
    print("=" * 50)
    
    test_kmeans_segmentation()
    test_feature_extraction()
    test_knn_classifier()
    test_otsu_threshold()
    test_adaptive_threshold()
    test_ml_edge_detection()
    test_morphological_operations()
    test_object_detection()
    test_pca_reduce()
    
    print("\n" + "=" * 50)
    print("All ML tests passed successfully!")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    run_all_tests()
