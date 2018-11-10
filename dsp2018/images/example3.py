
import cv2
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg

img = cv2.imread('bookpage.jpg')
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#binarizar sobre la escala de gris
retval, threshold = cv2.threshold(grayscaled,9, 255, cv2.THRESH_BINARY)

#threshold = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 121, 1)

plt.subplot(2,1,1)
plt.imshow(img)
plt.subplot(2,1,2)
plt.imshow(threshold,cmap='gray')

plt.show()






