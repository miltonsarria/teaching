import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    # Capturar un frame de la camara
    ret, frame = cap.read()

    # Las operaciones sobre el frame van aqui
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Mostrar el resultado
    cv2.imshow('frame',gray)
    if cv2.waitKey(33):
        break
# liberar el dispositivo y destruir ventanas
cap.release()
cv2.destroyAllWindows()


    
    
#    k = cv2.waitKey(33)
#    if k == 27:
#        break

#cv2.destroyAllWindows()
#cap.release()

