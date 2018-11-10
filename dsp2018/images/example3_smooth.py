
import cv2
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg

img = cv2.imread('bookpage.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)
#gray = cv2.GaussianBlur(gray,(5,5),0)


thr = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 1)

#thr = cv2.GaussianBlur(thr,(5,5),0)
#thr = cv2.medianBlur(thr,5)

plt.subplot(2,1,1)
plt.imshow(img)
plt.subplot(2,1,2)
plt.imshow(thr,cmap='gray')

plt.show()






