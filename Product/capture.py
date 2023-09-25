#!/usr/bin/python3

import time
from picamera2 import Picamera2
import parameters as param  # Assuming parameters.py contains common parameters
import file


def capture_dng_jpeg(output_filename="image0"):
    picam2 = Picamera2()

    exposure = param.metadata["ExposureTime"]  # Read from parameters module
    gain = param.metadata["AnalogueGain"] * param.metadata["DigitalGain"]  # Read from parameters module

    controls = {"ExposureTime": exposure, "AnalogueGain": gain}
    capture_config = picam2.create_still_configuration(raw={}, display=None, controls=controls)

    picam2.start()
    time.sleep(2)

    r = picam2.switch_mode_capture_request_and_stop(capture_config)
    r.save("main", output_filename+".jpg")
    r.save_dng(output_filename+".dng")

    picam2.stop()

def capture_dng(output_filename="cap_dng.dng", metadata=param.metadata):
    picam2 = Picamera2()

    exposure = metadata["ExposureTime"]  # Read from parameters module
    gain = metadata["AnalogueGain"] * metadata["DigitalGain"]  # Read from parameters module

    controls = {"ExposureTime": exposure, "AnalogueGain": gain}
    capture_config = picam2.create_still_configuration(raw={}, display=None, controls=controls)

    picam2.start()
    time.sleep(2)

    r = picam2.switch_mode_capture_request_and_stop(capture_config)
    r.save_dng(output_filename)

    picam2.stop()
    time.sleep(2)


def capture_jpeg(output_filename="cap_jpg.jpg", metadata=param.metadata):
    picam2 = Picamera2()

    exposure = metadata["ExposureTime"]  # Read from parameters module
    gain = metadata["AnalogueGain"] * metadata["DigitalGain"]  # Read from parameters module

    controls = {"ExposureTime": exposure, "AnalogueGain": gain}
    capture_config = picam2.create_still_configuration(raw={}, display=None, controls=controls)

    picam2.configure(capture_config)  # いらないかも
    picam2.start()
    time.sleep(2)

    r = picam2.switch_mode_capture_request_and_stop(capture_config)
    r.save("main", output_filename)

    picam2.stop()
    time.sleep(2)


if __name__ == "__main__":
    capture_dng_jpeg(file.get_name())
