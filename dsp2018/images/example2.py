import cv2
import numpy as np
import matplotlib.pyplot as plt



img = cv2.imread('bookpage.jpg')
_, threshold = cv2.threshold(img, 5, 255, cv2.THRESH_BINARY)
plt.subplot(2,1,1)
plt.imshow(img)
plt.subplot(2,1,2)
plt.imshow(threshold)

plt.show()

#
