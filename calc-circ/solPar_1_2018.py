#Milton Orlando Sarria Paja
#USC 2017
#solucion parcial 1
 
import numpy as np
import math

########################################################
def text2numbers(lines):
    x=[]
    numID=[]
    for line in lines:
      #leer el dato de cada linea e ignorar el cambio de linea
      data = line[:-1]
      #separar los dos ultimos
      x.append([float(data[-1:]), float(data[-2:-1])])
      numID.append(data)
    #convertir la lista a un arreglo numpy
    x=np.array(x)
    return (x,numID)
########################################################
def unitC(angle):
    C=(np.cos(np.deg2rad(angle))+1j*np.sin(np.deg2rad(angle)))
    return C
########################################################    
        
file_name='data_2018.txt'
hf = open(file_name,'r')
lines=hf.readlines()
hf.close()
#convertir los datos a valores numericos
x,numID=text2numbers(lines)

#     
#     _____________________________________
#    |--> I1  |____|    | --> I2  |____|   |
#    |          z1      |           z3     |
#  /   \               _|                 _|
# |  ~  | V           | |                | |
#  \ _ /              | | z2             | |z4
#    |                |_|                |_|
#    |                  |                  |
#    |__________________|__________________|
#
for ii in np.arange(x.shape[0]):
    d=x[ii]
    ids=numID[ii]

    A=d[1]
    B=d[0]
    
    ##################################################
    #definir parametros del circuito
    
    L  = B      #valor del inductor
    w  = A+B    #frecuencia angular en rad/seg
    Z  = A+1j*B*w #impedancia
    Rs = A
    V  = A*B
    if A==0:
        V = B
    ##################################################
    ZL=1j*w*L
    Zp=ZL*Z/(ZL+Z)
    
    Vo= Zp/(Zp+Rs)*V
    Iz=Vo/Z
    print('#########################################')
    print('Solucion para',ids)
    print('A=',A,' B=',B)
    print('Punto 1')
    print('ZL:',ZL, 'Fasorial: ', np.abs(ZL), np.angle(ZL, deg=True))
    print('Z:',Z, 'Fasorial: ', np.abs(Z), np.angle(Z, deg=True))
    print('Zp:',Zp, 'Fasorial: ', np.abs(Zp), np.angle(Zp, deg=True))
    print('Vo:',Vo, 'Fasorial: ', np.abs(Vo), np.angle(Vo, deg=True))    
    print('Iz:',Iz, 'Fasorial: ', np.abs(Iz), np.angle(Iz, deg=True))           
    print('Punto 2')        
    
    #z=(j4w+2)/(2+jw)
    w=A
    Z1=(1j*4*w+2)/(2+1j*w)
    w=B
    Z2=(1j*4*w+2)/(2+1j*w)
    print('Z1:',Z1, 'Fasorial: ', np.abs(Z1), np.angle(Z1, deg=True))
    print('Z2:',Z2, 'Fasorial: ', np.abs(Z2), np.angle(Z2, deg=True))
    print('\n')
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
