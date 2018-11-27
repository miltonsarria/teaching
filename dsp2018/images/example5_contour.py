import numpy as np
import cv2
import imutils
cap = cv2.VideoCapture(0)

lower = np.array([90,200,100])
upper = np.array([115,255,250])
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
    
    
    #mostrar resultados    
    cv2.imshow('original',frame)
    cv2.imshow('resultado',thr)


    if cv2.waitKey(33)==27:
        break
# liberar el dispositivo y destruir ventanas
cap.release()
cv2.destroyAllWindows()


#el siguiente codigo guardelo en un archivo separado o 
#ejecutelo de forma independiente en ipython
#pasos
#1) tomar una foto con el objeto o color que quieres seguir
#2) usando gimp y el selectro de color (gotero) seleccionar un punto
#para saber cual es el color, recuerde que se debe leer en el orden B G R
#3) reemplazar los valores en el vector del codigo de abajo
#4) una vez tenga el equivalente en hsv, el mas importante es el primer valor
#   tomar un rango de valor+10 y valor-10  aproximadamente 
#5) usar ese valor en el ejemplo5_countour.py en las primeras lineas
#lower = np.array([90,200,100])
#upper = np.array([115,255,250])
#ejecutar el codigo y verificar que se sigue el color deseado
#para salir del programa se usa la tecla esc

#import cv2
#import numpy as np
#color = np.uint8([[[38,22,0 ]]])
#hsv = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
#print(hsv)


