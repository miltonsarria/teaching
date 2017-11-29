#Milton Orlando Sarria Paja
#USC 2017
#solucion parcial  2

import numpy as np
import math
from sympy import  *
import control as ctrl
import matplotlib.pyplot as plt
from scipy import signal


def text2numbers(lines):
    x=[]
    numID=[]
    for line in lines:
      #leer el dato de cada linea e ignorar el cambio de linea
      data = line[:-1]
      #convertir (x[-1:],x[-2:-1]) a flotantes y apilar en la lista x
      x.append([float(data[-1:]), float(data[-2:-1])])
      numID.append(data)
    #convertir la lista a un arreglo numpy
    x=np.array(x)
    return (x,numID)
    
file_name='data.txt'
hf = open(file_name,'r')
lines=hf.readlines()
hf.close()
#convertir los datos a valores numericos
x,numID=text2numbers(lines)
#definir parametros del circuito
s=Symbol('s')
#     
#     _____________________________________
#    |--> I1  |____|    | --> I2           |  --> Vo
#    |          z1      |                  |
#  /   \               _|                 _|
# |  ~  | Vi          | |                | |
#  \ _ /              | | z2             | |z3
#    |                |_|                |_|
#    |                  |                  |
#    |__________________|__________________|
#

w=np.array([3,30,300])

for ii in np.arange(x.shape[0]):
    d=x[ii]
    ids=numID[ii]
    da=d[0]
    db=d[1]
    
    if (da==0): 
       da=5.
    if (db==0):
       db=5.
    #definir los valores que dependen del numero de identidad
    Z1=da
    Z2=da+s*db
    Z3=s*db
    Ze=Z2*Z3/(Z2+Z3)
    #aplicar divisor de voltaje
    Vd=Ze/(Ze+Z1)
    
    num=[db**2, da*db, 0]
    den=[db**2,3*da*db,da**2]
    #G = ctrl.tf(num, den)
        
    print('#########################################')
    print('Solucion para', [da, db], ids)
    print('vd',simplify(Vd))
    print('ze',simplify(Ze))
    print(num)    
    print(den)
    
    G1=signal.lti(num, den)
    
    omega, mag, phase  = signal.bode(G1)
    plt.subplot(211)
    
    plt.semilogx(omega, mag); 
    plt.grid()
    plt.title('Respuesta en frecuencia1');
    plt.ylabel('Magnitud');
    
    ###### punto 2
    H=db/(1+1j*w)+db/(da+1j*w)
    HdB=20*np.log10(abs(H))
    print 'H ',abs(H)
    print 'Hdb ', HdB
    
    num=[2*db, da*db+db]
    den=[1,da+1,da]
    print(num)    
    print(den)
    #G2 = ctrl.tf(num, den)
    #mag, phase, omega = ctrl.bode(G2)
    G2=signal.lti(num, den)
    omega, mag, phase  = signal.bode(G2)
    
    plt.subplot(212)
    plt.semilogx(omega, mag); 
    plt.grid()
    plt.title('Respuesta en frecuencia2');
    plt.ylabel('Magnitud');
    
    
    
    plt.show()
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
