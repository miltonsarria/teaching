import numpy as np
from scipy import signal
from scipy.signal import filter_design as fd
from matplotlib import pyplot as plt

Wp = 0.270   # Banda pasante
Ws = 0.333   # Banda de rechazo
Rp = 0.1     # Minima perdida en banda pasante
As = 120     # Minima perdida en banda de rechazo

(b,a) = fd.iirdesign(Wp, Ws, Rp, As, ftype='cheby2')

w, h = signal.freqz(b,a)


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
plt.show()

'''
ftype='butter'
ftype='cheby2'
ftype='ellip'
ftype='bessel'
b,a = signal.iirdesign(wp = [0.05, 0.3], ws= [0.02, 0.35], gstop= 60, gpass=1, ftype='ellip')
''' 


