#Milton Orlando Sarria
#Procesamiento digital de senales
#USC

import numpy as np
import matplotlib.pyplot as plt


#definir una secuencia x de forma manual
x=np.array([2.5,0,3,0,0,-2])

#definir una secuencia h de forma manual
h=np.array([1,0.7,0.4])

#graficar las secuencias
plt.subplot(311)
plt.title('Secuencias x[n], h[n], y[n]=x[n]*h[n]')
plt.ylabel('valor de x[n]')
plt.stem(range(x.size),x,'-.b')

plt.subplot(312)
plt.ylabel('valor de h[n]')

plt.stem(range(h.size),h,'-.g')

#realizar la convolucion entre x[n] y h[n]
y= np.convolve(x, h)
#graficar la secuencia y[n] resultante

plt.subplot(313)
plt.stem(range(y.size),y,'-.r')
plt.xlabel('valor de n')
plt.ylabel('valor de y[n]')
plt.show()


