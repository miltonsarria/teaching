#Milton Orlando Sarria
#analisis espectral de sinusoides

import matplotlib.pyplot as plt
import numpy as np
from fourierFunc import fourierAn

#definir la frecuencia de muestreo y generar un vector de tiempo hasta 5 segundos
Fs=1e3
t,T=np.linspace(1./Fs,5,Fs*5,retstep=True);

F=10            #frecuencia fundamental 10 hz
w=2*np.pi*5     #frecuencia angular
Vm=4            #valor de amplitud de la onda

#generar onda sinusoidal pura
y=Vm*np.cos(w*t)
#generar onda de ruido sinusoidal, alta frecuencia y baja amplitud
x=2*np.cos(2*np.pi*370*t)
#onda con ruido
yx=y+x
#calcular el espectro de las ondas limpias y contaminadas
absY,mYdb,pY=fourierAn(y)
absYx,mYxdb,pYx=fourierAn(yx)
#vector de frecuencias, desde -fs/2 a fs/2  (-pi<w<pi)
f=np.linspace(-Fs/2,Fs/2,absY.size)

#visualizar las dos ondas, limpia y contaminada y sus espectros
plt.subplot(221)
plt.plot(t,y)
plt.title('onda sin ruido')

plt.subplot(222)
plt.plot(f,mYdb)
plt.title('Espectro onda sin ruido')

plt.subplot(223)
plt.plot(t,yx)
plt.title('onda con ruido')

plt.subplot(224)
plt.plot(f,mYxdb)
plt.title('Espectro onda con ruido ')


plt.show()





