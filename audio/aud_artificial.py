#Milton Orlando Sarria
#analisis espectral de sinusoides
#generar audio de forma artificial para simular un instrumento musical
from pandas import Series
import matplotlib.pyplot as plt
import numpy as np
from fourierFunc import fourierAn
import wav_rw as wp
from scipy.signal import get_window
import sounddevice as sd

#########################################################################################
def findIndx(absY):
    indx=[]
    s=Series(absY)
    rol = s.rolling(window=10)
    r_mean=rol.mean()
    absy=r_mean.as_matrix()
    absy=np.hstack((np.zeros(5),absy[10:]))
    tresh=absy/np.max(absy)>0.05
    seg=np.hstack((tresh,np.zeros(1)))-np.hstack((np.zeros(1),tresh))
    
    ini=np.arange(seg.size)[seg>0]
    fin=np.arange(seg.size)[seg<0]
    
    for a,b in zip(ini,fin):
        indx.append(int(np.mean([a,b])))

    indx=np.array(indx)
    indx=indx[int(indx.size/2):]
    
    return indx
#########################################################################################


#sound/oboe-A4
#sound/organ-C3
#sound/flute-A4

filename1='sound/organ-C3'
F0=2*130.81 #440
longitud = 3
#leer los archivos de audio y generar vector de tiempo de 2 segundos
fs,x1=wp.wavread(filename1+'.wav')
t=(np.arange(1,longitud*fs))/float(fs)


#crear dos ventanas
N=int(1.5*fs)
N1=int(x1.size/2)

w1    = get_window('hamming', N); 

#calcular el espectro de las ondas 
s1=x1[int(N1-N/2):int(N1+N/2)]
absY1,mY1,pY1=fourierAn(s1*w1)
#vector de frecuencias, desde -fs/2 a fs/2  (-pi<w<pi)
f=np.linspace(-fs/2,fs/2,absY1.size)
#visualizar las dos ondas
plt.subplot(311)
plt.plot(x1)
plt.title('onda original')

plt.subplot(312)
plt.plot(f,absY1)
plt.title('Espectro onda 1')

plt.subplot(313)
plt.plot(pY1)
plt.title('fase onda 1')


indx1=findIndx(absY1)

f1=f[indx1]#np.array([443.7, 886.63, 1329.94])

A1=absY1[indx1]#np.array([0.02638, 0.13159, 0.03147])

p1=pY1[indx1]#np.array([-14.42432594, -70.36247253, -68.44787598])

y_out=np.zeros(t.size)

phase = np.random.rand(indx1.size)
phase = (phase - phase.mean())*2*np.pi

for i in range(indx1.size):
    omega_n = 2*np.pi*F0*(i+1)
    #fii=A1[i]*np.cos(2*np.pi*f1numpy.random.rand[i]*t+p1[i])
    fii=A1[i]*np.cos(omega_n*t+phase[i])
    y_out=y_out+fii  
       

#y1=0.5*y1/np.max(np.abs(y1))
G=x1.max()/y_out.max()
wp.wavwrite(G*y_out, fs,filename1+'_sin.wav')
#sd.play(y1, fs)
#sd.wait()

plt.figure(2)
plt.subplot(211)
plt.plot(y_out)
plt.title('onda 1')

plt.show()

