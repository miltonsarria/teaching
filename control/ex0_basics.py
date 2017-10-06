#Milton Orlando Sarria
#basics of control using numpy and scipy


import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#numpy can be used to compute polinomial roots from the coefficients or polinomial coefficients from roots

#A polynomial function
#ax^2+bx+c
#p=[a,b,c]

p=[1,6,9]
#roots of p
rp=np.roots(p)
print(rp)
#given the roots, compute the polynomial coefficients
#consider the factor (x+3)(x+4)(x+5)
rp=(-3,-4,-5)
p=np.poly(rp)
print(p)


#using scipy to define lti systems
num = [1, 2]
den = [1, 8, 7]
G = signal.lti(num, den)
print(G)

a = np.array([[0, 1,0], [0, 0,1],[-2,-3,-4]])
b = np.array([[0], [0],[1]])
c = np.array([[1, 2,0]])
d = np.array([[0]])

SS = signal.StateSpace(a, b, c, d)
print(SS)

#convert ss to tf
G=SS.to_tf()
print(G)
#step response
t,yout=G.step()
plt.plot(t,yout)
plt.show()








