#Milton Orlando Sarria
#INRS - 2014
import numpy as np
import os 
from scipy.io.wavfile import read
from scipy.signal import get_window
import math
from scipy.fftpack import fft, ifft

#######################
INT16_FAC = (2**15)-1
INT32_FAC = (2**31)-1
INT64_FAC = (2**63)-1
norm_fact = {'int16':INT16_FAC, 'int32':INT32_FAC, 'int64':INT64_FAC,'float32':1.0,'float64':1.0}
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
		raise ValueError("Audio file should be mono")

	#if (fs !=44100):                                         # raise error if fs is dfferent to 41kHz
	#	raise ValueError("Sampling rate of input sound should be 44100")

	#scale down and convert audio into floating point number in range of -1 to 1
	x = np.float32(x)/norm_fact[x.dtype.name]
	return fs, x
#######################
def enframe(x = None, window = 'hamming', M = 1024, H = 512):
        """
        inputs:
        x       input signal
        window  analysis window type (choice of rectangular, hanning, hamming, blackman, blackmanharris)	
        N       analysis window size 
        H       hop size (at least 1/2 of analysis window size to have good overlap-add) 
        output:
        X       np array with frames
        """
        if (x is None):                 # raise error if there is no input signal
           raise ValueError("there is no input signal")
		   
        # compute analysis window
	w    = get_window(window, M)
	pin  = 0                                        # the sound pointer starts at the sample 0
	pend = x.size-M                                 # last sample to start a frame
	w    = w / sum(w)                               # normalize analysis window
	while pin<=pend:                                # while sound pointer is smaller than last sample      
		x1 = x[pin:pin+M]                       # select one frame of input sound
		if (w.size != x1.size):                 # raise error if window size is different to frame size
                   raise ValueError("Window size (M) is different of frame size")
		xw = x1*w                               # window the frame
		mx = dftModel(xw)
                if pin == 0:                            # if first frame, create output array
			X = np.array([xw])			
			mX = np.array([mx])
		else:                                   # append output to existing array 
		        X = np.vstack((X,np.array([xw])))
		        mX = np.vstack((mX,np.array([mx])))
                pin += H                                # advance sound pointer
        return X, mX
        
def dftModel(xw,N=512):
	"""
	Analysis of a signal using the discrete Fourier transform
	x: input signal, N: FFT size
	returns y: output signal
	"""
	if all(xw==0):                                           # if input array is zeros return empty output
		return np.zeros(xw.size)
	hN = (N/2)+1                                            # size of positive spectrum, it includes sample 0
	hM1 = int(math.floor((xw.size+1)/2))                     # half analysis window size by rounding
	hM2 = int(math.floor(xw.size/2))                         # half analysis window size by floor
	fftbuffer = np.zeros(N)                                 # initialize buffer for FFT
	y = np.zeros(xw.size)                                    # initialize output array
	#----analysis--------

	fftbuffer[:hM1] = xw[hM2:]                              # zero-phase window in fftbuffer
	fftbuffer[-hM2:] = xw[:hM2]        
	X = fft(fftbuffer)                                      # compute FFT
	absX = abs(X[:hN])                                      # compute ansolute value of positive side
	absX[absX<np.finfo(float).eps] = np.finfo(float).eps    # if zeros add epsilon to handle log
	mX = 20 * np.log10(absX)                                # magnitude spectrum of positive frequencies in dB     
	pX = np.unwrap(np.angle(X[:hN]))                        # unwrapped phase spectrum of positive frequencies
	return mX
	 
  
        
