# metadata list
ScalerCrop = (160, 0, 960, 720)
SensorBlackLevels = (2048, 2048, 2048, 2048)
ColourTemperature = 4500
DigitalGain = 1.0
ColourGains = (1.1795026063919067, 1.0574291944503784)
AeLocked = False
Lux = 7597.48828125
FrameDuration = 8330
ColourCorrectionMatrix = (1.7592334747314453, -0.38649335503578186, -0.37275010347366333,
                          -0.44978946447372437, 1.555491328239441, -0.10570189356803894,
                          -0.1007557362318039, -0.46043145656585693, 1.5611871480941772)
SensorTimestamp = 7401520219000
AnalogueGain = 1.0
FocusFoM = 4766
ExposureTime = 8000


metadata = {
    'ScalerCrop': ScalerCrop,
    'SensorBlackLevels': SensorBlackLevels,
    'ColourTemperature': ColourTemperature,
    'DigitalGain': DigitalGain,
    'ColourGains': ColourGains,
    'AeLocked': AeLocked,
    'Lux': Lux,
    'FrameDuration': FrameDuration,
    'ColourCorrectionMatrix': ColourCorrectionMatrix,
    'SensorTimestamp': SensorTimestamp,
    'AnalogueGain': AnalogueGain,
    'FocusFoM': FocusFoM,
    'ExposureTime': ExposureTime
}


def check_metadata(metadata: dict):
    print("-------------------------------")
    for key, value in metadata.items():
        print(f'{key}: {value}')
    print("-------------------------------")


def adjust_metadata(metadata: dict, key, new_value):
    if key in metadata:
        metadata[key] = new_value
        print(f"Adjust {key} to {new_value}")
    else:
        print(f"Key {key} not found in metadata")


def update_metadata(metadata: dict, key, new_value, file_path="parameters.py"):
    if key in metadata:
        metadata[key] = new_value
        print(f"Updated {key} to {new_value}")
        
        # ファイルに保存
        with open(file_path, 'r', encoding="utf-8") as f:
            lines = f.readlines()
        
        with open(file_path, 'w') as f:
            for line in lines:
                if line.strip().startswith(f"{key}:"):
                    f.write(f"'{key}': {new_value},\n")
                else:
                    f.write(line)
        
        print(f"Saved {key} to {new_value} in {file_path}")
        
    else:
        print(f"Key {key} not found in metadata")


def describe_metadata(metadata):
    description = {}
    for key, value in metadata.items():
        description[key] = {'value': value, 'type': type(value).__name__}
        print(f"{key}:\n  Value: {value}\n  Type: {type(value).__name__}\n")


if __name__ == "__main__":
    print(describe_metadata(metadata))
