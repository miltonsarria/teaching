import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(255,255,255),15)
cv2.circle(img,(100,63), 55, (0,255,0), -1)
cv2.rectangle(img,(15,25),(200,150),(0,0,255),15)

imgplot = plt.imshow(img)
plt.show()
