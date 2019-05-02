import matplotlib.pyplot as plt
import numpy as np
from fourierFunc import fourierAn
import sounddevice as sd
from scipy.signal import get_window
from scipy import signal
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
M = int(0.02*fs)
print(M)
window = 'hanning'
w = get_window(window,M)
f, t, Sxx = signal.spectrogram(y, fs, window=w, scaling='spectrum', noverlap = int(0.75*M))

plt.subplot(313)
plt.pcolormesh(t, f, 20*np.log10(Sxx))
plt.ylabel('Frequencia [Hz]')
plt.xlabel('Tiempo [sec]')


plt.show()



