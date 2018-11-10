import numpy as np
import cv2
import imutils
cap = cv2.VideoCapture(0)

lower = np.array([80,100,100])
upper = np.array([110,255,255])
kernel = np.ones((10,10),np.uint8)

while(True):
    # Capturar un frame de la camara
    _, frame = cap.read()
    # Las operaciones sobre el frame van aqui
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)    
    gray = cv2.GaussianBlur(gray,(9,9),0)
    
    _, thr = cv2.threshold(gray,50, 255, cv2.THRESH_BINARY)
    #thr = cv2.morphologyEx(thr, cv2.MORPH_OPEN, kernel)
    thr = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, kernel)
    '''
    #calcular contornos
    cnts = cv2.findContours(thr.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    #dibujar contornos    
    for c in cnts:
        #     c = cnts[0]  
        # compute the center of the contour
        M = cv2.moments(c)
        try:
          cX = int(M["m10"] / M["m00"])
          cY = int(M["m01"] / M["m00"])
          x=cX
          y=cY
          # draw the contour and center of the shape on the image             
          cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
          cv2.circle(frame, (cX, cY), 7, (255, 255, 255), -1)
                
        except:
             pass        
    
    '''
    #mostrar resultados    
    cv2.imshow('original',frame)
    cv2.imshow('resultado',thr)


    if cv2.waitKey(33)==27:
        break
# liberar el dispositivo y destruir ventanas
cap.release()
cv2.destroyAllWindows()




