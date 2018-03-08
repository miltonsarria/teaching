#Milton Orlando Sarria
#analisis espectral de sinusoides

import matplotlib.pyplot as plt
import numpy as np
from fourierFunc import fourierAn
import wav_rw as wp
from scipy.signal import get_window

filename1='sound/flute-A4.wav'
filename2='sound/violin-B3.wav'

#leer los archivos de audio
fs,x1=wp.wavread(filename1)
fs,x2=wp.wavread(filename2)

t=(np.arange(1,5*fs))/float(fs)
#crear dos ventanas
w1    = get_window('hamming', x1.size);  w1    = w1 / sum(w1) 
w2    = get_window('hamming', x2.size);  w2    = w2 / sum(w2) 
#calcular el espectro de las ondas 
absY1,mY1,pY1=fourierAn(x1*w1)
absY2,mY2,pY2=fourierAn(x2*w2)
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


indx1=np.array([48355,49307,50265, 51222,52167])
indx2=np.array([48073,48606,49138, 50203])

f1=f[indx1]#np.array([443.7, 886.63, 1329.94])
f2=f[indx2]#np.array([312.6, 560.54, 808.01] )
A2=absY1[indx1]#np.array([0.02638, 0.13159, 0.03147])
A1=absY2[indx2]#np.array([0.0270,0.02018,0.00362])
p1=pY1[indx1]#np.array([-14.42432594, -70.36247253, -68.44787598])
p2=pY2[indx2]#np.array([-131.58657837, -428.93927002, -783.9352417 ])


y1=np.zeros(t.size)
y2=np.zeros(t.size)
for i in range(3):
    
    fii=A1[i]*np.cos(2*np.pi*f1[i]*t+p1[i])
    y1=y1+fii  
       
    fii=A2[i]*np.cos(2*np.pi*f2[i]*t+p2[i])
    y2=y2+fii     


plt.figure(2)

plt.subplot(211)
plt.plot(y1)
plt.title('onda 1')

plt.subplot(212)
plt.plot(y2)
plt.title('onda 2')



plt.show()

