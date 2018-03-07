#Milton Orlando Sarria Paja
#USC 2018
#solucion quiz 2

import numpy as np
import math

def unitC(angle):
    C=(np.cos(np.deg2rad(angle))+1j*np.sin(np.deg2rad(angle)))
    return C


Z1=20+1/(1j*2e-3*10)
Z2=1/(1j*4e-3*10)
Z3=50+(1j*2*10)


Z=Z1+Z2*Z3/(Z2+Z3)


print('Z=', Z, '; Polar:  |Z|=', np.abs(Z),'   theta=', np.angle(Z, deg=True))
    
V=10*unitC(75)
w=10

Z1=10*(1j*w*0.5)/(10+(1j*w*0.5))
Z2=1/(1j*w*1/20)


Vo=Z2/(Z1+Z2)*V

print('Z1=', Z1, '; Polar:  |Z1|=', np.abs(Z1),'   theta=', np.angle(Z1, deg=True))
print('Vo=', V, '; Polar:  |Vo|=', np.abs(Vo),'   theta=', np.angle(Vo, deg=True))
