#!/usr/bin/env python3
"""
Quick Start Script for Image Processing Application
Khởi động nhanh ứng dụng xử lý ảnh
"""

import sys
import subprocess

def main():
    """Main function to display menu and launch app"""
    
    print("=" * 60)
    print("  ỨNG DỤNG XỬ LÝ ẢNH - IMAGE PROCESSING APPLICATION")
    print("=" * 60)
    print()
    print("Chọn ứng dụng muốn chạy / Select application to run:")
    print()
    print("1. Comprehensive App (Bài 1-11) - KHUYẾN NGHỊ / RECOMMENDED ⭐")
    print("   Tích hợp đầy đủ tất cả chức năng")
    print()
    print("2. Basic Conversions App (Bài 1-3)")
    print("   Chuyển đổi cơ bản: xám, nhị phân, tách kênh")
    print()
    print("3. Advanced Processing App (Bài 4-9)")
    print("   Contrast, histogram, filters, edge detection")
    print()
    print("4. Exit / Thoát")
    print()
    
    choice = input("Nhập lựa chọn (1-4) / Enter choice (1-4): ").strip()
    
    if choice == '1':
        print("\nKhởi động Comprehensive App...")
        print("Starting Comprehensive App...")
        subprocess.run([sys.executable, "comprehensive_app.py"])
    elif choice == '2':
        print("\nKhởi động Basic Conversions App...")
        print("Starting Basic Conversions App...")
        subprocess.run([sys.executable, "image_processing_app.py"])
    elif choice == '3':
        print("\nKhởi động Advanced Processing App...")
        print("Starting Advanced Processing App...")
        subprocess.run([sys.executable, "main.py"])
    elif choice == '4':
        print("\nTạm biệt! / Goodbye!")
        sys.exit(0)
    else:
        print("\nLựa chọn không hợp lệ! / Invalid choice!")
        sys.exit(1)

if __name__ == "__main__":
    main()
