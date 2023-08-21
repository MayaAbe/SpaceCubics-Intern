import time
from datetime import datetime, timedelta, timezone
import os

import cv2
import numpy as np

from picamera2 import Picamera2
import parameters as param

# Simple Mertens merge with 3 exposures. No image alignment or anything fancy.
RATIO = 3.0

picam2 = Picamera2()
#picam2.configure(picam2.create_preview_configuration())
#picam2.start()

# Run for a second to get a reasonable "middle" exposure level.
time.sleep(1)
metadata = param.metadata #picam2.capture_metadata()

exposure_normal = metadata["ExposureTime"]
gain = metadata["AnalogueGain"] * metadata["DigitalGain"]
#picam2.stop()
print("Exposure is "+str(int(exposure_normal)))
print("Gain is "+str(gain))
print("AnalogueGain is "+str(metadata["AnalogueGain"]))
print("DigitalGain is "+str(metadata["DigitalGain"]))

controls = {"ExposureTime": exposure_normal, "AnalogueGain": gain}
print("control is "+ str(controls))
capture_config = picam2.create_preview_configuration(main={"size": (1024, 768),
                                                            "format": "RGB888"},
                                                    controls=controls)
picam2.configure(capture_config)
picam2.start()
normal = picam2.capture_array()
picam2.stop()

exposure_short = int(exposure_normal / RATIO)
picam2.set_controls({"ExposureTime": exposure_short, "AnalogueGain": gain})
picam2.start()
short = picam2.capture_array()
picam2.stop()

exposure_long = int(exposure_normal * RATIO)
picam2.set_controls({"ExposureTime": exposure_long, "AnalogueGain": gain})
picam2.start()
long = picam2.capture_array()
picam2.stop()

merge = cv2.createMergeMertens()
merged = merge.process([short, normal, long])
merged = np.clip(merged * 255, 0, 255).astype(np.uint8)

JP = timezone(timedelta(hours=+9), name='JP')
now = datetime.now(JP)
formatted_now = now.strftime("%m%d%H%M%S")  # mmddHHMMSS format

images_dir = './Images'
cv2.imwrite(os.path.join(images_dir, formatted_now+"short"+str(exposure_normal)+".jpg"), short)
cv2.imwrite(os.path.join(images_dir, formatted_now+"normal"+str(exposure_normal)+".jpg"), normal)
cv2.imwrite(os.path.join(images_dir, formatted_now+"long"+str(exposure_normal)+".jpg"), long)
cv2.imwrite(os.path.join(images_dir, formatted_now+"merged"+str(exposure_normal)+".jpg"), merged)
