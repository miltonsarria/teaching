#Milton Orlando Sarria Paja
#USC 2017
#analisis de fourier para datos de ondas periodicas guardados en archivos de texto



import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.fftpack import fft, ifft
from scipy import signal

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
file_name='cuadrada2.txt'
hf = open(file_name,'r')
lines=hf.readlines()
hf.close()
#convertir los datos a valores numericos, la primer columna es el tiempo, la segunda datos
#se separan en vectores diferentes y se calcula la frecuencia de muestreo
x=text2numbers(lines)
t=x[:,0]
y=x[:,1]
#fs es el inverso del periodo de muestreo, o la separacion en tiempo de dos muestras consecutivas
dt=t[1]-t[0] #incremento discreto o tiempo de muestreo
Fs=1./(dt)   #frecuencia de muestreo (inverso del tiempo de muestreo)
dF=Fs/x.size #incremento discreto en frecuencia
plt.subplot(211)
plt.plot(x[:,0],x[:,1])
plt.xlabel('tiempo - secs')
plt.ylabel('amplitud - volts')

#aplicar transformada de fourier a los datos
Y = fft(y)
#calcular la magnitud de la primera parte del espectro
hN=int(math.floor((Y.size+1)/2))

absY = abs(Y[:hN])/(y.size)                               # Calcular el valor absoluto del lado positivo y normalizar por el num de muestras
absY[absY < np.finfo(float).eps] = np.finfo(float).eps    # Si hay ceros, reemplazar por un valor muy pequeno, para aplicar el log
mY = 20 * np.log10(absY) 

#vector de frecuencias, desde 0 a fs/2
f=np.linspace(0,Fs/2,hN)
plt.subplot(212)

#graficar las primeras 1000 muestras, esto se puede modificar a conveniencia
Nplot=1000
plt.stem(f[:Nplot],absY[:Nplot])
plt.xlabel('Frecuencia - Hz')
plt.ylabel('Magnitud del espectro')
plt.show()










