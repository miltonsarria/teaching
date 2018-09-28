#Milton Orlando Sarria
#analisis espectral de sinusoides

import matplotlib.pyplot as plt
import numpy as np
from fourierFunc import fourierAn

#definir la frecuencia de muestreo y generar un vector de tiempo hasta 5 segundos
fs=1e3
longitud = 5
t=np.linspace(1./fs,longitud,fs*longitud);

F=10            #frecuencia fundamental 10 hz
w=2*np.pi*F     #frecuencia angular
Vm=4            #valor de amplitud de la onda

#generar onda sinusoidal pura
x=Vm*np.cos(w*t)
#generar onda de ruido sinusoidal, alta frecuencia y baja amplitud
#usar una frecuencia 30 veces mayor a la inicial
ruido=2*np.cos(30*w*t)
#onda con ruido: sumar las dos sinusoidales
x_n=x+ruido

#calcular el espectro de las ondas limpias y contaminadas
absY,mYdb,pY=fourierAn(x)
absYx,mYxdb,pYx=fourierAn(x_n)
#vector de frecuencias, desde -fs/2 a fs/2  (-pi<w<pi)
f=np.linspace(-fs/2,fs/2,absY.size)

#visualizar las dos ondas, limpia y contaminada y sus espectros
plt.subplot(221)
plt.plot(t,x)
plt.title('onda sin ruido')

plt.subplot(222)
plt.plot(f,mYdb)
plt.title('Espectro onda sin ruido')

plt.subplot(223)
plt.plot(t,x_n)
plt.title('onda con ruido')

plt.subplot(224)
plt.plot(f,mYxdb)
plt.title('Espectro onda con ruido ')


plt.show()





