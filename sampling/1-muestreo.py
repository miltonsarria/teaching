#Milton Orlando Sarria Paja
#USC 2017
#muestreo de senales y aliasing 



import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.fftpack import fft, ifft
from scipy import signal


#generar una onda sinusoidal de 1 Hz, idealmente esta es la onda que se quiere muestrear
t0=0  #tiempo inicial
tf=6.1 #tiempo final
t=np.linspace(t0,tf,2000)
y=np.sin(2*np.pi*t)

plt.subplot(311)
plt.plot(t,y)

plt.ylabel('Amplitud')
plt.title('Muestreo cada 0.2 segundos')

#graficar la onda que se quiere muestrear y visualizar las muestras que se toman
ts1=0.2           #tiempo de muestreo 1
plt.subplot(312)
plt.plot(t,y,':b')
t1=np.arange(t0,tf,ts1)
y1=np.sin(2*np.pi*t1)
plt.plot(t1,y1,'or')


plt.ylabel('Amplitud')
#crear una barra vertical en cada punto donde se tomara una muestra
barv=np.linspace(-1,1,10)
for tt in t1:
    x=tt*(np.ones(10))
    plt.plot(x,barv,'-.k') 

plt.subplot(313)
plt.plot(t1,y1,'-or')

plt.ylabel('Amplitud')
plt.xlabel('Tiempo (segundos)')

##########################################################  
#que pasa cuando se selecciona el ts de forma erronea??
########################################################## 

plt.figure(2)
plt.subplot(311)
plt.plot(t,y)


plt.ylabel('Amplitud')
plt.title('Muestreo cada 1.2 segundos')

#graficar la onda que se quiere muestrear y visualizar las muestras que se toman
ts2=1.2
plt.subplot(312)
plt.plot(t,y,':b')
t1=np.arange(t0,tf,ts2)
y1=np.sin(2*np.pi*t1)
plt.plot(t1,y1,'or')

plt.ylabel('Amplitud')

for tt in t1:
    x=tt*(np.ones(10))
    plt.plot(x,barv,'-.k')
    
plt.subplot(313)
plt.plot(t1,y1,'-or')


plt.ylabel('Amplitud')
plt.xlabel('Tiempo (segundos)')
   
############################# 
plt.figure(3)
plt.subplot(311)
plt.plot(t,y)


plt.ylabel('Amplitud')
plt.title('Muestreo cada 0.67 segundos')

#graficar la onda que se quiere muestrear y visualizar las muestras que se toman
ts3=0.67
plt.subplot(312)
plt.plot(t,y,':b')
t1=np.arange(t0,tf,ts3)
y1=np.sin(2*np.pi*t1)
plt.plot(t1,y1,'or')


plt.ylabel('Amplitud')

for tt in t1:
    x=tt*(np.ones(10))
    plt.plot(x,barv,'-.k')
    
plt.subplot(313)
plt.plot(t1,y1,'-or')



plt.ylabel('Amplitud')
plt.xlabel('Tiempo (segundos)')


plt.show()

