#Milton Orlando Sarria
#INRS - 2014
import numpy as np
import os 
from scipy.signal import get_window
import math
from scipy.fftpack import fft, ifft

#######################
INT16_FAC = (2**15)-1
INT32_FAC = (2**31)-1
INT64_FAC = (2**63)-1
norm_fact = {'int16':INT16_FAC, 'int32':INT32_FAC, 'int64':INT64_FAC,'float32':1.0,'float64':1.0}
tol = 1e-14 
#######################
def enframe(x = None, window = 'hamming', M = 1024, H = 512,N=512):
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
                mx,px = magFourier(xw,N)
                if pin == 0:                            # if first frame, create output array
                        X = np.array([xw])
                        mX = np.array([mx])
                        pX=np.array([px])
                else:                                   # append output to existing array 
                        X = np.vstack((X,np.array([xw])))
                        mX = np.vstack((mX,np.array([mx])))
                        pX=np.vstack((pX,np.array([px])))
                pin += H                                # advance sound pointer
        return X, mX
        
def magFourier(xw,N=512):
         """
         Analisis de una senal usando  discrete Fourier transform
         xw: senal entrada, N: FFT numero de puntos fft
         returns Xm: magnitud del espectro, pX: fase del espectro
         """
         if all(xw==0):                                           # if input array is zeros return empty output
                return np.zeros(xw.size)
         hN = int(N/2)+1                                            # size of positive spectrum, it includes sample 0
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
         return mX,pX
          
  



def stftAnal(x, w, N, H) :
	"""
	Analysis of a sound using the short-time Fourier transform
	x: input array sound, w: analysis window, N: FFT size, H: hop size
	returns xmX, xpX: magnitude and phase spectra
	"""
	if (H <= 0):                                   # raise error if hop size 0 or negative
		raise ValueError("Traslape (H) es mas negativo o igual 0")
		
	M = w.size                                      # size of analysis window
	hM1 = int(math.floor((M+1)/2))                  # half analysis window size by rounding
	hM2 = int(math.floor(M/2))                      # half analysis window size by floor
	x = np.append(np.zeros(hM2),x)                  # add zeros at beginning to center first window at sample 0
	x = np.append(x,np.zeros(hM2))                  # add zeros at the end to analyze last sample
	pin = hM1                                       # initialize sound pointer in middle of analysis window       
	pend = x.size-hM1                               # last sample to start a frame
	w = w / sum(w)                                  # normalize analysis window
	while pin<=pend:                                # while sound pointer is smaller than last sample      
		x1 = x[pin-hM1:pin+hM2]                       # select one frame of input sound
		mX, pX = dftAnal(x1, w, N)                # compute dft
		if pin == hM1:                                # if first frame create output arrays
			xmX = np.array([mX])
			xpX = np.array([pX])
		else:                                         # append output to existing array 
			xmX = np.vstack((xmX,np.array([mX])))
			xpX = np.vstack((xpX,np.array([pX])))
		pin += H                                      # advance sound pointer
	return xmX, xpX

def stftSynth(mY, pY, M, H) :
	"""
	Synthesis of a sound using the short-time Fourier transform
	mY: magnitude spectra, pY: phase spectra, M: window size, H: hop-size
	returns y: output sound
	"""
	hM1 = int(math.floor((M+1)/2))                   # half analysis window size by rounding
	hM2 = int(math.floor(M/2))                       # half analysis window size by floor
	nFrames = mY[:,0].size                           # number of frames
	y = np.zeros(nFrames*H + hM1 + hM2)              # initialize output array
	pin = hM1                  
	for i in range(nFrames):                         # iterate over all frames      
		y1 = dftSynth(mY[i,:], pY[i,:], M)         # compute idft
		y[pin-hM1:pin+hM2] += H*y1                     # overlap-add to generate output sound
		pin += H                                       # advance sound pointer
	y = np.delete(y, range(hM2))                     # delete half of first window which was added in stftAnal
	y = np.delete(y, range(y.size-hM1, y.size))      # delete the end of the sound that was added in stftAnal
	return y

 
 
 
def dftAnal(x, w, N):
	"""
	Analysis of a signal using the discrete Fourier transform
	x: input signal, w: analysis window, N: FFT size 
	returns mX, pX: magnitude and phase spectrum
	"""

	if not(isPower2(N)):                                 # raise error if N not a power of two
		raise ValueError("FFT size (N) is not a power of 2")

	if (w.size > N):                                        # raise error if window size bigger than fft size
		raise ValueError("Window size (M) is bigger than FFT size")

	hN = int((N/2)+1 )                                           # size of positive spectrum, it includes sample 0)
	hM1 = int(math.floor((w.size+1)/2))                     # half analysis window size by rounding
	hM2 = int(math.floor(w.size/2))                         # half analysis window size by floor
	fftbuffer = np.zeros(N)                                 # initialize buffer for FFT
	w = w / sum(w)                                          # normalize analysis window
	xw = x*w                                                # window the input sound
	fftbuffer[:hM1] = xw[hM2:]                              # zero-phase window in fftbuffer
	fftbuffer[-hM2:] = xw[:hM2]        
	X = fft(fftbuffer)                                      # compute FFT
	absX = abs(X[:hN])                                      # compute ansolute value of positive side
	absX[absX<np.finfo(float).eps] = np.finfo(float).eps    # if zeros add epsilon to handle log
	mX = 20 * np.log10(absX)                                # magnitude spectrum of positive frequencies in dB
	X[:hN].real[np.abs(X[:hN].real) < tol] = 0.0            # for phase calculation set to 0 the small values
	X[:hN].imag[np.abs(X[:hN].imag) < tol] = 0.0            # for phase calculation set to 0 the small values         
	pX = np.unwrap(np.angle(X[:hN]))                        # unwrapped phase spectrum of positive frequencies
	return mX, pX

def dftSynth(mX, pX, M):
	"""
	Synthesis of a signal using the discrete Fourier transform
	mX: magnitude spectrum, pX: phase spectrum, M: window size
	returns y: output signal
	"""

	hN = mX.size                                            # size of positive spectrum, it includes sample 0
	N = int((hN-1)*2)                                            # FFT size
	if not(isPower2(N)):                                 # raise error if N not a power of two, thus mX is wrong
		raise ValueError("size of mX is not (N/2)+1")

	hM1 = int(math.floor((M+1)/2))                          # half analysis window size by rounding
	hM2 = int(math.floor(M/2))                              # half analysis window size by floor
	fftbuffer = np.zeros(N)                                 # initialize buffer for FFT
	y = np.zeros(M)                                         # initialize output array
	Y = np.zeros(N, dtype = complex)                        # clean output spectrum
	Y[:hN] = 10**(mX/20) * np.exp(1j*pX)                    # generate positive frequencies
	Y[hN:] = 10**(mX[-2:0:-1]/20) * np.exp(-1j*pX[-2:0:-1]) # generate negative frequencies
	fftbuffer = np.real(ifft(Y))                            # compute inverse FFT
	y[:hM2] = fftbuffer[-hM2:]                              # undo zero-phase window
	y[hM2:] = fftbuffer[:hM1]
	return y       
	
def isPower2(num):
	"""
	Check if num is power of two
	"""
	return ((num & (num - 1)) == 0) and num > 0
