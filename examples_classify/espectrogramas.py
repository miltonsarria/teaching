#git clone https://github.com/miltonsarria/talkbox.git
#cd talkbox
#python setup.py install
#pip install version
import numpy as np
import matplotlib.pyplot as plt
from wav_rw import wavread, wavwrite
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


        

#paso 1, definir los un archivos de audio
audios=['audio/isolated/pesa0.wav','audio/isolated/mesa0.wav','audio/isolated/peso0.wav',
'audio/isolated/queso0.wav','audio/si/audio2_si.wav','audio/no/audio2_no.wav']
plt.figure(1)
for ii in range(len(audios)):
    #leer cada audio
    fs,x=wavread(audios[ii])
    #paso 2, normalizar en el rango [-1,1], remuestrear a 16khz y definir parametros
    nfs=16000
    factor=fs/nfs				 #defininir el factor para reducir fs
    new_samples=int(x.size/factor)	         #nueva longitud de la senal 
    x = signal.resample(x, new_samples)
    x = x/np.max(np.abs(x))

    M = int(0.05*nfs)
    H = int(0.01*M)

    #paso 3, calcular el espectrograma 
    w = signal.hamming(M)
    f, t, Sxx = signal.spectrogram(x, nfs, window=w, scaling='spectrum', noverlap = int(0.6*M))

    #paso 4, visualizar el espectrograma con fft 
    if ii<4:
        plt.subplot(2,2,ii+1)
        plt.pcolormesh(t, f, 20*np.log10(Sxx))
        plt.title(audios[ii].split('/')[-1:][0])
   
        plt.autoscale(tight=True)
    else:
        plt.figure(2)
        plt.subplot(2,1,ii-3)
        plt.pcolormesh(t, f, 20*np.log10(Sxx))
        plt.title(audios[ii].split('/')[-1:][0])
   
        plt.autoscale(tight=True)
plt.show()

