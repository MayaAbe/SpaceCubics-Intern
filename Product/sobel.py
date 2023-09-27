import os
import cv2
import numpy as np
from exifrw import xmp_write

def sobel_variance(image_path):
    # 画像を読み込む
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 画像が正常に読み込まれたか確認
    if image is None:
        print(f"Error: Could not open or find the image at {image_path}")
        return None

    # Sobelフィルタを適用
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # 分散を計算
    sobel_var = np.var(sobelx) + np.var(sobely)
    return sobel_var


def sobel_xmp(directory_path='./ImageJPG'):
    # List all files in the directory
    file_list = os.listdir(directory_path)

    # Filter out non-jpg files
    jpg_files = [f for f in file_list if f.lower().endswith('.jpg')]

    if not jpg_files:
        print("No jpg images found in the directory.")
        return

    # Process each jpg file
    for filename in jpg_files:
        file_path = os.path.join(directory_path, filename)

        # Read the image
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

        # Check if image is loaded correctly
        if image is None:
            print(f"Error: Could not open or find the image at {file_path}")
            continue

        # Apply Sobel filter and calculate variance
        sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
        sobel_var = np.var(sobelx) + np.var(sobely)

        # Write the Sobel variance to the XMP with the tag "SobelFilterResult"
        xmp_write(file_path, "SobelFilterResult", str(sobel_var))

        # Feedback
        print(f"Processed {filename} with Sobel Variance: {sobel_var}")



if __name__ == "__main__":
    sobel_xmp("./ImageJPG")


"""
    import time

    start_time = time.time()
    for x in range(100):
        for i in range(1, 5):  # 1から5までの連番
            image_path = f'Camera-test\Evaluation-desert\iss{i}.jpg'  # 画像のパスを生成
            result = sobel_variance(image_path)

            if result is not None:
                print(f"Sobel Variance for the image at {image_path}: {result}")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"実行時間: {elapsed_time} 秒")
"""