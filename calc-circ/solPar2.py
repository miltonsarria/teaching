#Milton Orlando Sarria Paja
#USC 2017
#solucion parcial

import numpy as np
import math
from sympy import  *

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
# |  ~  | V           | |                | |
#  \ _ /              | | z2             | |z3
#    |                |_|                |_|
#    |                  |                  |
#    |__________________|__________________|
#
for ii in np.arange(x.shape[0]):
    d=x[ii]
    ids=numID[ii]
    da=d[0]
    db=d[1]
    #casos especiales    #########################
    if (ids=='1144072458')|(ids=='1085899072')|(ids=='1118305239'):
       da=d[1]
       db=d[0]
       
    if (ids=='1143860873'):
       db=4.
       
    if (ids== '92061276523'):
       da=2.
       db=8.
    ##################################################
        
    if (da==0)&(db==0): 
       da=9.
       db=3.
    #definir los valores que dependen del numero de identidad
    Z1=da
    Z2=da+s*db
    Z3=s*db
    Ze=Z2*Z3/(Z2+Z3)
    #aplicar divisor de voltaje
    Vd=Ze/(Ze+Z1)
    
    num=[db**2, da*db, 0]
    den=[db**2,3*da*db,da**2]
    
    
    print('#########################################')
    print('Solucion para', d, ids)
    print(simplify(Vd))
    print(num)    
    print(den)
    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
