import matplotlib.pyplot as plt
import numpy as np

#inner product es el producto punto, o la multiplicacion punto a punto y suma de dos secuencias
#<x,s*>

#definir la secuencia a la cual se le quiere aplicad la DFT
x = np.array([1,1,1,1,-1,-1,-1,-1])
N = 8 #numero de muestras
mX = () #para guardar la magnitud de X(k)
pX = () #para guardar el angulo de X(k)
plt.figure(1, figsize=(9.5, 6))

plt.subplot(3,1,1)
plt.plot(x,marker='x',color='b', lw=1.5)
plt.axis([0,N-1,-1.5,1.5])
plt.title('x = [1,1,1,1,-1,-1,-1,-1]', fontsize=18)

#realizar el proceso para 8 sinusoidales complejas, k=0, 1, 2...7   (N-1)
for k in range(8):
  s = np.exp(1j*2*np.pi*k/N*np.arange(N))
  X = sum(x*np.conjugate(s))
  mX = np.append(mX, np.abs(X))
  pX = np.append(pX, np.angle(X))

plt.subplot(3,1,2)
plt.plot(mX, marker='x', color='r', lw=1.5)
plt.title('$abs(<x,s_k>)$', fontsize=18)

plt.subplot(3,1,3)
plt.plot(pX, marker='x', color='c', lw=1.5)
plt.title('$angle(<x,s_k>)$', fontsize=18)

plt.tight_layout()
plt.savefig('inner-product.png')
plt.show()
