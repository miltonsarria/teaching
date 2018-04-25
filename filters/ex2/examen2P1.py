#Examen 2
#Abril 25 - 2018
#procesamiento digital de senales
#universidad santiago de cali
#Nombre:
#ID:
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('tools/')
from fourierFunc import fourierAn


##########################################
#BLOQUE 1
#definir la frecuencia de muestreo
Fs=1

tf=5 #tiempo final
#definir la secuencia de tiempo hasta 5 segundos
nT=np.linspace(1./Fs,tf,Fs*tf);

#generar secuencia discreta x[n]
x=2*np.sin(12*np.pi*nT)+3*np.cos(40*np.pi*nT)

#usar fourier para identificar las componentes frecuenciales
absX,Xdb,pX=fourierAn(x)
f=np.linspace(-Fs/2,Fs/2,Xdb.size)

#visualizar los resultados del analisis hecho con transformada de fourier

plt.subplot(211)
plt.plot(nT,x)
plt.ylabel('x[n]')
plt.xlabel('tiempo - s')

plt.subplot(212)
plt.plot(f,Xdb)
plt.ylabel('|X| en dB')
plt.xlabel('Frecuencia - Hz')


##########################################
#BLOQUE 2  eliminar las comillas de la linea 46 y linea 79
'''
#disenar filtro que permita pasar unicamente la componente de frecuencia mas baja
#modificar los parametros que sean necesarios
frec_norm=0.8
longitud_filtro=3
b1 = signal.firwin(longitud_filtro, frec_norm, window='hamming', pass_zero=True)
#obtener la respuesta en frecuencia
w, h = signal.freqz(b1)

#filtrar la onda con el filtro numero 1
x1=signal.lfilter(b1, [1.0],x)
#usar fourier para ilustrar el resultado del filtro
absX1,X1db,pX1=fourierAn(x1)
#

plt.figure(2)
#ilustrar la respuesta en frecuencia del filtro
plt.subplot(311)
plt.title('Respuesta en frecuencia de filtro digital numero 1')
plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.ylabel('Amplitud [dB]', color='b')

#ilustrar los resultados
plt.subplot(312)
plt.plot(nT,x1)
plt.ylabel('x1[n] - filtrada')
plt.xlabel('tiempo - s')

plt.subplot(313)
plt.plot(f,X1db)
plt.ylabel('|X1| en dB')
plt.xlabel('Frecuencia - Hz')

'''

plt.show()




