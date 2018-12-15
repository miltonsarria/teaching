#Milton Orlando Sarria
#Procesamiento digital de senales


#Manejo de secuencias discretas usando Python
#Es necesario usar dos paquetes, numpy y matplotlib, son herramientas que ya vienen por defecto con el 
#python que instala anaconda

#numpy es una herramienta para manejo numerico, operaciones matriciales, vectores....
#recomiendo seguir el tutorial basico para familiarizarse con la herramienta
#https://docs.scipy.org/doc/numpy-dev/user/quickstart.html

#matplotlib es un paquete para visualizar datos, permite realizar gran cantidad de graficos
#visitar la siguiente pagina para familiarizarce con la herramienta:
#https://matplotlib.org/#

import numpy as np
import matplotlib.pyplot as plt


#definir una secuencia x de forma manual, notar que se requiere decir explicitamente que es un
#arreglo de numpy:
x=np.array([4,6,2,4,2,6,1,8,7,9,5,3])
#definir la secuencia n, para definir los indices en el eje horizontal
n = range(x.size)

#graficar la secuencia x vs la secuencia n
plt.stem(n, x, '-.')
plt.xlabel('valor de n')
plt.ylabel('valor de x[n]')
plt.title('mostar una secuencia x[n]')
plt.show()


