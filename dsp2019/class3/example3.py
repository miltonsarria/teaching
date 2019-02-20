#Milton Orlando Sarria
#Procesamiento digital de senales
#USC

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


#definir la frecuencia de muestreo y generar un vector de tiempo hasta 5 segundos
fs=16e3
longitud = 1# sec
n,T=np.linspace(1./fs,longitud,fs*longitud,retstep=True);

F1=800             #frecuencia  1
F2=400             #frecuencia  2
F3=600             #frecuencia  3
#frecuencias angulares
w1=2*np.pi*F1      
w2=2*np.pi*F2
w3=2*np.pi*F3
Vm=0.5            #valor de amplitud de la onda
#generar ondas sinusoidales
x1=Vm*np.cos(w1*n)
x2=Vm*np.cos(w2*n)
x3=Vm*np.cos(w3*n)

y=np.hstack((x1,x2,x3))


#reproducir
sd.play(y, fs)
