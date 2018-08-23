#Milton Orlando Sarria
#Procesamiento digital de senales
#USC

import numpy as np
import matplotlib.pyplot as plt
#se define una secuencia con ceros para acumular las sumas
def sinusoidal(k,n):
    A=k*np.pi
    fsin = A*np.sin(k*n)
    return fsin

n = np.linspace(0,14,1000)  #vector de tiempo
y=np.zeros(n.size)
##########################################
#se suman 3 sinusoidales y se grafica el resultado
##########################################
#para k=1
plt.subplot(411)
f1=sinusoidal(1,n)
plt.plot(n,f1)
y=y+f1
#para k=2
plt.subplot(412)
f2=sinusoidal(2,n)
plt.plot(n,f2)
y=y+f2
#para n=3
plt.subplot(413)
f3=sinusoidal(3,n)
plt.plot(n,f3)
y=y+f3
plt.subplot(414)
plt.plot(n,y)

plt.show()


