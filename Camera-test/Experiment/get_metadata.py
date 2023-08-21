from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start()

#metadataは辞書型らしい
metadata = picam2.capture_metadata()

#辞書型の中身をループさせて全部表示させる
print("-------------------------------")

for key, value in metadata.items():
    print(f'{key}: {value}')

print("-------------------------------")