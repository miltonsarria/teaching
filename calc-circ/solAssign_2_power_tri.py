#Milton Orlando Sarria Paja
#USC 2018
#solucion parcial 2
 
import numpy as np
import math


########################################################
def unitC(angle):
    C=(np.cos(np.deg2rad(angle))+1j*np.sin(np.deg2rad(angle)))
    return C


print('#########################################')
print('Solucion para tarea 1')
##################################################
Zab=10-1j*5
Zbc=16
Zca=8+1j*6
Vp=440
##################################################
Vab=Vp*unitC(0)
Vbc=Vp*unitC(-120)
Vca=Vp*unitC(120)

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
print('IAB:',IAB, 'Fasorial: ', np.abs(IAB), np.angle(IAB, deg=True))
print('IBC:',IBC, 'Fasorial: ', np.abs(IBC), np.angle(IBC, deg=True))
print('ICA:',ICA, 'Fasorial: ', np.abs(ICA), np.angle(ICA, deg=True))


print('Ia:',Ia, 'Fasorial: ', np.abs(Ia), np.angle(Ia, deg=True))
print('Ib:',Ib, 'Fasorial: ', np.abs(Ib), np.angle(Ib, deg=True))
print('Ic:',Ic, 'Fasorial: ', np.abs(Ic), np.angle(Ic, deg=True))

print('S1:',S1, 'Fasorial: ', np.abs(S1), np.angle(S1, deg=True))
print('S2:',S2, 'Fasorial: ', np.abs(S2), np.angle(S2, deg=True))
print('S3:',S3, 'Fasorial: ', np.abs(S3), np.angle(S3, deg=True))

print('St:',St, 'Fasorial: ', np.abs(St), np.angle(St, deg=True))
print('Fp:',np.real(St)/np.abs(St), 'Cos: ', np.cos(np.angle(St)))


##################################################   
print('\n\nSolución para tarea 2:')
Ra=20
Zb=30-1j*10
Rc=60
Zc=Rc+1j*20

Pc=400
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





   
   
   
   
   
   
   
   
   
   
   
   
   
