import os 
import matplotlib.pyplot as plt
import numpy as np
import wav_process as wp
from wav_rw import wavread


archivo='sounds/piano.wav'
######################
# frequency range to plot
rango =[0.0, 8000.0]
(fs,x)=wavread(archivo)
print('frecuencia de muestreo: ' + str(fs) + ', numero de muestras: ' + str(x.size))

M = int(fs * 0.01)
H = int(fs * 0.005)
N = 2048
#window choice of rectangular, hanning, hamming, blackman, blackmanharris
(X,mX)=wp.enframe(x=x, window = 'hamming', M=M, H=H, N=N)

# plot the input sound
plt.subplot(2,1,1)
plt.plot(np.arange(x.size)/float(fs), x)
plt.axis([0, x.size/float(fs), min(x), max(x)])
plt.ylabel('amplitude')
plt.title('input sound: x')
         
# plot magnitude spectrogram
plt.subplot(2,1,2)
numFrames = int(X[:,0].size)
frmTime = H*np.arange(numFrames)/float(fs)
binFreq=np.linspace(0,fs/2,mX.shape[1])

bins=(binFreq>rango[0]) & (binFreq<rango[1])

plt.pcolormesh(np.transpose(mX[:,bins]))
plt.xlabel('time (sec)')
plt.ylabel('frequency (Hz)')
plt.title('magnitude spectrogram')
plt.autoscale(tight=True)
plt.show()
         
       
