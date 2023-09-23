from PIL import Image
import os

def binarize_pixels(img, threshold=30):
    pixels = img.load()  # ピクセルデータをロード
    white_pixels = 0
    width, height = img.size  # 画像のサイズ
    for x in range(width):
        for y in range(height):
            if pixels[x, y] <= threshold:
                pixels[x, y] = 0  # 黒にする
            else:
                pixels[x, y] = 255  # 白にする
                white_pixels += 1  # 白いピクセルの数をカウント
    return img, white_pixels

def calculate_white_ratio(white_pixels, total_pixels):
    return (white_pixels / total_pixels) * 100  # 白いピクセルの割合を計算

def save_image(img, path):
    img.save(path)

if __name__ == "__main__":
    # スクリプトが存在するディレクトリのパスを取得
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # スクリプトが存在するディレクトリ内の全てのファイルをリストする
    files = os.listdir(script_directory)

    processed = False  # 画像が処理されたかどうかをチェックするフラグ

    for file in files:
        full_path = os.path.join(script_directory, file)
        if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg') or file.lower().endswith('.png'):
            print(f"Processing {file}...")

            with Image.open(full_path).convert("L") as img:
                width, height = img.size  # 画像のサイズ
                total_pixels = width * height  # 全ピクセル数を計算

                # 画像を二値化
                processed_img, white_pixels = binarize_pixels(img, threshold=30)

                # 白いピクセルの割合を計算
                white_ratio = calculate_white_ratio(white_pixels, total_pixels)

                # 新しいファイル名を生成
                base_name, ext = os.path.splitext(file)
                new_file_name = f"{base_name}_binarize{ext}"

                # 処理した画像を保存
                save_image(processed_img, new_file_name)

                print(f"Saved as {new_file_name}")
                print(f"White pixel ratio: {white_ratio:.2f}%")

            processed = True

    if not processed:
        print("No suitable image files found for processing.")
