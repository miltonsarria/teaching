import matplotlib.pyplot as plt
import numpy as np
from fourierFunc import fourierAn
import sounddevice as sd


#definir la frecuencia de muestreo y generar un vector de tiempo hasta 5 segundos
fs=16e3
longitud = 1# sec
n=np.linspace(1./fs,longitud,fs*longitud);

F1=200             #frecuencia fundamental 
F2=400             #
F3=600             #
F4=800             #
F5=1000            #

#generar ondas sinusoidal puras y compuestas
y1=np.cos(2*np.pi*F1*n)
y2=np.cos(2*np.pi*F1*n) + np.cos(2*np.pi*F2*n)
y3=np.cos(2*np.pi*F3*n)
y4=np.cos(2*np.pi*F1*n) + np.cos(2*np.pi*F4*n) 
y5=np.cos(2*np.pi*F2*n) + np.cos(2*np.pi*F3*n) + np.cos(2*np.pi*F5*n)

y = np.hstack((y1,y2,y3,y4,y5))
n = np.arange(y.size)/fs 
plt.subplot(2,1,1)
plt.plot(n,y)

#aplicar transformada de fourier
f_n,mX,pX = fourierAn(y)

#graficar transformada de fourier de la ventana
plt.subplot(2,1,2)
plt.plot(f_n*fs/2, mX-max(mX), 'r', lw=1.5)
plt.axis([-fs/2,fs/2,-80,0])
plt.tight_layout()
plt.ylabel('|X| en dB')
plt.xlabel('Frecuencia - Hz')

#normalizar en el rango [-1,1] antes de reproducir el audio
y = y/np.max(np.abs(y))

sd.play(y, fs)
sd.wait()

plt.show()



