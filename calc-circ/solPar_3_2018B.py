#Milton Orlando Sarria Paja
#USC 2017
#solucion parcial 3

import numpy as np
import math


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
########################################################
def unitC(angle):
    C=(np.cos(np.deg2rad(angle))+1j*np.sin(np.deg2rad(angle)))
    return C

########################################################    
file_name='data_2018b.txt'
hf = open(file_name,'r')
lines=hf.readlines()
hf.close()
#convertir los datos a valores numericos
x,numID=text2numbers(lines)
#definir parametros que son fijos
Vp=120.0
r3=np.sqrt(3)
r2=np.sqrt(2)
########################################################    
for ii in np.arange(x.shape[0]):
    d=x[ii]
    ids=numID[ii]

    A=d[1]
    B=d[0]
    if A==0:
        A = 5

    if B==0:
        B = 5
        
    print('#########################################')
    print('Solucion para',ids)
    print('A=',A,' B=',B)
    #1) definir los valores que dependen del numero de identidad
    ZAB=3*B+1j*5*A
    ZBC=2*A+1j*5*B
    ZCA=B+1j*10*A        
    
    theta=10*A
    #calcular voltaje de linea usando el de fase
    Van=Vp*unitC(theta)
    Vbn=Vp*unitC(theta-120)  
    Vcn=Vp*unitC(theta+120)
    
    VAB=Van-Vbn
    VBC=Vbn-Vcn
    VCA=Vcn-Van
    #calcular corrientes sobre cada impedancia            
    IAB=VAB/ZAB
    IBC=VBC/ZBC
    ICA=VCA/ZCA    
    #Realizar calculos de corrientes de linea
    Ia=IAB-ICA
    Ib=IBC-IAB
    Ic=ICA-IBC
    

    S=VAB*np.conjugate(IAB)+VBC*np.conjugate(IBC)+VCA*np.conjugate(ICA)

    print('1)---------------')   
    print('VAB:   ', np.abs(VAB),np.angle(VAB, deg=True))
    print('VBC:   ', np.abs(VBC),np.angle(VBC, deg=True))
    print('VCA:   ', np.abs(VCA),np.angle(VCA, deg=True))
    print('IAB: C ',IAB,' P:' ,np.abs(IAB),np.angle(IAB, deg=True))
    print('IBC: C ',IBC,' P:' ,np.abs(IBC),np.angle(IBC, deg=True))
    print('ICA: C ',ICA,' P:' ,np.abs(ICA),np.angle(ICA, deg=True))

    print('Ia: C  ',Ia,'  P:' ,np.abs(Ia),np.angle(Ia, deg=True))
    print('Ib: C  ',Ib,'  P:' ,np.abs(Ib),np.angle(Ib, deg=True))
    print('Ic: C  ',Ic,'  P:' ,np.abs(Ic),np.angle(Ic, deg=True))
    
    print('P=', S.real, ' S=', np.abs(S),'   fp=', S.real/np.abs(S))
    
    #2)     
    Vrms=15*B/r2*unitC(-50)
    Irms=5*A/r2*unitC(-70)
    S=Vrms*np.conjugate(Irms)
    print('2)---------------')
    print('|V|=', np.abs(Vrms), '  |I|=', np.abs(Irms))
    print('S=', S, '  |S|=', np.abs(S),'   P=', S.real,'   Q=', S.imag, '   fp=', S.real/np.abs(S))
    Z=Vrms/Irms
    print('Z=', Z, '; Polar:  |Z|=', np.abs(Z),'   theta=', np.angle(Z, deg=True))
    
    #3) 
    print('3)---------------')    
    M  = 1j*(A+B)
    Z1 = 3*A
    Z2 = -1j*(A*B)
    Z3 = 1j*3*B
    Z4 = 1j*A*B
    Z5 = A*B
    V  = 10*A*B
    
    AA =np.array([[Z1+Z2+Z3,  -(Z3+M)],\
                 [-(Z3+M)  ,  Z3+Z4+Z5+2*M]])
                 
    A1=np.array([[V    ,  -(Z3+M)],\
                 [0.0  ,  Z3+Z4+Z5+2*M]])
                 
    A2=np.array([[Z1+Z2+Z3,  V],\
                 [-(Z3+M) ,  0.0]]) 
     
    detA =np.linalg.det(AA)
    detA1=np.linalg.det(A1)
    detA2=np.linalg.det(A2)
    
    I1=detA1/detA
    I2=detA2/detA
    Vo = Z5*I2
    print(AA)
    print('I1', I1, 'Polar: ',np.abs(I1),np.angle(I1, deg=True))
    print('I2', I2, 'Polar: ',np.abs(I2),np.angle(I2, deg=True))
    print('Vo', Vo, 'Polar: ',np.abs(Vo),np.angle(Vo, deg=True))    
    
    #4) 
    print('4)---------------')
    V = 100
    Z2   = (5*A-1j*(A*B))/16
    Zent = B+Z2
    I1 = V/Zent
    I2 = -1/4.*I1
    Vo = -1j*(A*B)*I2
    S  = V * np.conjugate(I1)
    
    print('Zi', Zent, 'Polar: ',np.abs(Zent),np.angle(Zent, deg=True))
    print('I1', I1, 'Polar: ',np.abs(I1),np.angle(I1, deg=True))
    print('I2', I2, 'Polar: ',np.abs(I2),np.angle(I2, deg=True))
    print('Vo', Vo, 'Polar: ',np.abs(Vo),np.angle(Vo, deg=True))    
    print('S', S, 'Polar: ',np.abs(S),np.angle(S, deg=True))    
    
    print('\n\n---------------')
    
    
    
    
    
    
    
    
    
