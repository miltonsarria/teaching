import matplotlib.pyplot as plt
import numpy as np
from fourierFunc import fourierAn
from scipy.signal import get_window


M = 16   #tamano de la ventana
N = 32   #numero de puntos de la FFT
hN = int(N/2) #punto medio de la fft
hM = int(M/2) #punto medio de la ventana
window = 'hanning'

#crear un arreglo para guardar la ventana y agregar ceros en los extremos
fftbuffer = np.zeros(N)
#generar la ventana ponerla en la parte central del arreglo, quedando los ceros a los extremos
fftbuffer[hN-hM:hN+hM]=get_window(window, M)

#graficar ventana
plt.subplot(2,1,1)
plt.plot(np.arange(-hN, hN), fftbuffer, 'b', lw=1.5)
plt.axis([-hN, hN, 0, 1.1])

#aplicar transformada de fourier
f_n,mX,pX = fourierAn(fftbuffer)

#graficar transformada de fourier de la ventana
plt.subplot(2,1,2)
plt.plot(np.arange(-hN, hN), mX-max(mX), 'r', lw=1.5)
plt.axis([-hN,hN,-80,0])
plt.tight_layout()
plt.ylabel('|X| en dB')
plt.xlabel('Frecuencia - Hz')
plt.show()



