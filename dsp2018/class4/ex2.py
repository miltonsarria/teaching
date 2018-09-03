#!/usr/bin/python
# Milton Orlando Sarria Paja
# dft
# Procesamiento digital de senales
#USC

import numpy as np
import matplotlib.pyplot as plt

################ DFT
N = 32
k0  = 20.8
#x   = np.exp(1j*2*np.pi*k0/N*np.arange(N))
x   = np.cos(2*np.pi*k0/N*np.arange(N))
X   = np.array([])
nv  = np.arange(-N/2,N/2)  #np.arange(N)
kv  = np.arange(-N/2,N/2)

for k in kv:
    s   =np.exp(1j*2*np.pi*k/N * nv)    
    X   =np.append(X,sum(x*np.conjugate(s)))
    
plt.plot(kv,np.abs(X), label='Magnitude')
plt.axis([-N/2, N/2-1,0,N])
plt.xlabel('n')
plt.ylabel('Amplidute')
ax =  plt.gca()
legend = ax.legend(loc='upper right', shadow=True)

plt.show()

# energia
Et=(np.abs(x)**2).sum()
Ef=(1./X.size*np.abs(X)**2).sum()

from scipy.fftpack import fft, ifft
#from scipy import signal

Xfft =  fft(x)
X2  =  np.fft.fft(x)

Efft=(1./Xfft.size*np.abs(Xfft)**2).sum()
Ef2=(1./X2.size*np.abs(X2)**2).sum()


print(Et,Ef,Efft,Ef2)
