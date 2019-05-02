import matplotlib.pyplot as plt
import numpy as np
from fourierFunc import fourierAn
import sounddevice as sd
from scipy import signal

#definir la frecuencia de muestreo y generar un vector de tiempo hasta 5 segundos
fs=16e3
longitud = 5# sec
n=np.linspace(1./fs,longitud,fs*longitud);
y = signal.chirp(n, f0=100, f1=1000, t1=5, method='linear')


plt.subplot(2,1,1)
plt.plot(n,y)

#aplicar transformada de fourier
f_n,mX,pX = fourierAn(y)

#graficar transformada de fourier de la senal
plt.subplot(2,1,2)
plt.plot(f_n*fs/2, mX-max(mX), 'r', lw=1.5)
plt.axis([-fs/2,fs/2,-80,0])
plt.tight_layout()
plt.ylabel('|X| en dB')
plt.xlabel('Frecuencia - Hz')
y = y/np.max(np.abs(y))

sd.play(y, fs)
sd.wait()
plt.show()



