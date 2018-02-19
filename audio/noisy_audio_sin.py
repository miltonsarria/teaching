import matplotlib.pyplot as plt
import numpy as np
import wav_rw as wp

#####################################
filename='audio/speaker2/audio1.wav'
#cargar archivo de audio
fs,x=wp.wavread(filename)
#vector de tiempo para generar ruido, de la misma longitud del audio
t=(np.arange(1,x.size+1))/float(fs)

F=150            #frecuencia fundamental
w=2*np.pi*F     #frecuencia angular

#generar onda de ruido sinusoidal
ruido=0.1*np.cos(w*t)
#onda con ruido
y=x+ruido

plt.subplot(211)
plt.plot(t,x)
plt.subplot(212)
plt.plot(t,y)
plt.show()

filename_out='audio/speaker2/audio1_noise.wav'

wp.wavwrite(y, fs, filename_out)

