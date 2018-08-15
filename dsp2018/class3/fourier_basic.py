from scipy.signal import get_window
import numpy as np
import matplotlib.pyplot as plt 

n = np.linspace(0,20, 300) 

x=np.cos(2*np.pi*n/8.)

w= get_window('hamming', x.size);

y=x*w

plt.plot(y)

plt.show()




