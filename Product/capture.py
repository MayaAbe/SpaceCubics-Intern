
#!/usr/bin/python3

import time
from picamera2 import Picamera2, Preview
import parameters as param  # Assuming parameters.py contains common parameters


def capture_dng(output_filename="cap_dng.dng", metadata=param.metadata):
    picam2 = Picamera2()
    
    exposure = metadata["ExposureTime"]  # Read from parameters module
    gain = metadata["AnalogueGain"] * metadata["DigitalGain"]  # Read from parameters module

    controls = {"ExposureTime": exposure, "AnalogueGain": gain}
    capture_config = picam2.create_still_configuration(raw={}, display=None, controls=controls)

    picam2.configure(capture_config) #いらないかも
    picam2.start()
    time.sleep(2)

    r = picam2.switch_mode_capture_request_and_stop(capture_config)
    r.save_dng(output_filename)

    picam2.stop()


def capture_jpeg(output_filename="capture.jpg"):
    picam2 = Picamera2()

    preview_config = picam2.create_preview_configuration(main={"size": (800, 600)})
    picam2.configure(preview_config)

    picam2.start_preview(Preview.QTGL)
    picam2.start()
    time.sleep(2)

    metadata = picam2.capture_file(output_filename)
    print(metadata)

    picam2.close()


def capture_dng_jpeg(output_filename_dng="capture.dng", output_filename_jpeg="capture.jpg"):
    picam2 = Picamera2()

    exposure = param.metadata["ExposureTime"]  # Read from parameters module
    gain = param.metadata["AnalogueGain"] * param.metadata["DigitalGain"]  # Read from parameters module

    controls = {"ExposureTime": exposure, "AnalogueGain": gain}
    capture_config = picam2.create_still_configuration(raw={}, display=None, controls=controls)


    picam2.start()
    time.sleep(2)

    r = picam2.switch_mode_capture_request_and_stop(capture_config)
    r.save("main", output_filename_jpeg)
    
    r.save_dng(output_filename_dng)


if __name__ == "__main__":
    capture_dng_jpeg()
