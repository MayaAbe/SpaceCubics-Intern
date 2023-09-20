from PIL import Image
import os
import exifrw

# 画像内の各ピクセルを二値化（白または黒）にする関数。白いピクセルの数も計算します。
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


# 白いピクセルの比率を計算する関数。
def calculate_white_ratio(white_pixels, total_pixels):
    return (white_pixels / total_pixels) * 100  # 白いピクセルの割合を計算


def save_image(img, path):
    img.save(path)


#def binalize_xmp():
    #./Product/ImageJPG/にある画像を全て取得
    #exifrw.pyのxmp_readを使って，全ての画像のxmpを読み込む
    #xmpの中に"BinalizedWhiteRate"タグがない画像を見つける
    #その画像をbinalize_pixelsで二値化し，calculate_white_ratioで白いピクセルの割合を計算
    #白いピクセルの割合を"BinalizedWhiteRate"タグに書き込む
    #"BinalizedWhiteRate"タグがない画像全てに対して上記の処理を行う
    #xmpの中に"BinalizedWhiteRate"タグがある画像は処理しない


# ディレクトリ内の画像を2値化してタグ付けする新機能
def binarize_xmp(directory_path='./ImageJPG', tag_name='Binalized'):
    import os
    import pyexiv2
    from PIL import Image

    # ディレクトリ内のすべてのJPEGファイルをループする
    for filename in sorted(os.listdir(directory_path)):
        if filename.endswith('.jpg'):
            file_path = os.path.join(directory_path, filename)
            
            # 画像からXMPデータを読み込む
            with pyexiv2.Image(file_path) as img:
                xmp_data = img.read_xmp()
                
                # 画像にすでに'Binalized'タグが付けられているかチェックする
                if tag_name not in xmp_data:
                    # PILを使って画像を開く
                    img_pil = Image.open(file_path)
                    
                    # 二値化の実行
                    bin_img, white_pixels = binarize_pixels(img_pil)
                    
                    # 白画素の比率を計算する
                    width, height = bin_img.size
                    total_pixels = width * height
                    white_ratio = calculate_white_ratio(white_pixels, total_pixels)
                    
                    # 二値化した画像を同じパスに保存する
                    #bin_img.save(file_path)
                    
                    # 新しいXMPタグを書き込む
                    with pyexiv2.Image(file_path) as img:
                        img.modify_xmp({tag_name: str(white_ratio)})


if __name__ == "__main__":
    binarize_xmp("Product\ImageJPG")
    
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
