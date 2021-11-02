import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import scipy.ndimage.filters


def showResult(img,lap,after_transformation_image):
    plt.figure(figsize=(10,10))
    
    plt.subplot(1,3,1)
    plt.title("Original Image")
    plt.axis('off') 
    #plt.imshow(img)
    plt.imshow(abs(img), plt.cm.gray)
    
    plt.subplot(1,3,2)
    plt.title("Laplacian")
    plt.axis('off') 
    plt.imshow(abs(lap), plt.cm.gray)
    
    plt.subplot(1,3,3)
    plt.title("After Laplacian filtered Image")
    plt.axis('off') 
    plt.imshow(abs(after_transformation_image), plt.cm.gray)
    
    plt.show()
    return

img = Image.open('../HW1_test_image/Jetplane.bmp')
img_array = np.array(img)

img_array = (img_array - np.amin(img_array))*255.0 /(np.amax(img_array)-np.amin(img_array))
kernel = np.ones((3,3))*(1)
kernel[1,1] = -8
#kernel[0,1] = kernel[1,0] = kernel[1,2] = kernel[2,1] = 2
print("kernel:\n",kernel)
lap = scipy.ndimage.filters.convolve(img_array, kernel)

Sharpening_factor = 100
Laps = lap*Sharpening_factor/np.amax(lap) 
result = np.clip(img_array + Laps, 0, 255)

showResult(img_array,Laps,result)