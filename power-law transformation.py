from PIL import Image
import numpy as np

def powerlaw(img,gamma):
    img_array = np.array(img)
    im_gamma = img_array ** gamma
    final = combine(img, Image.fromarray(np.uint8(im_gamma)))
    final.show()
    return

def combine(oringImg, translateImg):
    dst = Image.new('RGB', (512, 256))
    dst.paste(oringImg, (0, 0))
    dst.paste(translateImg, (256, 0))
    return dst


powerlaw(Image.open('../HW1_test_image/Peppers.bmp').convert('RGB'),0.85)
powerlaw(Image.open('../HW1_test_image/Jetplane.bmp').convert('RGB'),0.97)
powerlaw(Image.open('../HW1_test_image/Lake.bmp').convert('RGB'),1.03)
