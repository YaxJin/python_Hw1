from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def powerlaw(img,gamma):
    img_array = np.array(img)
    im_gamma = img_array ** gamma
    showResult(img,Image.fromarray(np.uint8(np.clip(im_gamma, 0, 255))))
    return


def showResult(img,after_transformation_image):
    plt.figure(figsize=(10,10))
    
    plt.subplot(1,2,1)
    plt.title("Original Image")
    plt.axis('off') 
    plt.imshow(img)
    
    plt.subplot(1,2,2)
    plt.title("After Equalization Image")
    plt.axis('off') 
    plt.imshow(after_transformation_image)
    
    plt.show()
    return


powerlaw(Image.open('../HW1_test_image/Peppers.bmp').convert('RGB'),0.85)
powerlaw(Image.open('../HW1_test_image/Jetplane.bmp').convert('RGB'),0.95)
powerlaw(Image.open('../HW1_test_image/Lake.bmp').convert('RGB'),1.1)
