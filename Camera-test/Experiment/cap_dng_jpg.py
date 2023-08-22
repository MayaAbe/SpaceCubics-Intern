#!/usr/bin/python3

import time
from picamera2 import Picamera2, Preview

def capture_dng(output_filename="cap_dng_jpg.dng"):
    picam2 = Picamera2()

    exposure = 8000
    gain = 1

    controls = {"ExposureTime": exposure, "AnalogueGain": gain}
    capture_config = picam2.create_still_configuration(raw={}, display=None, controls=controls)

    picam2.start()
    time.sleep(2)

    r = picam2.switch_mode_capture_request_and_stop(capture_config)
    r.save_dng(output_filename)

if __name__ == "__main__":
    capture_dng()
