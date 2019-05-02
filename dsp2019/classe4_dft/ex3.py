import matplotlib.pyplot as plt
import numpy as np

#inner product es el producto punto, o la multiplicacion punto a punto y suma de dos secuencias
#<x,s*>

#definir una secuencia
fs=100
t=np.linspace(1./fs,1,fs);
w=2*np.pi*5

x=np.sign(np.cos(w*t))+1
N = x.size #numero de muestras
mX = () #para guardar la magnitud de X(k)
pX = () #para guardar el angulo de X(k)
plt.figure(1, figsize=(9.5, 6))

plt.subplot(3,1,1)
plt.plot(x,marker='o',color='b', lw=1.5)
plt.axis([0,N-1,-0.5,2.5])
plt.title('x = square wave', fontsize=18)

#realizar el proceso para N sinusoidales complejas, k=0, 1, 2...7   (N-1)
for k in range(N):
  s = np.exp(-1j*2*np.pi*k/N*np.arange(N))
  X = x @ s #sum(x*s)
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


Et=(np.abs(x)**2).sum()
print(Et)
Ef=(1./mX.size*mX**2).sum()
print(Ef)
