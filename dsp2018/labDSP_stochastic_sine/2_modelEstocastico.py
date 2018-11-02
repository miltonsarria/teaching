import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hamming, hanning, triang, blackmanharris, resample
import math
import sys, os, time
from scipy.fftpack import fft, ifft
import wav_rw as rw
import stochasticModel as sm


#
if __name__ == '__main__':

  (fs, x) = rw.wavread('sound/si.wav')
  scale=np.max(np.abs(x))
  x=x/scale
  
  N=512
  H=256
  w = np.hanning(N)
  stocf = 0.1
  
  y=sm.stochasticModel(x, H, N, stocf)
  
  plt.figure(1, figsize=(9, 5))
  plt.subplot(2,1,1)
  plt.plot(x)
  plt.title('original')
  plt.subplot(2,1,2)
  plt.plot(y)
  plt.title('\hat y')
  plt.show()
  
  rw.wavwrite(y*scale, fs, 'output/si.wav')
