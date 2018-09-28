#Milton Orlando Sarria
#filtrado elemental de ruido sinusoidal
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


#disenar el filtro usando una ventana hamming
b = signal.firwin(9, 0.8, window='hamming', pass_zero=True)

#definir la frecuencia de muestreo y generar un vector de tiempo hasta 5 segundos
fs=1e3
longitud = 5
t=np.linspace(1./fs,longitud,fs*longitud);


F=10            #frecuencia fundamental 10 hz
w=2*np.pi*F     #frecuencia angular
Vm=4            #valor de amplitud de la onda

#generar onda sinusoidal pura
x=Vm*np.cos(w*t)
#generar onda de ruido sinusoidal, alta frecuencia y baja amplitud
#usar una frecuencia 30 veces mayor a la inicial
ruido=2*np.cos(30*w*t)
#onda con ruido: sumar las dos sinusoidales
x_n=x+ruido

#filtrar la onda con ruido usando el filtro FIR
yf=signal.lfilter(b, [1.0],x_n)

#visualizar las tres ondas, limpia, contaminada y filtrada
plt.subplot(311)
plt.plot(t,x)
plt.title('onda sin ruido')

plt.subplot(312)
plt.plot(t,x_n)
plt.title('onda con ruido')

plt.subplot(313)
plt.plot(t,yf)
plt.title('onda filtrada')


plt.xlabel('tiempo')

plt.show()





