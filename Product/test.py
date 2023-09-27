import sobel
import file
import exifrw

if __name__ == "__main__":
    exifrw.xmp_read('./ImageJPG/image1.jpg')
    file.loop_in_directory(sobel.sobel_xmp, './ImageJPG')