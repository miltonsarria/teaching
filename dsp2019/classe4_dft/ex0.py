import matplotlib.pyplot as plt
import numpy as np


N = 8 #numero de muestras 

plt.subplot(2,2,1)
k=0
s = np.exp(-1j*2*np.pi*k/N*np.arange(N))
print(s)
plt.plot(np.real(s))
plt.plot(np.imag(s),'g')

plt.subplot(2,2,2)
k=1
s = np.exp(-1j*2*np.pi*k/N*np.arange(N))
print(s)
plt.plot(np.real(s))
plt.plot(np.imag(s),'g')


plt.subplot(2,2,3)
k=2
s = np.exp(-1j*2*np.pi*k/N*np.arange(N))
print(s)
plt.plot(np.real(s))
plt.plot(np.imag(s),'g')


plt.subplot(2,2,4)
k=3
s = np.exp(-1j*2*np.pi*k/N*np.arange(N))
print(s)
plt.plot(np.real(s))
plt.plot(np.imag(s),'g')


plt.show()
