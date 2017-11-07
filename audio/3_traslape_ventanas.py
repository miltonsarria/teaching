import numpy as np

import matplotlib.pyplot as plt
from scipy.signal import get_window

#analizar diferentes longitudes de ventana y como afecta el traslape para la reconstruccion

plt.figure(1, figsize=(9.5, 6))

N  = 1000 # longitud total del segmento a analizar
M  = 201  # longitud de la ventana
H1 = 100  # traslape entre venanas caso 1
H2 = 50   # traslape entre venanas caso 2

window = 'hanning'
#window puede ser rectangular, hanning, hamming, blackman, blackmanharris
#generar ventana y normalizarla
w = get_window(window, M)
w1 = w/sum(w)

y = np.zeros(N)

pin = 0
pend = N - M
#graficar ventanas de forma individual y la resultante de la suma caso 1
plt.subplot(211)
while pin<pend:
	y[pin:pin+M] += w1*H1
	plt.plot(np.arange(pin, pin+M), w, 'b', lw=1.5)
	pin += H1
plt.plot(np.arange(0, N), y, 'r', lw=1.5)
plt.axis([0, N-H1, 0, max(y)+.01])
plt.title(window+' , M=201, H='+str(H1))

y = np.zeros(N)
pin = 0
pend = N - M
plt.subplot(212)
#graficar ventanas de forma individual y la resultante de la suma caso 2
while pin<pend: 
	y [pin:pin+M] += w1*H2
	plt.plot(np.arange(pin, pin+M), w, 'b', lw=1.5)
	pin += H2
plt.plot(np.arange(0, N), y, 'r', lw=1.5)
plt.axis([0, N-H2, 0, max(y)+.01])
plt.title(window+' , M=201, H='+str(H2))

plt.tight_layout()
plt.show()

