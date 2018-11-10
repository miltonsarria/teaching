import numpy as np
import cv2
cap = cv2.VideoCapture(0)

lower = np.array([80,100,100])
upper = np.array([110,255,255])


while(True):
    # Capturar un frame de la camara
    _, frame = cap.read()
    # Las operaciones sobre el frame van aqui
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #mostrar resultados    
    cv2.imshow('original',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('resultado',res)

    if cv2.waitKey(33)==27:
        break
# liberar el dispositivo y destruir ventanas
cap.release()
cv2.destroyAllWindows()

