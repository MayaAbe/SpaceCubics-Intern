import parameters

key1 = input("Do you watch params? (y/n):")
if key1 == "y":
    parameters.check_metadata(parameters.metadata)

key2 = input("Do you change params? (y/n):")
if key2 == "y":
    key2_1 = input("Which parameters?: ")
    key2_2 = input("New parameters?: ")
    parameters.update_metadata(parameters.metadata, key2_1, key2_2)

