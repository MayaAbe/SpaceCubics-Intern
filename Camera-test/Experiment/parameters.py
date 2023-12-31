def update_metadata(metadata, key, new_value):
    if key in metadata:
        metadata[key] = new_value
        print(f"Updated {key} to {new_value}")
    else:
        print(f"Key {key} not found in metadata")

def check_metadata(metadata):
    print("-------------------------------")
    for key, value in metadata.items():
        print(f'{key}: {value}')
    print("-------------------------------")

metadata={ 
'ScalerCrop': (160, 0, 960, 720), 
'SensorBlackLevels': (2048, 2048, 2048, 2048), 
'ColourTemperature': 4500, 
'DigitalGain': 1.0, 
'ColourGains': (1.1795026063919067, 1.0574291944503784), 
'AeLocked': False, 
'Lux': 7597.48828125, 
'FrameDuration': 8330, 
'ColourCorrectionMatrix': (1.7592334747314453, -0.38649335503578186, -0.37275010347366333, 
                            -0.44978946447372437, 1.555491328239441, -0.10570189356803894, 
                            -0.1007557362318039, -0.46043145656585693, 1.5611871480941772), 
'SensorTimestamp': 7401520219000, 
'AnalogueGain': 1.0, 
'FocusFoM': 4766, 
'ExposureTime': 8000}
