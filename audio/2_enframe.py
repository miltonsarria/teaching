import os 
import matplotlib.pyplot as plt
import numpy as np
import wav_process as wp
from wav_rw import wavread
from scipy.signal import get_window


#cambiar el nombre del archivo

archivo='sounds/sines-440-602-transient.wav'
######################
# modificar el rango de frecuencias para ver una banda especifica
rango =[0.0, 8000.0]
(fs,x)=wavread(archivo)
print('frecuencia de muestreo: ' + str(fs) + ', numero de muestras: ' + str(x.size))

long_ventana =  0.025 #en segundos
incremento   =  0.01#en segundos
#en muestras
M = int(fs * long_ventana)
H = int(fs * incremento)
#tipo de ventana, window puede ser rectangular, hanning, hamming, blackman, blackmanharris
window = 'blackman'

N = 2048 #si usa una longitud de ventana superior a 0.05 usar 4096

(X,mX)=wp.enframe(x=x, window = window, M=M, H=H, N=N)

# graficar el archivo de audio
plt.subplot(2,1,1)
plt.plot(np.arange(x.size)/float(fs), x)
plt.axis([0, x.size/float(fs), min(x), max(x)])
plt.ylabel('amplitude')
plt.title('input sound: x')
         
# graficar la magnitud del espectro en decibeles
plt.subplot(2,1,2)
numFrames = int(X[:,0].size)
frmTime = H*np.arange(numFrames)/float(fs)
binFreq=np.linspace(0,fs/2,mX.shape[1])
bins=(binFreq>rango[0]) & (binFreq<rango[1])

Sxx=np.transpose(mX[:,bins])
binFreq=binFreq[bins]

plt.pcolormesh(frmTime,binFreq,Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.autoscale(tight=True)

#graficar el espectro de todo el archivo de audio sin ventanear
M  = x.size
w  = get_window(window, M)
w  = w / sum(w)       
xw = x*w              
mX,pX = wp.magFourier(xw,xw.size)
binFreq=np.linspace(0,fs/2,mX.size)
bins=(binFreq>rango[0]) & (binFreq<rango[1])
plt.figure(2)
plt.plot(binFreq[bins],mX[bins])

plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitud en dB')

plt.show()
         
       
