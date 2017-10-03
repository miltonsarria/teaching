#Milton Orlando Sarria Paja
#USC 2017
#analisis de fourier para datos de ondas periodicas guardados en archivos de texto
#la onda se ha contaminado con ruido sinusoidal
import matplotlib.pyplot as plt
import numpy as np
#importar la funcion para hacer el analisis de fourier
from fourierFunc import fourierAn

##################################################################################
##################################################################################
def text2numbers(lines):
    x=[]
    for line in lines:
      #de cada linea tomar por separado cada numero e ignorar el cambio de linea
      #que es el ultimo caracter
      data = line[:-1].split(',')
      #convertir a flotantes y apilar en la lista X
      x.append([float(data[0]), float(data[1])])
    #convertir la lista a un arreglo numpy
    x=np.array(x)
    return x
##################################################################################
##################################################################################
#CODIGO PRINCIPAL
##################################################################################
##################################################################################

#lectura del archivo de texto donde se encuentran los datos
file_name='sierra_ruido_sin.txt'
#file_name='sierra_ruido_ran.txt'

hf = open(file_name,'r')
lines=hf.readlines()
hf.close()
#convertir los datos a valores numericos, la primer columna es el tiempo, la segunda datos
#se separan en vectores diferentes y se calcula la frecuencia de muestreo
x=text2numbers(lines)
t=x[:,0]
y=x[:,1]
#fs es el inverso del periodo de muestreo, o la separacion, en tiempo, entre dos muestras consecutivas
Ts=t[1]-t[0] #incremento discreto o tiempo de muestreo Ts
Fs=1.0/(Ts)   #frecuencia de muestreo (inverso del tiempo de muestreo)
dF=Fs/x.size #incremento discreto en frecuencia
print(Fs)
plt.figure(1)
plt.plot(x[:,0],x[:,1])
plt.xlabel('tiempo - secs')
plt.ylabel('amplitud - volts')
###########################################
#aplicar transformada de fourier a los datos
absY,mYdb,pY=fourierAn(y)
#vector de frecuencias, desde -fs/2 a fs/2  (-pi<w<pi)
f=np.linspace(-Fs/2,Fs/2,absY.size)

#se grafican las 3000 muestras del lado positivo y 1000 muestras del lado negativo, esto se puede modificar a conveniencia
#y dependiendo del numero de muestras que se tengan
Nplot=3000

plt.figure(2)
plt.subplot(311)
plt.plot(f,absY)
plt.ylabel('|Y|')

plt.subplot(312)
plt.plot(f,mYdb)
plt.ylabel('En dB (20log10(|Y|)')

plt.subplot(313)
plt.plot(f,pY)
plt.ylabel('Angulo o fase rad')

plt.xlabel('Frecuencia - Hz')

plt.show()
