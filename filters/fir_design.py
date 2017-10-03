#Milton Orlando Sarria
#diseno de filtros FIR

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


#disenar el filtro usando una ventana kaiser y beta 8
#b = signal.firwin(80, 0.5, window=('kaiser', 8))

#diseñar un filtro pasa bajas usando una ventana hamming
b = signal.firwin(81, 0.5, window='hamming', pass_zero=True)
#pasa bajas pass_zero=True
#pasa altas pass_zero=False

#obtener la respuesta en frecuencia
w, h = signal.freqz(b)

#opciones de ventanas:
#boxcar, triang, blackman, hamming, hann, bartlett, flattop, parzen, bohman, blackmanharris, nuttall, barthann, kaiser (necesita un parametro adicional beta), gaussian (necesita la desviacion estandar std), general_gaussian (needs necesita potencia y ancho: power, width), slepian (necesita ancho), chebwin (necesita atenuacion en banda de rechazo)

#graficar la respuesta del filtro, magnitud |H(w)| y fase  phi
fig = plt.figure(1)
plt.subplot(211)
plt.title('Respuesta en frecuencia de filtro digital')
plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.ylabel('Amplitud [dB]', color='b')
plt.grid()

plt.subplot(212)
angles = np.unwrap(np.angle(h))
plt.plot(w, angles, 'g')
plt.ylabel('Angulo (radianes)', color='g')
plt.grid()
plt.xlabel('Frequencia [rad/muestra]')
plt.axis('tight')

#crear una nueva figura para graficar la respuesta a impulso del filtro, la secuencia h[n] representada por los coeficientes b
fig = plt.figure(2)
plt.stem(b, '-.b')
plt.xlabel('valor de n')
plt.ylabel('valor de h[n]')
plt.title('Respuesta a impulso del filtro h[n]')
plt.show()


plt.show()





