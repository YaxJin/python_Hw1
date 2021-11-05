import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def histogram_Equalization(img):
    img_array = np.array(img)
    hist,bins = np.histogram(img_array.ravel(),256,[0,255])
    pdf = hist/img_array.size
    cdf = pdf.cumsum()
    equ_value = np.around(cdf * 255).astype('uint8')
    result = equ_value[img_array]
    showResult(img_array,result)
    return

def showResult(img, result):
    plt.figure(figsize=(10,10))
    
    plt.subplot(2,2,1)
    plt.title("Original Image")
    plt.axis('off') 
    plt.imshow(Image.fromarray(np.uint8(img)))
    
    plt.subplot(2,2,2)
    plt.title("The Histrogram - Original Image")
    plt.hist(np.array(img).ravel(),bins=256,range=(0,255))
    
    plt.subplot(2,2,3)
    plt.title("After Equalization Image")
    plt.axis('off')
    plt.imshow(Image.fromarray(np.uint8(result)))
    
    plt.subplot(2,2,4)
    plt.title("The Histrogram - After Equalization Image")
    plt.hist(result.ravel(),bins=256,range=(0,255))
    plt.show()
    return

histogram_Equalization(Image.open('../HW1_test_image/Peppers.bmp').convert('L'))
histogram_Equalization(Image.open('../HW1_test_image/Jetplane.bmp').convert('L'))
histogram_Equalization(Image.open('../HW1_test_image/Lake.bmp').convert('L'))
