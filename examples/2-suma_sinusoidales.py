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
a1=2./(n**2*np.pi**2)*np.cos(n*np.pi-1)
f1=a1*np.cos(n*t)
plt.plot(t,f1)
y=y+f1
#para n=2
plt.subplot(613)
n=2
a2=2./(n**2*np.pi**2)*np.cos(n*np.pi-1)
f2=a2*np.cos(n*t)
plt.plot(t,f2)
y=y+f2
#para n=3
plt.subplot(614)
n=3
a3=2./(n**2*np.pi**2)*np.cos(n*np.pi-1)
f3=a3*np.sin(n*t)
plt.plot(t,f3)
y=y+f3

plt.subplot(615)
plt.plot(t,y)

##########################################
# haciendo un proceso similar, se suman los armonicos de 1 a 50
##########################################

n=range(1,50,2)
y=np.ones(t.size)*1/2
for ii in n:
    aii=2./(ii**2*np.pi**2)*np.cos(ii*np.pi-1)
    fii=aii*np.cos(ii*t)
    y=y+fii
    
plt.subplot(616)    
plt.plot(t,y)
plt.show()







