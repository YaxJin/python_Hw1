import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
import scipy.ndimage.filters


def showResult(img,after_transformation_image):
    plt.figure(figsize=(10,10))
    
    plt.subplot(1,3,1)
    plt.title("Original Image")
    plt.axis('off') 
    plt.imshow(abs(img), plt.cm.gray)
    
    plt.subplot(1,3,2)
    plt.title("After Equalization Image")
    plt.axis('off') 
    plt.imshow(abs(after_transformation_image), plt.cm.gray)
    
    plt.subplot(1,3,3)
    plt.title("After Equalization Image")
    plt.axis('off') 
    plt.imshow(abs(after_transformation_image), plt.cm.gray)
    
    plt.show()
    return

# Reading of the image into numpy array:
A0           = scipy.misc.imread('../HW1_test_image/Peppers.bmp', flatten=True)
# Map values to the (0, 255) range:
A0           = (A0 - np.amin(A0))*255.0 /(np.amax(A0)-np.amin(A0)) 

# Kernel for negative Laplacian:
kernel      = np.ones((3,3))*(-1)
kernel[1,1] = 8

# Convolution of the image with the kernel:
Lap        = scipy.ndimage.filters.convolve(A0, kernel)

#Map Laplacian to some new range:
ShF         = 100                   #Sharpening factor!
Laps        = Lap*ShF/np.amax(Lap) 

# Add negative Laplacian to the original image:
A           = A0 + Laps 
# Set negative values to 0, values over 255 to 255:
A = np.clip(A, 0, 255)

# Image the result:
showResult(A,Laps)