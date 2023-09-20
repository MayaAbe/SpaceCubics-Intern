import parameters

parameters.check_metadata(parameters.metadata)
parameters.adjust_metadata(parameters.metadata, 'ColourTemperature', 5000)
parameters.check_metadata(parameters.metadata)


parameters.update_metadata('Product\parameters.py', 'ColourTemperature', 6000)
parameters.check_metadata(parameters.metadata)