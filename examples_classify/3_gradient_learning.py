#Milton Orlando Sarria
#elementos basicos de aprendizaje, ajustar una linea recta a datos
#problema de regresion

import matplotlib.pyplot as plt
import numpy as np


#generar datos de forma aleatoria, inicialmente con cruce por cero
mu=0;
sigma=3
N=200
x=np.arange(N)
y=3*x+np.random.normal(mu, sigma, N)

plt.plot(x,y,'.r')
plt.plot(x,3*x,'--b')


def gradiente(y,x,y_hat):
    
    dEm=np.sum((y_hat-y)*x)
    Et=1/2*np.sum((y_hat-y)**2)
    return dEm,Et
    
    
iter = 500
alpha=1e-8
#buscar entre -50 y 50
m=np.random.randint(-5, 9)
M=[]
E=[]
grad=0;
for i in range(iter):
     y_hat=m*x
     gd,e=gradiente(y,x,y_hat)
     m=m-alpha*gd
     M.append(m)
     E.append(e)


plt.plot(x,m*x,'--k')

Et=[]
M_=np.linspace(-5,9,100)
for m_ in M_:
    y_hat=m_*x
    Et.append(1/2*np.sum((y_hat-y)**2))


plt.figure(2)
plt.plot(M_,Et)
plt.plot(M,E,'or')
print(M)

plt.show()
