#Milton Orlando Sarria
#Procesamiento digital de senales
#USC

import numpy as np
import matplotlib.pyplot as plt
n = np.linspace(0,14,1000)  #vector de tiempo
#se define una secuencia con ceros para acumular las sumas
y=np.zeros(n.size)
##########################################
#se suman 3 sinusoidales y se grafica el resultado
##########################################
#para k=1
plt.subplot(411)
k=1
A1=k*np.pi
f1=A1*np.sin(k*n)
plt.plot(n,f1)
y=y+f1
#para k=2
plt.subplot(412)
k=2
A2=k*np.pi
f2=A2*np.sin(k*n)
plt.plot(n,f2)
y=y+f2
#para n=3
plt.subplot(413)
k=3
A3=k*np.pi
f3=A3*np.sin(k*n)
plt.plot(n,f3)
y=y+f3
plt.subplot(414)
plt.plot(n,y)




