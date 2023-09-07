import cv2
import numpy as np

def analyze_image(image_path):
    # 画像を読み込む
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 画像が正常に読み込まれたか確認
    if image is None:
        print(f"Error: Could not open or find the image at {image_path}")
        return None

    # 画像のヒストグラムを計算
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])
    return hist

if __name__ == "__main__":
    for i in range(1, 6):  # 1から5までの連番
        print(f"\nimage number: {i}")
        image_path = f'Camera-test\Evaluation\image{i}.jpg'  # 画像のパスを正確に指定
        histogram = analyze_image(image_path)

        if histogram is not None:
            print("Histogram:", histogram)
