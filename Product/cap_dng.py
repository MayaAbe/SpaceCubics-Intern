#!/usr/bin/python3

import parameters as param
import time
from picamera2 import Picamera2


def capture_dng(output_filename="cap_dng_jpg(.dng)", metadata=param.metadata):
    picam2 = Picamera2()

    exposure = metadata["ExposureTime"]  # Read from parameters module
    gain = metadata["AnalogueGain"] * metadata["DigitalGain"]  # Read from parameters module

    controls = {"ExposureTime": exposure, "AnalogueGain": gain}
    capture_config = picam2.create_still_configuration(raw={}, display=None, controls=controls)

    picam2.start()
    time.sleep(2)

    r = picam2.switch_mode_capture_request_and_stop(capture_config)
    r.save_dng("./ImageDNG/"+output_filename + ".dng")

    picam2.stop()


if __name__ == "__main__":
    capture_dng("image_test")