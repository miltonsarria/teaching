import matplotlib.pyplot as plt
import numpy as np
from fourierFunc import fourierAn
from scipy.signal import get_window


M = 128   #tamaño de la ventana (usar solo numeros pares para este ejercicio)
N = 256  #numero de puntos de la FFT
hN = int(N/2) #punto medio de la fft
hM = int(M/2) #punto medio de la ventana
window = 'hamming'

#crear un arreglo para guardar la ventana y agregar ceros en los extremos
fftbuffer = np.zeros(N)

plt.figure(1, figsize=(7.5, 4))
#obtener la ventana y agregar ceros en los extremos
fftbuffer[hN-hM:hN+hM]=get_window(window, M)

#graficar ventana
plt.subplot(2,1,1)
plt.plot(np.arange(-hN, hN), fftbuffer, 'b', lw=1.5)
plt.axis([-hN, hN, 0, 1.1])

#aplicar transformada de fourier
absX,mX,pX = fourierAn(fftbuffer)

#graficar transformada de fourier de la ventana
plt.subplot(2,1,2)
plt.plot(np.arange(-hN, hN), mX-max(mX), 'r', lw=1.5)
plt.axis([-hN,hN,-80,0])
plt.tight_layout()
plt.ylabel('|X| en dB')
plt.xlabel('Frecuencia - Hz')
plt.show()



