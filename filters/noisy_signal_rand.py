import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.fftpack import fft, ifft
from scipy import signal


fs=1e3
t,T=np.linspace(1./fs,5,fs*5,retstep=True);
nFs=1/T;

F=10            #frecuencia fundamental 10 hz
w=2*np.pi*5     #frecuencia angular
Vm=10           #valor de amplitud de la onda

#generar onda diente de sierra a 10hz y duracion 5 segundos
y=Vm*signal.sawtooth(w*t)
#generar onda de ruido aleatorio y de baja amplitud
mu, sigma = 0, 3 # Media y desviacion estandard
x = np.random.normal(mu, sigma, y.size)
b = signal.firwin(127, 0.6, window='hamming', pass_zero=False)
x=signal.lfilter(b, [1.0],x)
#onda con ruido
yx=y+x

plt.subplot(211)
plt.plot(t,y)
plt.title('onda sin ruido')

plt.subplot(212)
plt.plot(t,yx)
plt.title('onda con ruido')
plt.xlabel('tiempo')

YX=np.vstack((t,yx))
YX=YX.transpose()
np.savetxt('sierra_ruido_ran.txt', YX, fmt='%5.5f', delimiter=',', newline='\n', header='', footer='', comments='# ')

plt.show()

