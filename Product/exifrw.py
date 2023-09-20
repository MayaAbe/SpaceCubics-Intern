import pyexiv2

IMG_PATH = "Product\ImageJPG\image1.jpg"


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


def xmp_get_dict(path=""):
    with pyexiv2.Image(path) as img:
        data = img.read_xmp()
        return data


def xmp_write(path="", tag="", data=""):
    pyexiv2.registerNs("namespace for scsat1-rpi","sc1")
    img = pyexiv2.Image(path)
    if tag == "":
        pass
    else:
        tag = "Xmp.sc1." + tag
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
    # xmp_write(IMG_PATH, "BinalizedWhiteRate", "100"); xmp_read(IMG_PATH)