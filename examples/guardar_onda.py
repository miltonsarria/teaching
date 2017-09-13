import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.fftpack import fft, ifft
from scipy import signal


fs=20e3
t,T=np.linspace(1./fs,10,fs*10,retstep=True);
nFs=1/T;

w=2*np.pi*3
Vm=10
x1=Vm*np.sign(np.cos(w*t))
x2=Vm*signal.sawtooth(w*t)
x3=Vm/2*np.sign(np.cos(w*t))+Vm/2.

X1=np.vstack((t,x1))
X1=X1.transpose()
X2=np.vstack((t,x2))
X2=X2.transpose()

X3=np.vstack((t,x3))
X3=X3.transpose()

np.savetxt('cuadrada1.txt', X1, fmt='%5.5f', delimiter=',', newline='\n', header='', footer='', comments='# ')
np.savetxt('cuadrada2.txt', X3, fmt='%5.5f', delimiter=',', newline='\n', header='', footer='', comments='# ')
np.savetxt('sierra.txt', X2, fmt='%5.5f', delimiter=',', newline='\n', header='', footer='', comments='# ')

plt.plot(t,x1)
plt.plot(t,x2)
plt.plot(t,x3)
plt.show()

