#example taken from scipy documentation
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


#disenar el filtro usando una ventana hamming
b = signal.firwin(9, 0.8, window='hamming', pass_zero=True)
#pasa bajas pass_zero=True
#pasa altas pass_zero=False

fs=1e3
t,T=np.linspace(1./fs,5,fs*5,retstep=True);
nFs=1/T;

F=10            #frecuencia fundamental 10 hz
w=2*np.pi*5     #frecuencia angular
Vm=4           #valor de amplitud de la onda

#generar onda compuesta de sinusoides
y=Vm*np.cos(w*t)+Vm/2*np.cos(2*w*t+np.deg2rad(45))+Vm/3*np.cos(3*w*t)+Vm/2*np.cos(4*w*t)
#generar onda de ruido sinusoidal, alta frecuencia y baja amplitud
x=2*np.cos(2*np.pi*370*t)
#onda con ruido
yx=y+x

#filtrar la onda con ruido usando el filtro FIR
yf=signal.lfilter(b, [1.0],yx)



plt.subplot(311)
plt.plot(t,y)
plt.title('onda sin ruido')

plt.subplot(312)
plt.plot(t,yx)
plt.title('onda con ruido')

plt.subplot(313)
plt.plot(t,yf)
plt.title('onda filtrada')


plt.xlabel('tiempo')

plt.show()





