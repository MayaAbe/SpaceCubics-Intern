import pyexiv2

IMG_PATH = "Camera-test\Experiment\cap_dng_jpg0.jpg"

def exif_read(path = ""):
    with pyexiv2.Image(path) as img:
        data = img.read_exif()
        print("----------------")
        print(type(data))
        for key, value in data.items():
            print(f'{key}: {value}')
        print("----------------")

def xmp_read(path = ""):
    with pyexiv2.Image(path) as img:
        data = img.read_xmp()
        print("----------------")
        print(type(data))
        for key, value in data.items():
            print(f'{key}: {value}')
        print("----------------")

def xmp_write(path="", tag="", data=""):
    if tag=="":
        pass
    else:
        img.modify_xmp({'Xmp.dc.mytag1': 'Hello'})

def xmp_delete(path=""):
    key = input("Are you sure to delete all xmp data? (y/n): ")
    if key =="y":
        with pyexiv2.Image(path) as img:
            img.clear_xmp()
    else:
        pass

if __name__=="__main__":
    xmp_delete(IMG_PATH)
    exif_read(IMG_PATH)
    xmp_read(IMG_PATH)