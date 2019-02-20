#Milton Orlando Sarria
#Procesamiento digital de senales
#USC

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


#definir la frecuencia de muestreo y generar un vector de tiempo hasta 5 segundos
fs=16e3
longitud = 5# sec
n,T=np.linspace(1./fs,longitud,fs*longitud,retstep=True);

F=800             #frecuencia fundamental 
w=2*np.pi*F       #frecuencia angular
Vm=0.5            #valor de amplitud de la onda
#generar onda sinusoidal pura
x=Vm*np.cos(w*n)

lift1 = np.linspace(0,1,x.size)
lift2 = np.linspace(1,0,x.size)

#y=np.vstack((x*lift1,x*lift2))
y=x*lift1

#reproducir
sd.play(y.transpose(), fs)
