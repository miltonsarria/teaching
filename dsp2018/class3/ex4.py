#Milton Orlando Sarria
#Procesamiento digital de senales
#USC

import numpy as np
import matplotlib.pyplot as plt


#definir una secuencia x de forma exponencial. primero se define los valores del eje horizontal
#en este caso se una linspace de numpy
n = np.linspace(0,20, 30)  #que hace esta funcion?
#se define la secuencia sinusoidal
x = np.exp(-n)
#graficar la secuencia x vs la secuencia n
plt.stem(n, x, '-.b')
plt.xlabel('valor de n')
plt.ylabel('valor de x[n]')
plt.title('mostar una secuencia exponencial')
plt.show()


