import parameters
import cap_dng_jpg as dngjpg
import exifrw

FILENAME = "A"

key1 = input("Do you watch params? (y/n):")
if key1 == "y":
    parameters.check_metadata(parameters.metadata)

key2 = input("Do you change params? (y/n):")
if key2 == "y":
    key2_1 = input("Which parameters?: ")
    key2_2 = input("New parameters?: ")
    parameters.update_metadata(parameters.metadata, key2_1, key2_2)

key3 = input("Do you take photo? ( jpg-> j / dng-> d / no-> n ): ")
while True:
    if key3 == "j":
        pass
    if key3 == "d":
        dngjpg.capture_dng(FILENAME, parameters.metadata)
    if key3 == "n":
        break
    else:
        print("type again")
        pass



key4 = input("enter pass to check metadata for photo:")
print("EXIF data is ...")
exifrw.exif_read(key4)

print("")
