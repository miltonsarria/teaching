import matplotlib.pyplot as plt
import numpy as np
import wav_rw as wp

#####################################
filename1='/home/sarria/data/vuvuzela44k_16b.wav'
filename2='/home/sarria/data/AVPEPUDEAC0025_micasa.wav'



#cargar archivo de audio
fs,xn=wp.wavread(filename1)
fs,xc=wp.wavread(filename2)
#vector de tiempo para generar ruido, de la misma longitud del audio
xn=xn/(np.abs(xn)).max()
xc=xc/(np.abs(xc)).max()

xc=np.hstack((np.zeros(20000),xc))


plt.subplot(211)
plt.plot(xn)
plt.subplot(212)
plt.plot(xc)
plt.show()

n=xc.size
y=xn[1000:1000+n]

x1=xc+0.3*y; x1=x1/(np.abs(x1)).max()
x2=xc+0.6*y; x2=x2/(np.abs(x2)).max()
x3=xc+0.9*y; x3=x3/(np.abs(x3)).max()
x4=xc+y;     x4=x4/(np.abs(x4)).max()

filename_out='/home/sarria/data/audio1.wav'
wp.wavwrite(0.9*x1, fs, filename_out)
filename_out='/home/sarria/data/audio2.wav'
wp.wavwrite(0.9*x2, fs, filename_out)
filename_out='/home/sarria/data/audio3.wav'
wp.wavwrite(0.9*x3, fs, filename_out)
filename_out='/home/sarria/data/audio4.wav'
wp.wavwrite(0.9*x4, fs, filename_out)
