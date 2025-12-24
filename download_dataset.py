#!/usr/bin/env python3
"""
Script to download Bean Leaf Lesions Classification dataset from Kaggle.

Requirements:
    - kaggle package installed: pip install kaggle
    - Kaggle API credentials configured (~/.kaggle/kaggle.json)

Usage:
    python download_dataset.py
"""

import os
import sys
import subprocess
import zipfile
from pathlib import Path


def check_kaggle_installed():
    """Check if kaggle package is installed."""
    try:
        import kaggle
        print("✓ Kaggle package is installed")
        return True
    except ImportError:
        print("✗ Kaggle package is not installed")
        print("  Install it with: pip install kaggle")
        return False


def check_kaggle_credentials():
    """Check if Kaggle credentials are configured."""
    kaggle_dir = Path.home() / '.kaggle'
    kaggle_json = kaggle_dir / 'kaggle.json'
    
    if kaggle_json.exists():
        print("✓ Kaggle credentials found")
        return True
    else:
        print("✗ Kaggle credentials not found")
        print("  Please set up your Kaggle API credentials:")
        print("  1. Go to https://www.kaggle.com/account")
        print("  2. Click 'Create New API Token'")
        print("  3. Place kaggle.json in ~/.kaggle/")
        print("  4. Run: chmod 600 ~/.kaggle/kaggle.json")
        return False


def download_dataset():
    """Download the Bean Leaf Lesions Classification dataset."""
    dataset_name = "marquis03/bean-leaf-lesions-classification"
    download_dir = Path(__file__).parent / "data" / "bean-leaf-lesions"
    
    # Create directory if it doesn't exist
    download_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n📦 Downloading dataset: {dataset_name}")
    print(f"📂 Download directory: {download_dir}")
    
    try:
        # Change to download directory
        original_dir = os.getcwd()
        os.chdir(download_dir)
        
        # Download using kaggle API
        cmd = ["kaggle", "datasets", "download", "-d", dataset_name]
        print(f"\n🔄 Running: {' '.join(cmd)}")
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✓ Download completed successfully")
            
            # Find the downloaded zip file
            zip_files = list(download_dir.glob("*.zip"))
            if zip_files:
                zip_file = zip_files[0]
                print(f"\n📦 Extracting {zip_file.name}...")
                
                with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                    zip_ref.extractall(download_dir)
                
                print("✓ Extraction completed")
                
                # Optionally remove the zip file
                print(f"\n🗑️  Removing zip file...")
                zip_file.unlink()
                print("✓ Cleanup completed")
                
                # List the extracted contents
                print("\n📁 Dataset structure:")
                for item in sorted(download_dir.iterdir()):
                    if item.is_dir():
                        print(f"  📂 {item.name}/")
                        # Show subdirectories
                        for subitem in sorted(item.iterdir())[:5]:
                            if subitem.is_dir():
                                file_count = len(list(subitem.glob("*")))
                                print(f"     📂 {subitem.name}/ ({file_count} files)")
                        if len(list(item.iterdir())) > 5:
                            print(f"     ... and {len(list(item.iterdir())) - 5} more")
                    else:
                        print(f"  📄 {item.name}")
                
                print("\n✅ Dataset ready to use!")
                return True
            else:
                print("✗ No zip file found after download")
                return False
        else:
            print("✗ Download failed")
            print(f"Error: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"✗ Error during download: {e}")
        return False
    finally:
        os.chdir(original_dir)


def main():
    """Main function."""
    print("=" * 60)
    print("Bean Leaf Lesions Classification Dataset Downloader")
    print("=" * 60)
    
    # Check prerequisites
    print("\n🔍 Checking prerequisites...")
    
    if not check_kaggle_installed():
        sys.exit(1)
    
    if not check_kaggle_credentials():
        sys.exit(1)
    
    # Download dataset
    success = download_dataset()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ SUCCESS! Dataset is ready to use.")
        print("=" * 60)
        print("\n📖 Next steps:")
        print("  1. Check data/bean-leaf-lesions/ directory")
        print("  2. Run: python comprehensive_app.py")
        print("  3. Load images from the dataset for processing")
        sys.exit(0)
    else:
        print("\n" + "=" * 60)
        print("❌ FAILED! Please check the errors above.")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    main()
