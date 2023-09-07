from PIL import Image, ImageEnhance
import os

def enhance_brightness(image_path, factor):
    with Image.open(image_path) as img:
        enhancer = ImageEnhance.Brightness(img)
        img_enhanced = enhancer.enhance(factor)

        # 元のファイル名から拡張子を除いた部分を取得
        base_name, ext = os.path.splitext(os.path.basename(image_path))

        # 新しいファイル名を生成
        new_file_name = f"{base_name}_brighter{ext}"

        # 新しいファイル名で画像を保存
        new_file_path = os.path.join(os.path.dirname(image_path), new_file_name)
        img_enhanced.save(new_file_path)
        print(f"Saved as {new_file_name}")

if __name__ == "__main__":
    # スクリプトが存在するディレクトリのパスを取得
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # スクリプトが存在するディレクトリ内の全てのファイルをリストする
    files = os.listdir(script_directory)

    processed = False  # 画像が処理されたかどうかをチェックするフラグ

    # JPEGファイルだけを処理する
    for file in files:
        full_path = os.path.join(script_directory, file)
        if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg'):
            print(f"Processing {file}...")
            enhance_brightness(full_path, 2.0)  # 明るさを200%に変更
            processed = True

    if not processed:
        print("No JPEG files found for processing.")
