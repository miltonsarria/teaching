import numpy as np
import matplotlib.pyplot as plt

#generar la secuencia h
n=np.arange(40)
arg=np.pi*(n-20)/10
h=np.sin(arg)/(arg)
h[20]=1


#generar la secuencia x
n=np.arange(1000)
x=np.cos(np.pi*n/4)

#generar la secuencia y=x*h
y=np.convolve(x,h)

#graficar las secuencias
plt.plot(h)
plt.figure()
plt.plot(x)
plt.plot(y)
plt.show()
