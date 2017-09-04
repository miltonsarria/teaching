#Milton Orlando Sarria
#Procesamiento digital de senales
#USC

import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0,14,1000)  #vector de tiempo
#se define una secuencia con ceros para acumular las sumas
y=np.zeros(t.size)
##########################################
#se suman los primeros 4 armonicos y se grafica el resultado
##########################################
#
#para n=0
plt.subplot(611)
f0=np.ones(t.size)*1/2
plt.plot(t,f0)
y=y+f0
#para n=1
plt.subplot(612)
n=1
b1=2./(n*np.pi)
f2=b1*np.sin(n*t)
plt.plot(t,f2)
y=y+f2
#para n=3
plt.subplot(613)
n=3
b3=2./(n*np.pi)
f3=b3*np.sin(n*t)
plt.plot(t,f3)
y=y+f3
#para n=5
plt.subplot(614)
n=5
b5=2./(n*np.pi)
f5=b5*np.sin(n*t)
plt.plot(t,f5)
y=y+f5

plt.subplot(615)
plt.plot(t,y)

##########################################
# haciendo un proceso similar, se suman los armonicos de 1 a 50
##########################################

n=range(1,50,2)
y=np.ones(t.size)*1/2
for ii in n:
    bii=4./(ii*np.pi)
    fii=bii*np.sin(ii*t)
    y=y+fii
    
plt.subplot(616)    
plt.plot(t,y)
plt.show()







