from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start()

# metadata method retuns dictionary type
metadata = picam2.capture_metadata()

# Roop and get metadata
print("-------------------------------")

for key, value in metadata.items():
    print(f"{key}: {value}")

print("-------------------------------")
