#Milton Orlando Sarria Paja
#USC 2018
#solucion parcial 2
 
import numpy as np
import math

########################################################
def text2numbers(file_name):
    hf = open(file_name,'r')
    lines=hf.readlines()
    hf.close()

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
        
file_name='data_2018b.txt'
#convertir los datos a valores numericos
x,numID=text2numbers(file_name)

for ii in np.arange(x.shape[0]):
    d=x[ii]
    ids=numID[ii]

    A=d[1]
    B=d[0]
    if A==0:
        A = 7

    if B==0:
        B = 7
    print('#########################################')
    print('Solucion para',ids)
    print('A=',A,' B=',B)
    ##################################################
    print('Punto 1:')
    Zab=-1j*(A+B)
    Zbc=1j*(A*B)/2.
    Zca=5*(A+B)
    
    Vp=10*(A*B)
    ##################################################    
    Vab=Vp*unitC(0)
    Vbc=Vp*unitC(120)
    Vca=Vp*unitC(-120)

    IAB=Vab/Zab
    IBC=Vbc/Zbc
    ICA=Vca/Zca        
    
    Ia=IAB-ICA
    Ib=IBC-IAB
    Ic=ICA-IBC
    
    S1=Vab*np.conjugate(IAB)
    S2=Vbc*np.conjugate(IBC)
    S3=Vca*np.conjugate(ICA)
    
    St=S1+S2+S3
    print("vp: ",Vp)
    print('Iab:',IAB, 'Fasorial: ', np.abs(IAB), np.angle(IAB, deg=True))
    print('Ibc:',IBC, 'Fasorial: ', np.abs(IBC), np.angle(IBC, deg=True))
    print('Ica:',ICA, 'Fasorial: ', np.abs(ICA), np.angle(ICA, deg=True))    
    print('Ia:',Ia, 'Fasorial: ', np.abs(Ia), np.angle(Ia, deg=True))
    print('Ib:',Ib, 'Fasorial: ', np.abs(Ib), np.angle(Ib, deg=True))
    print('Ic:',Ic, 'Fasorial: ', np.abs(Ic), np.angle(Ic, deg=True))
            
    print('S1:',S1, 'Fasorial: ', np.abs(S1), np.angle(S1, deg=True))
    print('S2:',S2, 'Fasorial: ', np.abs(S2), np.angle(S2, deg=True))
    print('S3:',S3, 'Fasorial: ', np.abs(S3), np.angle(S3, deg=True))
    
    print('St:',St, 'Fasorial: ', np.abs(St), np.angle(St, deg=True))
    print('Fp:',np.real(St)/np.abs(St), 'Cos: ', np.cos(np.angle(St)))

    
    ##################################################       
    print('\n\nPunto 2:')
    Ra=A+B
    Zb=10*A-1j*(A+B)
    Rc=5*(A+B)
    Zc=Rc+1j*(A*B)
    
    Pc=20*(A*B)
    ##################################################    
    I1=np.sqrt(Pc/Rc)
    Vo=I1*Zc
    I2=Vo/Zb
    It=I1+I2
    Vt=(Ra+Zb*Zc/(Zb+Zc))*It


    St=Vt*np.conjugate(It)
    S1=Vo*np.conjugate(I1)
    S2=Vo*np.conjugate(I2)
    
    Sl=S1+S2
    
    print('Vo:',Vo, 'Fasorial: ', np.abs(Vo), np.angle(Vo, deg=True))
    print('I1:',I1, 'Fasorial: ', np.abs(I1), np.angle(I1,deg=True))    
    print('I2:',I2, 'Fasorial: ', np.abs(I2), np.angle(I2,deg=True))  
    print('It:',It, 'Fasorial: ', np.abs(It), np.angle(It,deg=True))  
    print('\n')
    print('Vt:',Vt, 'Fasorial: ', np.abs(Vt), np.angle(Vt, deg=True))
    print('S1:',S1, 'Fasorial: ', np.abs(S1), np.angle(S1, deg=True))
    print('S2:',S2, 'Fasorial: ', np.abs(S2), np.angle(S2, deg=True))
    print('St:',St, 'Fasorial: ', np.abs(St), np.angle(St, deg=True))
    print('En la carga: ')
    print('Sl:',Sl, 'Fasorial: ', np.abs(Sl), np.angle(Sl, deg=True))
    print('Fp:',np.real(Sl)/np.abs(Sl), 'Cos: ', np.cos(np.angle(Sl)))
    
    
    
    
    
   
   
   
   
   
   
   
   
   
   
   
   
   
