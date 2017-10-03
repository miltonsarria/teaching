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
#generar onda de ruido sinusoidal, alta frecuencia y baja amplitud
x=1*np.cos(2*np.pi*150.3*t) + 1*np.cos(2*np.pi*151.1*t) + 1*np.cos(2*np.pi*155.8*t)+1*np.cos(2*np.pi*155.9*t)
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
np.savetxt('sierra_ruido_sin.txt', YX, fmt='%5.5f', delimiter=',', newline='\n', header='', footer='', comments='# ')

plt.show()

