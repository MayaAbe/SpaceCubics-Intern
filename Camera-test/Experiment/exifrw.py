import pyexiv2

IMG_PATH = "Camera-test\Experiment\cap_dng_jpg0.dng"


def exif_read(path=""):
    with pyexiv2.Image(path) as img:
        data = img.read_exif()
        print("----------------")
        print(type(data))
        for key, value in data.items():
            print(f'{key}: {value}')
        print("----------------")


def xmp_read(path=""):
    with pyexiv2.Image(path) as img:
        data = img.read_xmp()
        print("----------------")
        print(type(data))
        for key, value in data.items():
            print(f'{key}: {value}')
        print("----------------")


def show_available_namespace(path=""):
    with pyexiv2.Image(path) as img:
        data = img.read_xmp()
        print("----------------")
        print(type(data))
        for key, value in data.items():
            print(f'{key}: {value}')
        print("----------------")

def xmp_write(path="", tag="", data=""):
    img = pyexiv2.Image(path)
    if tag == "":
        pass
    else:
        img.modify_xmp({tag: data})


def xmp_delete(path=""):
    key = input("Are you sure to delete all xmp data? (y/n): ")
    if key == "y":
        with pyexiv2.Image(path) as img:
            img.clear_xmp()
    else:
        pass


if __name__ == "__main__":
    xmp_delete(IMG_PATH)
    exif_read(IMG_PATH)
    xmp_read(IMG_PATH)