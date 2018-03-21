#Milton Orlando Sarria
#analisis espectral de sinusoides

import matplotlib.pyplot as plt
import numpy as np
from fourierFunc import fourierAn
import wav_rw as wp


filename1='audio/speaker2/audio1.wav'
#leer los archivos de audio
fs,x1=wp.wavread(filename1)

t=(np.arange(1,x1.size+1))/float(fs)

#calcular el espectro de la onda
absY1,mY1,pY1=fourierAn(x1)

#vector de frecuencias, desde -fs/2 a fs/2  (-pi<w<pi)
f=np.linspace(-fs/2,fs/2,absY1.size)

#visualizar las dos ondas, limpia y contaminada y sus espectros
plt.subplot(211)
plt.plot(t,x1)
plt.title('onda sin ruido')

plt.subplot(212)
plt.plot(f,mY1)
plt.title('Espectro onda sin ruido')

plt.show()


