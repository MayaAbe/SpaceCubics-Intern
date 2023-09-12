from PIL import Image
import os

def binarize_image(image_path, threshold=30):
    white_pixels = 0  # 白いピクセルの数
    total_pixels = 0  # 全ピクセル数

    with Image.open(image_path).convert("L") as img:  # "L"はグレースケールモード
        pixels = img.load()  # ピクセルデータをロード
        width, height = img.size  # 画像のサイズ

        total_pixels = width * height  # 全ピクセル数を計算

        # 各ピクセルを処理
        for x in range(width):
            for y in range(height):
                if pixels[x, y] <= threshold:
                    pixels[x, y] = 0  # 黒にする
                else:
                    pixels[x, y] = 255  # 白にする
                    white_pixels += 1  # 白いピクセルの数をカウント

        # 白いピクセルが占める割合を計算
        white_ratio = (white_pixels / total_pixels) * 100

        return img, white_ratio  # 二値化後の画像オブジェクトと白いピクセルの割合を返す

if __name__ == "__main__":
    # スクリプトが存在するディレクトリのパスを取得
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # スクリプトが存在するディレクトリ内の全てのファイルをリストする
    files = os.listdir(script_directory)

    processed = False  # 画像が処理されたかどうかをチェックするフラグ

    # グレースケール画像だけを処理する
    for file in files:
        full_path = os.path.join(script_directory, file)
        if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg') or file.lower().endswith('.png'):
            print(f"Processing {file}...")
            processed_img, white_ratio = binarize_image(full_path, threshold=10)  # 画像を二値化

            # 新しいファイル名を生成
            base_name, ext = os.path.splitext(file)
            new_file_name = f"{base_name}_binarize{ext}"

            # 処理した画像を保存
            processed_img.save(new_file_name)
            print(f"Saved as {new_file_name}")
            print(f"White pixel ratio: {white_ratio:.2f}%")

            processed = True

    if not processed:
        print("No suitable image files found for processing.")
