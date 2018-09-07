import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.signal import get_window
from scipy.signal import spectrogram
from scipy.signal import lfilter
from scipy.signal import resample
#paso 1, cargar un archivo de audio
filename = 'vowels/u.wav'
fs, x = read(filename)

#paso 2, normalizar la senal
nfs=16000
factor=fs/nfs				 #defininir el factor para reducir fs
new_samples=int(x.size/factor)	         #nueva longitud de la senal 
#remuestrear la senal x y el resultado nx1 es la nueva secuencia remuestreada
x = resample(x, new_samples)
#normalizar al rango [-1,1]
x = x/np.max(np.abs(x))
x = lfilter([1 -0.97], 1, x);

#paso 3, calcular el espectrograma
M = int(0.005*nfs)
w = get_window('hamming', M)

f, t, Sxx = spectrogram(x, nfs, window=w, scaling='spectrum')

#paso 4, visualizar el espectrograma y la senal

plt.subplot(211)
plt.pcolormesh(t, f, 20*np.log10(Sxx))
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')


plt.subplot(212)
plt.plot(np.arange(0,x.size)/nfs,x)


plt.show()
