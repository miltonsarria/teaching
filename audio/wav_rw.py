#Milton Orlando Sarria
#Read and write a wav file
import copy, os
from scipy.io.wavfile import read
from scipy.io.wavfile import write
import numpy as np
from scipy.signal import get_window
#These are the wavread and wavwrite functions taken from utilFunctions of smstools
INT16_FAC = (2**15)-1
INT32_FAC = (2**31)-1
INT64_FAC = (2**63)-1
norm_fact = {'int16':INT16_FAC, 'int32':INT32_FAC, 'int64':INT64_FAC,'float32':1.0,'float64':1.0}
############################################################################
def wavread(filename):
    """
    Read a sound file and convert it to a normalized floating point array
    filename: name of file to read
    returns fs: sampling rate of file, x: floating point array
    """
    if (os.path.isfile(filename) == False):                  # raise error if wrong input file
        raise ValueError("Input file is wrong")
    fs, x = read(filename)

    if (len(x.shape) !=1):                                   # raise error if more than one channel
        print('audio en estereo: tomar solo el canal 1')
        #raise ValueError("Audio file should be mono")
        x=x[:,0]
        print(x.shape)
    #if (fs !=44100):                                         # raise error if fs is dfferent to 41kHz
    #    raise ValueError("Sampling rate of input sound should be 44100")

    #scale down and convert audio into floating point number in range of -1 to 1
    x = np.float32(x)/norm_fact[x.dtype.name]
    return fs, x
############################################################################    
def wavwrite(y, fs, filename):
    y=y/np.max(np.abs(y))
    """
    Write a sound file from an array with the sound and the sampling rate
    y: floating point array of one dimension, fs: sampling rate
    filename: name of file to create
    """
    x = copy.deepcopy(y)                         # copy array
    x *= INT16_FAC                               # scaling floating point -1 to 1 range signal to int16 range
    x = np.int16(x)                              # converting to int16 type
    write(filename, fs, x)    
############################################################################
def enframe(x = None, window = 'rectangular', M = 512, H = 512):
        """
        retorna una matriz de ventanas en tiempo corto usando M como longitud
        y H para incrementos
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
        
