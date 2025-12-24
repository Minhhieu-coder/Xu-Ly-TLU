# Dataset Directory

This directory contains datasets used for image processing and classification tasks.

## Bean Leaf Lesions Classification Dataset

### Source
- **Kaggle Dataset**: [Bean Leaf Lesions Classification](https://www.kaggle.com/datasets/marquis03/bean-leaf-lesions-classification)
- **Author**: marquis03

### Description
This dataset contains images of bean leaves with various types of lesions for classification purposes. It is useful for:
- Plant disease detection
- Image classification tasks
- Computer vision research
- Agricultural AI applications

### How to Download

#### Method 1: Using Kaggle API (Recommended)

1. Install Kaggle API:
   ```bash
   pip install kaggle
   ```

2. Set up Kaggle credentials:
   - Go to [Kaggle Account Settings](https://www.kaggle.com/account)
   - Click "Create New API Token" to download `kaggle.json`
   - Place the file in `~/.kaggle/kaggle.json` (Linux/Mac) or `C:\Users\<Username>\.kaggle\kaggle.json` (Windows)
   - Set permissions: `chmod 600 ~/.kaggle/kaggle.json`

3. Download the dataset:
   ```bash
   cd data/bean-leaf-lesions
   kaggle datasets download -d marquis03/bean-leaf-lesions-classification
   unzip bean-leaf-lesions-classification.zip
   rm bean-leaf-lesions-classification.zip  # Optional: remove zip after extraction
   ```

#### Method 2: Manual Download

1. Visit [https://www.kaggle.com/datasets/marquis03/bean-leaf-lesions-classification](https://www.kaggle.com/datasets/marquis03/bean-leaf-lesions-classification)
2. Click "Download" button (requires Kaggle account)
3. Extract the zip file to `data/bean-leaf-lesions/`

### Dataset Structure

After downloading and extracting, the directory structure should be:
```
data/
└── bean-leaf-lesions/
    ├── README.md (this file)
    ├── train/
    │   ├── angular_leaf_spot/
    │   ├── bean_rust/
    │   └── healthy/
    ├── test/
    │   ├── angular_leaf_spot/
    │   ├── bean_rust/
    │   └── healthy/
    └── validation/
        ├── angular_leaf_spot/
        ├── bean_rust/
        └── healthy/
```

### Usage with This Project

Once downloaded, you can use the dataset with the image processing tools in this repository:

```python
# Example: Process bean leaf images
from comprehensive_app import *
import cv2
import os

# Load an image from the dataset
image_path = 'data/bean-leaf-lesions/train/angular_leaf_spot/image_001.jpg'
img = cv2.imread(image_path)

# Apply various processing techniques
# ... (use the tools from comprehensive_app.py)
```

### Notes

- The actual dataset files are not included in this repository due to size constraints
- Make sure to download the dataset before running any scripts that depend on it
- The dataset is for educational and research purposes
- Please respect the original dataset license and terms of use

### Citation

If you use this dataset in your research or project, please cite:
```
Bean Leaf Lesions Classification Dataset
Available at: https://www.kaggle.com/datasets/marquis03/bean-leaf-lesions-classification
Author: marquis03
```
