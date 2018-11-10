
import cv2
import numpy as np
import matplotlib.pyplot as plt



kernel = np.ones((5,5),np.uint8)


img = cv2.imread('phone.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_, thr = cv2.threshold(gray,90, 255, cv2.THRESH_BINARY)
#thr = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 1)

#thr_m = cv2.dilate(thr,kernel,iterations = 1)
thr_m = cv2.erode(thr,kernel,iterations = 1)
#thr_m = cv2.morphologyEx(thr, cv2.MORPH_OPEN, kernel)
#thr_m = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, kernel)
#thr_m = cv2.morphologyEx(thr, cv2.MORPH_GRADIENT, kernel)

plt.subplot(2,2,1)
plt.imshow(img)
plt.subplot(2,2,2)
plt.imshow(thr,cmap='gray')
plt.subplot(2,2,3)
plt.imshow(thr_m,cmap='gray')


plt.show()






