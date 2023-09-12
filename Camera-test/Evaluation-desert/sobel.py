import cv2
import numpy as np

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

if __name__ == "__main__":
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
