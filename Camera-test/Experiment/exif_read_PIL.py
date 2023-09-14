from PIL import Image, ImageTk          # Pillow
from PIL.ExifTags import TAGS, GPSTAGS  # Exifタグ情報
from pyexif import ExifEditor

# 画像の取得
image1 = Image.open("Camera-test\Experiment\cap_dng_jpg0.jpg")

# Exif情報の取得
exif_dict = image1.getexif()
exif = [TAGS.get(k, "Unknown")+ f": {str(v)}" for k, v in exif_dict.items()]
exif_str = "\n".join(exif)

print(exif_str)