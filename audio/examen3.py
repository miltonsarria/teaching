#Examen 2
#Octubre 11 - 2017
#procesamiento digital de senales
#universidad santiago de cali
#Nombre:
#ID:
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
#from fourierFunc import fourierAn
import wav_process as wp
from wav_rw import wavread, wavwrite
from scipy.signal import get_window

##########################################
#BLOQUE 1

#definir archivo de audio
archivo='/home/sarria/Documents/2017B/dsp-python/audio/sound/prueba1_exam.wav'
######################
# modificar el rango de frecuencias para ver una banda especifica
rango =[0.0, 20000.0]
(fs,x)=wavread(archivo)
#normalizar
x=x/np.max(np.abs(x))
print('frecuencia de muestreo: ')
#graficar espectrograma y espectro
window = 'hamming'
long_ventana =  0.02 #en segundos
incremento   =  0.01#en segundos
#en muestras
M = int(fs * long_ventana)
H = int(fs * incremento)
N = 1024
#generar ventana
w = get_window(window, M)
#obtener la transformada de fourier del archivo de audio (magnitud y la fase)
mX, pX = wp.stftAnal(x, w, N, H)

#Graficar archivo de audio y su representacion en  frecuencia

t=np.arange(x.size)/float(fs) #vector de tiempo
Freq=np.linspace(0,fs/2,mX.shape[1]) #vector de frecuencia

#graficar

plt.subplot(2,2,1)
plt.plot(t, x)
plt.axis([0, x.size/float(fs), min(x), max(x)])
plt.ylabel('amplitud')
plt.xlabel('tiempo')
plt.title('audio: x')
         
# graficar espectrograma en el rango definido
plt.subplot(2,2,2)
numFrames = int(mX[:,0].size)
frmTime = H*np.arange(numFrames)/float(fs)
bins=(Freq>rango[0]) & (Freq<rango[1])

Sxx=np.transpose(mX[:,bins])

plt.pcolormesh(frmTime,Freq[bins],Sxx)
plt.ylabel('Frequencia [Hz]')
plt.xlabel('Time [sec]')
plt.autoscale(tight=True)

#graficar el promedio del espectro de todo el archivo de audio
mX=np.mean(mX,axis=0)
plt.subplot(2,2,3)
plt.plot(Freq[bins],mX[bins])

plt.xlabel('Frequencia [Hz]')
plt.ylabel('Magnitud en dB')

##########################################
#BLOQUE 2
'''
#disenar filtro que permita pasar unicamente las componentes de frecuencia con informacion relevante
#modificar los parametros que sean necesarios
b1 = signal.firwin(64, 0.1, window='hamming', pass_zero=True)
#obtener la respuesta en frecuencia
omega, mag = signal.freqz(b1)

#filtrar la onda con el filtro numero 1
x1=signal.lfilter(b1, [1.0],x)
#usar fourier para ilustrar el resultado del filtro
mX, pX = wp.stftAnal(x1, w, N, H)
#
plt.figure(2)
#graficar audio filtrado
plt.subplot(2,2,1)
plt.plot(t, x1)
plt.axis([0, x1.size/float(fs), min(x1), max(x1)])
plt.ylabel('amplitud')
plt.title('audio filtrado: x')

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
#BLOQUE 3
'''
#remuestrear la senal filtrada y guardarla en un nuevo archivo de audio

#definir la nueva frecuencia de muestreo
nfs=2000

##Remuestrear
factor=fs/nfs
new_samples=int(x1.size/factor)
nx1 = signal.resample(x1, new_samples)
#graficar la nueva senal de audio
t=np.arange(nx1.size)/float(nfs) #vector de tiempo
plt.subplot(2,2,4)
plt.plot(t,nx1)
plt.ylabel('amplitud')
plt.xlabel('tiempo')

wavwrite(nx1, nfs, 'output/nuevo_audio1.wav')
'''
plt.show()



