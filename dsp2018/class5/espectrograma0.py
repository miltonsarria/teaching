import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy import signal


#paso 1, cargar un archivo de audio
filename = 'vowels/a.wav'

fs, x = read(filename)
if len(x.shape)>1:
        x=x[:,0]
#paso 2, normalizar en el rango [-1,1]
x = x/np.max(np.abs(x))

#paso 3, calcular el espectrograma
f, t, Sxx = signal.spectrogram(x, fs)

#paso 3, visualizar el espectrograma
plt.pcolormesh(t, f, np.log10(Sxx))
plt.ylabel('Frequencia [Hz]')
plt.xlabel('Tiempo [sec]')
plt.show()

