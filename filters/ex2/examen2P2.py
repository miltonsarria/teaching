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
import wav_process as wp
from wav_rw import wavread, wavwrite
from scipy.signal import get_window


##########################################
#BLOQUE 1
#definir archivo de audio
archivo='prueba1_exam.wav'
######################
#rango de frecuencias para ver una banda especifica
rango =[0.0, 20000.0]
(fs,x)=wavread('sound/'+archivo)
#normalizar
x=x/np.max(np.abs(x))
#modificar la siguiente linea para imprimir la frecuencia de muestreo
print('frecuencia de muestreo: ')

#graficar espectrograma y espectro promedio
window = 'hamming'
long_ventana =  0.02 #en segundos
incremento   =  0.008#en segundos
#en muestras
M = int(fs * long_ventana) #ventana
H = int(fs * incremento)   #incremento
N = 1024                   #numero de puntos en fft
#generar ventana
w = get_window(window, M)
#obtener la transformada de fourier del archivo de audio (magnitud y la fase)
mX, pX = wp.stftAnal(x, w, N, H)

#Graficar archivo de audio y su representacion en  frecuencia
t=np.arange(x.size)/float(fs)        #vector de tiempo
Freq=np.linspace(0,fs/2,mX.shape[1]) #vector de frecuencia

#graficar audio
plt.subplot(2,1,1)
plt.plot(t, x)
plt.axis([0, x.size/float(fs), min(x), max(x)])
plt.ylabel('amplitud')
plt.xlabel('tiempo')
plt.title('audio original')

#graficar el promedio del espectro de todo el archivo de audio
bins=(Freq>rango[0]) & (Freq<rango[1])
mX=np.mean(mX,axis=0)
plt.subplot(2,1,2)
plt.plot(Freq[bins],mX[bins])

plt.xlabel('Frequencia [Hz]')
plt.ylabel('Magnitud en dB')

##########################################
#BLOQUE 2 para habilitar este bloque debe quitar las comillas ''' de las lineas 66 y 102
'''
#disenar filtro que permita pasar unicamente las componentes de frecuencia con informacion relevante
#modificar los parametros que sean necesarios
frec_norm=0.8
longitud_filtro=3
b1 = signal.firwin(longitud_filtro, frec_norm, window='hamming', pass_zero=True)

#obtener la respuesta en frecuencia
omega, mag = signal.freqz(b1)

#filtrar la onda original
x1=signal.lfilter(b1, [1.0],x)
#usar fourier para ilustrar la salida del filtro
mX, pX = wp.stftAnal(x1, w, N, H)
#
plt.figure(2)
#graficar audio filtrado
plt.subplot(2,2,1)
plt.plot(t, x1)
plt.axis([0, x1.size/float(fs), min(x1), max(x1)])
plt.ylabel('amplitud')
plt.title('audio filtrado')

mX=np.mean(mX,axis=0)
plt.subplot(2,2,2)
plt.plot(Freq[bins],mX[bins])

plt.title('Espectro')
plt.xlabel('Frequencia [Hz]')
plt.ylabel('Magnitud en dB')

#ilustrar la respuesta en frecuencia del filtro
plt.subplot(2,2,3)
plt.title('Respuesta en frecuencia de filtro')
plt.plot(omega, 20 * np.log10(abs(mag)), 'b')
plt.ylabel('Amplitud [dB]')
'''
##########################################  
#BLOQUE 3 eliminar las comillas ''' de las lineas 105 y 125 para habilitar el siguiente bloque
'''
#remuestrear la senal filtrada y guardarla en un nuevo archivo de audio
#definir la nueva frecuencia de muestreo
nfs=1000

##Remuestrear, reducir la frecuencia en un factor determinado
factor=fs/nfs
new_samples=int(x1.size/factor)
nx1 = signal.resample(x1, new_samples)   #nueva senal remuestreada
#graficar la nueva senal de audio
t=np.arange(nx1.size)/float(nfs)         #vector de tiempo
plt.subplot(2,2,4)
plt.plot(t,nx1)
plt.title('senal remuestreada')
plt.ylabel('amplitud')
plt.xlabel('tiempo')


archivo='nuevo_audio1.wav'
wavwrite(nx1, nfs, 'sound/'+archivo)
'''
plt.show()



