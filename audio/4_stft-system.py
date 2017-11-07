import numpy as np
import time, os, sys
import wav_process as wp
import matplotlib.pyplot as plt
#from scipy.signal import hamming
from wav_rw import wavread, wavwrite
from scipy.signal import get_window

#seleccionar el archivo de audio, el tipo de ventana, tamaño, numero de puntos de la FFT y traslape

(fs, x) = wavread('sound/speech-male.wav')
#window puede ser rectangular, hanning, hamming, blackman, blackmanharris...........
window = 'rectangular'
M=  1024
N = 1024
H = 500
#generar ventana y normalizarla
w = get_window(window, M)
#obtener la transformada de fourier del archivo de audio (magnitud y la fase)
mX, pX = wp.stftAnal(x, w, N, H)

#usando la magnitud y fase reconstuir el archivo de audio
y = wp.stftSynth(mX, pX, w.size, H)

#realizar las graficas respectivas para comparar los resultados
plt.figure(1, figsize=(9.5, 7))
plt.subplot(311)
plt.plot(np.arange(x.size)/float(fs), x, 'b')
plt.title('x (audio original wav)')
plt.axis([0,x.size/float(fs),min(x),max(x)])

plt.subplot(312)
numFrames = int(mX[:,0].size)
frmTime = H*np.arange(numFrames)/float(fs)                             
binFreq = np.arange(mX[0,:].size)*float(fs)/N                         
plt.pcolormesh(frmTime, binFreq, np.transpose(mX))
plt.title('mX, M='+str(M)+', N='+str(N)+', H='+str(H))
plt.autoscale(tight=True)

plt.subplot(313)
plt.title('x (audio reconstruido wav)')
plt.plot(np.arange(y.size)/float(fs), y,'b')
plt.axis([0,y.size/float(fs),min(y),max(y)])
plt.title('y')

plt.tight_layout()
wavwrite(y, fs, 'output/audio_stft.wav')
plt.show()
  
  
  
