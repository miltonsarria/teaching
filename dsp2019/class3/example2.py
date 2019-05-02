#Milton Orlando Sarria
#Procesamiento digital de senales
#USC
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
#definir la frecuencia de muestreo y generar un vector de tiempo hasta 5 segundos
fs=16e3
longitud = 2# sec
n=np.linspace(1./fs,longitud,fs*longitud);
F=800             #frecuencia fundamental 
w=2*np.pi*F       #frecuencia angular
Vm=10          #valor de amplitud de la onda
#generar onda sinusoidal pura
x=Vm*np.cos(w*n)
lift1 = np.linspace(0,1,x.size)
lift2 = np.linspace(1,0,x.size)
#y=np.vstack((x*lift1,x*lift2))
y1=x*lift1
y2=x*lift2
y=np.hstack((y1,y2))
sd.play(y.transpose(), fs)
sd.wait()
