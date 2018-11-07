#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2

img = cv2.imread('dog.jpg')
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagen de perro',img_g)
cv2.imwrite('dog_gris.jpg',img_g)

img_bn=np.zeros(img_g.shape)
for i in range(img_g.shape[0]):
    for j in range(img_g.shape[1]): 

        if img_g[i,j]>128:
            img_bn[i,j]=256            
        
        
cv2.imwrite('dog_bn.jpg',img_bn)
       


k = cv2.waitKey(0)