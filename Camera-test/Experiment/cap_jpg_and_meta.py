import time
from datetime import datetime, timedelta, timezone
import os
import cv2
import numpy as np
from picamera2 import Picamera2
import parameters as param

RATIO = 3.0

def get_next_image_index(directory):
    # Get list of files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Extract indices from filenames
    indices = []
    for f in files:
        if f.startswith("image") and f.endswith(".jpg"):
            try:
                index = int(f.split("image")[1].split(".jpg")[0])
                indices.append(index)
            except ValueError:
                continue
    
    # Get the next index
    if indices:
        return max(indices) + 1
    else:
        return 1

def save_image_and_metadata(directory, index, image, metadata):
    image_filename = os.path.join(directory, f"image{index}.jpg")
    metadata_filename = os.path.join(directory, f"image{index}.txt")
    
    cv2.imwrite(image_filename, image)
    with open(metadata_filename, 'w') as f:
        f.write(str(metadata))

picam2 = Picamera2()
time.sleep(1)
metadata = param.metadata 

exposure_normal = metadata["ExposureTime"]
gain = metadata["AnalogueGain"] * metadata["DigitalGain"]

controls = {"ExposureTime": exposure_normal, "AnalogueGain": gain}
capture_config = picam2.create_preview_configuration(main={"size": (1024, 768), "format": "RGB888"}, controls=controls)
picam2.configure(capture_config)
picam2.start()
normal = picam2.capture_array()
request = picam2.capture_request()
meta_normal = request.get_metadata()
picam2.stop()

exposure_short = int(exposure_normal / RATIO)
picam2.set_controls({"ExposureTime": exposure_short, "AnalogueGain": gain})
picam2.start()
short = picam2.capture_array()
request = picam2.capture_request()
meta_short = request.get_metadata()
picam2.stop()

exposure_long = int(exposure_normal * RATIO)
picam2.set_controls({"ExposureTime": exposure_long, "AnalogueGain": gain})
picam2.start()
long = picam2.capture_array()
request = picam2.capture_request()
meta_long = request.get_metadata()
picam2.stop()

merge = cv2.createMergeMertens()
merged = merge.process([short, normal, long])
merged = np.clip(merged * 255, 0, 255).astype(np.uint8)

images_dir = './Images'
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

# Get the next image index
index = get_next_image_index(images_dir)

# Save images and exposures
save_image_and_metadata(images_dir, index, short, meta_short)
save_image_and_metadata(images_dir, index + 1, normal, meta_normal)
save_image_and_metadata(images_dir, index + 2, long, meta_long)
save_image_and_metadata(images_dir, index + 3, merged, "merged")
