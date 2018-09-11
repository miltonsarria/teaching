#git clone https://github.com/miltonsarria/talkbox.git
#cd talkbox
#python setup.py install
#pip install version
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy import signal
from scipy.signal import get_window
from scikits.talkbox.spectral.basic import periodogram, arspec
from scipy.fftpack import fft
import math

def enframe(x = None, window = 'hamming', M = 1024, H = 512):
        """
        inputs:
        x       input signal
        window  analysis window type (choice of rectangular, hanning, hamming, blackman, blackmanharris)
        M       analysis window size
        H       hop size (at least 1/2 of analysis window size to have good overlap-add) 
        output:
        X       np array with frames
        """
        if (x is None):                         # raise error if there is no input signal
           raise ValueError("there is no input signal")
        x = np.squeeze(x)
        w    = get_window(window, M)            # compute analysis window
        w    = w / sum(w)                       # normalize analysis window        
        if x.ndim != 1: 
                raise TypeError("enframe input must be a 1-dimensional array.")
        n_frames = 1 + np.int(np.floor((len(x) - M) / float(H)))
        xf = np.zeros((n_frames, M))
        for ii in range(n_frames):
                xf[ii] = x[ii * H : ii * H + M]*w
        return xf 


        

#paso 1, cargar un archivo de audio
filename = 'vowels/i.wav'

fs, x = read(filename)
if len(x.shape)>1:
        x=x[:,0]
#paso 2, normalizar en el rango [-1,1] y remuestrear a 16khz y definir parametros
nfs=16000
factor=fs/nfs				 #defininir el factor para reducir fs
new_samples=int(x.size/factor)	         #nueva longitud de la senal 
x = signal.resample(x, new_samples)
x = x/np.max(np.abs(x))

M = int(0.005*nfs)
H = int(0.4*M)

#paso 3, calcular el espectrograma , espectro y promedio del espectrograma 
w = signal.hamming(M)
f, t, Sxx = signal.spectrogram(x, nfs, window=w, scaling='spectrum', noverlap = int(0.6*M))

#calcular el espectro con la fft y lpc
px1, fx1 = arspec(x * signal.hamming(x.size) , order = 20, fs=nfs)

X=fft(x * signal.hamming(x.size))
absX = abs(X)/(X.size)
hN=int(math.floor((X.size+1)/2))
absX=absX[:hN]
absX[absX < np.finfo(float).eps] = np.finfo(float).eps
px2 = 20 * np.log10(absX)
fx2 = np.linspace(0,nfs/2.,px2.size) 

#promediar spectrograma  para suavizar el espectro
px3 = np.mean(Sxx,axis=1)


#paso 4, calcular espectrograma usando lpc
xx = enframe(x = x, window = 'hamming', M = M, H = H)
i=0
numFrames = xx.shape[0]
frmTime = H*np.arange(numFrames+1)/float(nfs) 

for fx in xx:
    px, fx = arspec(fx , order = 20, fs=nfs)    
    if i==0:
            lpcX = np.array([px])
            i=1
    if i==1:
            lpcX = np.vstack((lpcX,np.array([px])))    
lpcX=lpcX.transpose()
#paso 3, visualizar el espectrograma con fft y lpc, tambien el promedio
plt.subplot(311)
plt.pcolormesh(t, f, 20*np.log10(Sxx))
plt.ylabel('Frequencia [Hz]')
plt.xlabel('Tiempo [sec]')


plt.subplot(312)
plt.pcolormesh(frmTime, fx, 20*np.log10(lpcX))
plt.ylabel('Frequencia [Hz]')
plt.xlabel('Tiempo [sec]')


plt.subplot(313)
plt.plot(fx2, px2)
plt.plot(fx1, 10 * np.log10(px1),linewidth=2)
plt.plot(f, 20*np.log10(px3),linewidth=2)

plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')





plt.show()

