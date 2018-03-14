import numpy as np
import matplotlib.pyplot as plt

n=np.arange(1000)
x=np.cos(np.pi*n/8)

n=np.arange(40)
arg=np.pi*(n-20)/10

h=np.sin(arg)/(arg)
h[20]=1
y=np.convolve(x,h)

plt.plot(h)
plt.figure()
plt.plot(x)
plt.plot(y)
plt.show()
