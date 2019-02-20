import numpy as np
import matplotlib.pyplot as plt


#definir una secuencia x de forma manual, notar que se requiere decir explicitamente que es un
#como una lista
y=[4,3,5,6,1,7,8,1,0,9,3,4]
#arreglo de numpy:
x=np.array([4,6,2,4,2,6,1,8,7,9,5,3])
#secuencia n, para definir los indices en el eje horizontal


#graficar la secuencia x
plt.stem(y, '-.')
plt.ylabel('valor de y[n]')
plt.title('mostar una secuencia y[n]')

plt.figure(2)
#graficar la secuencia x
plt.stem(x, '-.')
plt.ylabel('valor de x[n]')
plt.title('mostar una secuencia x[n]')

plt.show()
