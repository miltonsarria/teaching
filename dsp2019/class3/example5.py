#Milton Orlando Sarria
#Procesamiento digital de senales
#USC
import numpy as np
import matplotlib.pyplot as plt

#definir una secuencia x de forma exponencial compleja
plt.figure(1, figsize=(9.5, 7))
#definir  numero de puntos
N = 30
#vector o arreglo para el eje horizantal
n = np.arange(N)
#secuencia compleja
x = np.exp(1j*2*np.pi*n/8)

plt.title('Sinusoidal compleja: x')
sinReal,=plt.plot(n, np.real(x),'--ob', label='Parte real')
sinImag,=plt.plot(n, np.imag(x),'--og', label='Parte imaginaria')

plt.legend(handles=[sinReal, sinImag])
plt.xlabel('valor de n')
plt.ylabel('valor de x[n]')
plt.show()


