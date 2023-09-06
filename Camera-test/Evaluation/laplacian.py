import cv2

def laplacian_variance(image_path):
    # 画像を読み込む
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 画像が正常に読み込まれたか確認
    if image is None:
        print(f"Error: Could not open or find the image at {image_path}")
        return None

    # ラプラシアンフィルタを適用し、その分散を計算
    laplacian_var = cv2.Laplacian(image, cv2.CV_64F).var()
    return laplacian_var

if __name__ == "__main__":
    for i in range(1, 6):  # 1から5までの連番
        image_path = f'Camera-test\Evaluation\image{i}.jpg'  # 画像のパスを生成
        result = laplacian_variance(image_path)

        if result is not None:
            print(f"Laplacian Variance for the image at {image_path}: {result}")
