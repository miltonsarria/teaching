#Milton Orlando Sarria Paja
#USC 2018 B
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
        
file_name='data_2019A.txt'
hf = open(file_name,'r')
lines=hf.readlines()
hf.close()
#convertir los datos a valores numericos
x,numID=text2numbers(lines)
for ii in np.arange(x.shape[0]):
    d=x[ii]
    ids=numID[ii]

    A=d[0]
    B=d[1]

    if A==0:
        A = 7

    if B==0:
        B = 7

    ##################################################
    #1) definir parametros del circuito

    L1  = 1j*4*B      #valor del inductor 1
    L2  = 1j*2*B      #valor del inductor 2
    R1  = 3*A
    R2  = A+B
    C   = -1j*A
    ##################################################
    Z1 = L1+R1
    Z2 = (C+L2)*R2/((C+L2)+R2)

    Zeq = Z1+Z2
    
    V=10*A*B*unitC(20)
    
    I = V/Zeq
    ##################################################
    #2) definir parametros del circuito
    R1 = 3*(A+B)
    L1 = 1j*8*B
    C  = -1j*10*A
    L2 = 1j*(A+B)
    V  = 5*(A*B)
    #A = 2    
    ##################################################
    AA =np.array([[R1/C+R1/L1+1,  -R1/L1],\
                 [A/C+1/L1  ,  -(1/L1+1/L2)]])
                 
    A1=np.array([[V,  -R1/L1],\
                 [0  ,  -(1/L1+1/L2)]])
                 
    A2=np.array([[R1/C+R1/L1+1,  V],\
                 [A/C+1/L1  ,  0]])
     
    detA =np.linalg.det(AA)
    detA1=np.linalg.det(A1)
    detA2=np.linalg.det(A2)
    
    V1=detA1/detA
    V2=detA2/detA
    Ix = V1/C
    ##################################################
    #3) Definir parametros
    Z3=3+1j*4
    V3=5*A*B*unitC(10*A)
    I3=V3/Z3
    S3=1/2*V3*np.conjugate(I3)   
        
    ##################################################
    print('#########################################')
    print('Solucion para',ids)
    print('A=',A,' B=',B)
    print('\nPunto 1')
    print('Z1:',Z1, 'Fasorial: ', np.abs(Z1),'<',np.angle(Z1, deg=True))
    print('Z2:',Z2, 'Fasorial: ', np.abs(Z2),'<', np.angle(Z2, deg=True))    
    print('Zeq:',Zeq, 'Fasorial: ', np.abs(Zeq),'<', np.angle(Zeq, deg=True))    
    print('I:',I, 'Fasorial: ', np.abs(I),'<', np.angle(I, deg=True))           
    
    print("\nPunto 2")
    print(AA)
    print('V1:',V1, 'Fasorial: ', np.abs(V1),'<', np.angle(V1, deg=True))
    print('V2:',V2, 'Fasorial: ', np.abs(V2),'<', np.angle(V2, deg=True))    
    print('Ix:',Ix, 'Fasorial: ', np.abs(Ix),'<', np.angle(Ix, deg=True))
    
    print("\nPunto 3")
    print('V:',V3, 'Fasorial: ', np.abs(V3),'<', np.angle(V3, deg=True))
    print('I:',I3, 'Fasorial: ', np.abs(I3),'<', np.angle(I3, deg=True))
    print('S:',S3, 'Fasorial: ', np.abs(S3),'<', np.angle(S3, deg=True))    
    print('Fp:',np.real(S3)/np.abs(S3), 'Cos: ', np.cos(np.angle(S3)))
    print("\n\n")
    
    
