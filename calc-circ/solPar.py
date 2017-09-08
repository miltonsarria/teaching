#Milton Orlando Sarria Paja
#USC 2017
#solucion parcial

import numpy as np
import math


def text2numbers(lines):
    x=[]
    numID=[]
    for line in lines:
      #de cada linea cada numero e ignorar el cambio de linea
      #que es el ultimo caracter
      data = line[:-1]
      #converti(x[-1:],x[-2:-1])r a flotantes y apilar en la lista X
      x.append([float(data[-1:]), float(data[-2:-1])])
      numID.append(data)
    #convertir la lista a un arreglo numpy
    x=np.array(x)
    return (x,numID)
    
file_name='data.txt'
hf = open(file_name,'r')
lines=hf.readlines()
hf.close()
#convertir los datos a valores numericos, la primer columna es el tiempo, la segunda datos
#se separan en vectores diferentes y se calcula la frecuencia de muestreo
x,numID=text2numbers(lines)

#definir parametros del circuito
f=60
L=10e-3
w=2*np.pi*f
z1=2
z2=1
z3=1j*w*L
#     
#     ____________________________________
#    |--> I1  |____|    | --> I2 |____|   |
#    |          z1      |          z3     |
#  /   \               _|                _|
# |  ~  | V           | |               | |
#  \ _ /              | | z2            | |z4
#    |                |_|               |_|
#    |                  |                 |
#    |__________________|_________________|
#
for ii in np.arange(x.shape[0]):
    d=x[ii]
    ids=numID[ii]

    da=d[0]
    db=d[1]*1e-3
    #casos especiales    #########################
    if (ids=='1144072458')|(ids=='1085899072')|(ids=='1118305239'):
       da=d[1]
       db=d[0]*1e-3  
       
    if (ids=='1143860873'):
       db=4*1e-3  
       
    if (ids== '92061276523'):
       da=2
       db=8*1e-3  
    ##################################################
        
    if (da==0)&(db==0): 
       da=9.
       db=3.*1e-3
    V=da+db*1e3
    z4=da+1/(1j*w*db)
    
    A =np.array([[z1+z2, -z2],\
                 [-z2  , z2+z3+z4]])
                 
    A1=np.array([[V  ,  -z2],\
                 [0.0,  z2+z3+z4]])
                 
    A2=np.array([[z1+z2, V],\
                 [-z2  , 0.0]])
    print('#########################################')
    print('Solucion para', d, ids)
    print(A)
    print('Con z4 y zl: ', z4, z3)

    
    detA =np.linalg.det(A)
    detA1=np.linalg.det(A1)
    detA2=np.linalg.det(A2)
    
    I1=detA1/detA
    I2=detA2/detA
    
    print('corriente en z es:', I2)
    print('I en z fasorial es:', np.abs(I2), np.angle(I2, deg=True))
    
    print('corriente total IT es:', I1)
    print('IT fasorial es:', np.abs(I1), np.angle(I1, deg=True))
    Zeq=V/I1
    print('la impedancia Z es:', Zeq)
    print('de forma polar:', np.abs(Zeq), np.angle(Zeq, deg=True))

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
