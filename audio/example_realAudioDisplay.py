#Milton Orlando Sarria Paja
#USC
#Procesamiento digital de senales
#graficar audio en tiempo real
#plot audio data in real time

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import sounddevice as sd
from scipy import signal
from scipy.fftpack import fft
import math
from scikits.talkbox.spectral.basic import arspec
import sys


try:
    import Queue as queue
except ImportError:
    import queue


def audio_callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print status, sys.stderr
    # Fancy indexing with mapping creates a (necessary!) copy:
    q.put(indata[::downsample, mapping])


def update_plot(frame):
    """This function is called by matplotlib for each plot update. 
    Typically, audio callbacks happen more frequently than plot updates,
    therefore the queue tends to contain multiple blocks of audio data.
    """
    global plotdata
        
    while True:
        try:
            data = q.get_nowait()
        except queue.Empty:
            break
        shift = len(data)
        plotdata = np.roll(plotdata, -shift, axis=0)
        plotdata[-shift:, :] = data
    #plotdata tiene un formato especifico que permite tener varios canales
    #solo se tomara un canal para vizualizar
    signal=plotdata[:, 0]
    line1.set_data(t,signal)
    
    return [line1]
    
#################################################################
#to save data from stream in a separate thread
q = queue.Queue()

#define important parameters
window     = 500    #miliseconds  longitud ventana a mostrar en grafica
samplerate = 16000  #khz
downsample = 1      #para bajar la frecuencia de muestreo en un factor
channels   = [1]    #numero de canales
device     = 11      #dispositivo a utilizar
interval   = 100    #update plot every 'interval' ms

#Definir e inicializar variables para graficar
length     = int(window * samplerate / (1000 * downsample))
plotdata = np.zeros((length, len(channels)))
t=np.arange(0,length)/float(samplerate)  

#Definir e inicializar la figura y los ejes donde se va a graficar
fig = plt.figure()

line1 = Line2D([], [], color='black')
ax1  = fig.add_subplot(1,1,1)

ax1.set_ylim(-1.2, 1.2)
ax1.set_xlim(0, window/1000.)

ax1.add_line(line1)

#Mapeo para separar los canales
mapping = [c - 1 for c in channels] 

#Inicializar el canal de entrada de datos usando stream y los parametros definidos
stream = sd.InputStream(
        device=device, channels=max(channels),
        samplerate=samplerate, callback=audio_callback)

#iniciar la animacion
ani1 = FuncAnimation(fig, update_plot, interval=interval,blit=True)

#iniciar el proceso
with stream:
    plt.show()



    








