import matplotlib.pyplot as plt
import numpy as np
from fourierFunc import fourierAn
import sounddevice as sd
from scipy import signal
from scipy.signal import get_window

#definir la frecuencia de muestreo y generar un vector de tiempo hasta 5 segundos
fs=16e3
tf = 5# tiempo final
#vector de tiempo
n=np.linspace(1./fs,tf,fs*tf);
#generar chirp
y = signal.chirp(n, f0=100, f1=1000, t1=tf, method='linear')


plt.subplot(3,1,1)
plt.plot(n,y)

#aplicar transformada de fourier
f_n,mX,pX = fourierAn(y)

#graficar transformada de fourier de la senal
plt.subplot(3,1,2)
plt.plot(f_n*fs/2, mX-max(mX), 'r', lw=1.5)
plt.axis([-fs/2,fs/2,-80,0])
plt.tight_layout()
plt.ylabel('|X| en dB')
plt.xlabel('Frecuencia - Hz')
y = y/np.max(np.abs(y))

sd.play(y, fs)
sd.wait()


#calcular el espectrograma usando las funcionalidades de scipy 
M = int(0.05*fs)
print(M)
window = 'hanning'
w = get_window(window,M)
f, t, Sxx = signal.spectrogram(y, fs, window=w, scaling='spectrum', noverlap = int(0.75*M))

plt.subplot(313)
plt.pcolormesh(t, f, 20*np.log10(Sxx))
plt.ylabel('Frequencia [Hz]')
plt.xlabel('Tiempo [sec]')

plt.show()



