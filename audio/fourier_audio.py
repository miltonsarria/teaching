#Milton Orlando Sarria
#analisis espectral de sinusoides

import matplotlib.pyplot as plt
import numpy as np
from fourierFunc import fourierAn
import wav_rw as wp


filename1='/home/sarria/Documents/2017B/dsp-python/audio/audio/speaker2/audio1.wav'
filename2='/home/sarria/Documents/2017B/dsp-python/audio/audio/speaker2/audio1_noise.wav'

#leer los archivos de audio
fs,x1=wp.wavread(filename1)
fs,x2=wp.wavread(filename2)

t=(np.arange(1,x1.size+1))/float(fs)

#calcular el espectro de las ondas limpias y contaminadas
absY1,mY1,pY1=fourierAn(x1)
absY2,mY2,pY2=fourierAn(x2)
#vector de frecuencias, desde -fs/2 a fs/2  (-pi<w<pi)
f=np.linspace(-fs/2,fs/2,absY1.size)


#visualizar las dos ondas, limpia y contaminada y sus espectros
plt.subplot(221)
plt.plot(t,x1)
plt.title('onda sin ruido')

plt.subplot(222)
plt.plot(f,mY1)
plt.title('Espectro onda sin ruido')

plt.subplot(223)
plt.plot(t,x2)
plt.title('onda con ruido')

plt.subplot(224)
plt.plot(f,mY2)
plt.title('Espectro onda con ruido ')


plt.show()

####su codigo va aqui#############
#disenar un filtro

#filtrar la senal

#audio sin ruido
y=np.array([0,0,0])

#guardar el resultado
filename_out='salida.wav'
#guardar en un archivo de audio para verificar el sonido
wp.wavwrite(y, fs, filename_out)



