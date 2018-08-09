#Milton Orlando Sarria
#Procesamiento digital de senales
#USC

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


#definir la frecuencia de muestreo y generar un vector de tiempo hasta 5 segundos
fs=16e3
longitud = 3# sec
n,T=np.linspace(1./fs,longitud,fs*longitud,retstep=True);

F=500             #frecuencia fundamental 
w=2*np.pi*F       #frecuencia angular
Vm=1            #valor de amplitud de la onda
#generar onda sinusoidal pura
y=Vm*np.cos(w*n)
#reproducir
sd.play(y, fs)
