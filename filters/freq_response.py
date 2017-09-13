#example taken from scipy documentation


from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


#disenar el filtro usando una ventana kaiser
b = signal.firwin(80, 0.5, window=('kaiser', 8))
w, h = signal.freqz(b)

fig = plt.figure(1)

plt.subplot(211)
plt.title('Respuesta en frecuencia de filtro digital')
#ax1 = fig.add_subplot(111)
plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.ylabel('Amplitud [dB]', color='b')
plt.grid()

plt.subplot(212)
#ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
plt.plot(w, angles, 'g')
plt.ylabel('Angulo (radianes)', color='g')
plt.grid()
plt.xlabel('Frequencia [rad/muestra]')
plt.axis('tight')


### generar secuencias sinusoidales usando dos frecuen
fs=2000
tf=1 #tiempo final
t,T=np.linspace(1./fs,tf,fs*tf,retstep=True)
#
f1=200.
w1=2*np.pi*f1
x1=np.cos(w1*t)
#
f2=600.
w2=2*np.pi*f2
x2=np.cos(w2*t)

x1f=signal.lfilter(b, [1.0],x1)
x2f=signal.lfilter(b, [1.0],x2)

fig = plt.figure(2)
plt.subplot(211)
plt.title('Caso 1: Frecuencia de muestreo 2kHz, f1=200, f2=600')
plt.plot(t,x1,t,x1f)
plt.ylabel('Amplitud')

plt.subplot(212)
plt.plot(t,x2,t,x2f)
plt.ylabel('Amplitud')
plt.xlabel('tiempo - s')
##########
fs=100
t,T=np.linspace(1./fs,tf,fs*tf,retstep=True)
#
f1=10.
w1=2*np.pi*f1
x1=np.cos(w1*t)
#
f2=30.
w2=2*np.pi*f2
x2=np.cos(w2*t)

x1f=signal.lfilter(b, [1.0],x1)
x2f=signal.lfilter(b, [1.0],x2)

fig = plt.figure(3)
plt.subplot(211)
plt.title('Caso 2: Frecuencia de muestreo 100,  f1=10, f2=30')
plt.plot(t,x1,t,x1f)
plt.ylabel('Amplitud')

plt.subplot(212)
plt.plot(t,x2,t,x2f)
plt.ylabel('Amplitud')
plt.xlabel('tiempo - s')




plt.show()





