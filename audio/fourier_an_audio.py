#Milton Orlando Sarria
#analisis espectral de sinusoides

import matplotlib.pyplot as plt
import numpy as np
from fourierFunc import fourierAn
import wav_rw as wp


filename1='sound/flute-A4.wav'
filename2='sound/violin-B3.wav'

#leer los archivos de audio
fs,x1=wp.wavread(filename1)
fs,x2=wp.wavread(filename2)

t=(np.arange(1,x1.size+1))/float(fs)

#calcular el espectro de las ondas 
absY1,mY1,pY1=fourierAn(x1)
absY2,mY2,pY2=fourierAn(x2)
#vector de frecuencias, desde -fs/2 a fs/2  (-pi<w<pi)
f=np.linspace(-fs/2,fs/2,absY1.size)

#visualizar las dos ondas
plt.subplot(321)
plt.plot(x1)
plt.title('onda sin ruido')

plt.subplot(323)
plt.plot(absY1)
plt.title('Espectro onda 1')

plt.subplot(325)
plt.plot(pY1)
plt.title('fase onda 1')


plt.subplot(322)
plt.plot(x2)
plt.title('onda 2 ')

plt.subplot(324)
plt.plot(absY2)
plt.title('Espectro 2')

plt.subplot(326)
plt.plot(pY2)
plt.title('fase onda 2')


#48355
#48073
plt.show()

