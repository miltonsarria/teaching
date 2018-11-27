#For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255].

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('hands.png',cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([110,100,100])
upper = np.array([130,255,255])
mask = cv2.inRange(hsv, lower, upper)
res = cv2.bitwise_and(img,img, mask= mask)

cv2.imshow('original',img)

cv2.imshow('mask',mask)

cv2.imshow('resultado',res)
k = cv2.waitKey(0)
cv2.destroyAllWindows()


color = np.uint8([[[38,22,0 ]]])
hsv = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
print hsv

