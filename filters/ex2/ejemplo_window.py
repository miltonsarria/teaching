#procesamiento digital de senales
#universidad santiago de cali

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('tools/')
from fourierFunc import fourierAn
from scipy.signal import get_window

##########################################
#BLOQUE 1
#definir la frecuencia de muestreo
Fs=20
F1=2
F2=5

#omega
w1=2*np.pi*F1
w2=2*np.pi*F2

tf=50 #tiempo final
#definir la secuencia de tiempo hasta 5 segundos
nT=np.linspace(1./Fs,tf,Fs*tf);

#generar secuencia discreta x[n]=x1[n]+x2[n]
x=2*np.sin(w1*nT)+1*np.cos(w2*nT)
#secuencias separadas
x1=2*np.sin(w1*nT)
x2=1*np.cos(w2*nT)

#generar ventana y normalizarla
window = 'hanning'
M=  nT.size
w = get_window(window, M)

xw=x*w
xw1=x1*w
xw2=x2*w
#usar fourier 
absX,Xdb,pX=fourierAn(x)
f=np.linspace(-Fs/2,Fs/2,Xdb.size)

absXw,Xdbw,pXw=fourierAn(xw)
absXw1,Xdbw1,pXw2=fourierAn(xw1)
absXw2,Xdbw2,pXw2=fourierAn(xw2)

#visualizar los resultados del analisis hecho con transformada de fourier


plt.subplot(311)
plt.plot(nT,x)
plt.ylabel('x[n]')
plt.xlabel('tiempo - s')

plt.subplot(312)
plt.plot(nT,x1)

plt.subplot(313)
plt.plot(nT,x2)

plt.figure(2)
plt.subplot(311)
plt.plot(f,Xdbw)

plt.subplot(312)
plt.plot(f,Xdbw1)

plt.subplot(313)
plt.plot(f,Xdbw2)


plt.show()




