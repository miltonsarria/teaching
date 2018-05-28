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
Fs=60
tf=5 #tiempo final
#definir la secuencia de tiempo hasta 5 segundos
nT=np.linspace(1./Fs,tf,Fs*tf);

#definir dos componentes frecuenciales en Hz y calcular su equivalente en rad/s
F1=5
F2=7

#omega
w1=2*np.pi*F1
w2=2*np.pi*F2


#definir ventana
window = 'hamming'

#secuencias separadas
A1=1
A2=0.1
x1=A1*np.sin(w1*nT)
x2=A2*np.cos(w2*nT)
#generar secuencia discreta x[n]=x1[n]+x2[n]
x=A1*np.sin(w1*nT)+A2*np.cos(w2*nT)


N=512
n=nT.size
x=np.hstack((np.zeros(int((N-n)/2)),x,np.zeros(int((N-n)/2))))
x1=np.hstack((np.zeros(int((N-n)/2)),x1,np.zeros(int((N-n)/2))))
x2=np.hstack((np.zeros(int((N-n)/2)),x2,np.zeros(int((N-n)/2))))

#generar ventana
M =  n
w = get_window(window, M)
w=np.hstack((np.zeros(int((N-n)/2)),w,np.zeros(int((N-n)/2))))

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
plt.subplot(411)
plt.plot(x1)
plt.ylabel('x1[n]')

plt.subplot(412)
plt.plot(x2)
plt.ylabel('x2[n]')

plt.subplot(413)
plt.plot(x)
plt.ylabel('x[n]=x1[n]+x2[n]')

plt.subplot(414)
plt.plot(xw)
plt.ylabel('x[n]*w[n]')
plt.xlabel('tiempo - s')


plt.figure(2)
plt.subplot(311)
plt.plot(f,Xdbw)

plt.subplot(312)
plt.plot(f,Xdbw1)

plt.subplot(313)

plt.plot(f,Xdbw2)


plt.show()




