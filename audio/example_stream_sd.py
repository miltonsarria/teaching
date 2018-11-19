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
import sys
from scipy.signal import get_window

try:
    import Queue as queue
except ImportError:
    import queue
#####################################################################
def enframe(x = None, window = 'hamming', M = 1024, H = 512):
        """
        retorna una matriz de ventanas en tiempo corto usando M como longitud
        y H para incrementos
        """
        if (x is None):                         # raise error if there is no input signal
           raise ValueError("there is no input signal")
        x = np.squeeze(x)
        w    = get_window(window, M)            # compute analysis window
        w    = w / sum(w)                       # normalize analysis window        
        if x.ndim != 1: 
                raise TypeError("enframe input must be a 1-dimensional array.")
        n_frames = 1 + np.int(np.floor((len(x) - M) / float(H)))
        xf = np.zeros((n_frames, M))
        for ii in range(n_frames):
                xf[ii] = x[ii * H : ii * H + M]*w
        return xf 
        
#####################################################################
def audio_callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print status, sys.stderr
    # Fancy indexing with mapping creates a (necessary!) copy:
    q.put(indata[::downsample, mapping])

#####################################################################
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
    
    audio = plotdata[:, 0]
    line1.set_data(t,audio)
    ####### de esta linea hasta la linea 94 se hace todo el proceso
    #que se quiere hacer sobre el segmento de audio, que para este ejemplo
    #dura 500 milisegundos. Es posible tomar mas tiempo o acumular la variable
    #que acumula solo tramos de 100 milisegundos y esa es data.
    
    #compute spectrum in dB of plotdata using FFT algorithm
    X=fft(audio)
    absX = abs(X)/(X.size)
    #fase
    #numero de muestras hasta la mitad del espectro
    hN=int(math.floor((X.size+1)/2))
    absX= absX=absX[:hN] #np.hstack((absX[hN:],absX[:hN]))
    absX[absX < np.finfo(float).eps] = np.finfo(float).eps
    Xdb = 20 * np.log10(absX)
    
    F=np.linspace(0,samplerate/2.,Xdb.size)
    line2.set_data(F,Xdb)
    
    #calcular el spectro usando un promedio de espectros en tiempo corto
    xf = enframe(audio,M=400,H=160)
    Xst = []
    for x in xf:
        Xf=fft(x)
        absX = abs(Xf)/(Xf.size)    
        hN=int(math.floor((Xf.size+1)/2))
        absX= absX=absX[:hN] #np.hstack((absX[hN:],absX[:hN]))
        absX[absX < np.finfo(float).eps] = np.finfo(float).eps
        Xst.append( 20 * np.log10(absX))
    Xst = np.mean(np.vstack(Xst),axis=0)

    Fst=np.linspace(0,samplerate/2.,Xst.size)
    line3.set_data(Fst,Xst)
    
    return [line1,line2,line3]
#####################################################################    
#####################################################################
#to save data from stream in a separate thread
q = queue.Queue()

#define important parameters
window     = 500    #miliseconds
samplerate = 16000  #khz
downsample = 1      #show every 'downsample' samples
channels   = [1]
device     = 6 
interval   = 100    #update plot every 'interval' ms

length     = int(window * samplerate / (1000 * downsample))
#define variables to initialice plots
plotdata = np.zeros((length, len(channels)))
t=np.arange(0,length)/float(samplerate)  
#np.linspace(-samplerate/2.,samplerate/2.,X.size)

#define plots and lines to show
fig = plt.figure()

line1 = Line2D([], [], color='black')
line2 = Line2D([], [], color='green',linewidth=2)
line3 = Line2D([], [], color='red',linewidth=2)
        
ax1  = fig.add_subplot(2,1,1)

ax1.set_ylim(-1.2, 1.2)
ax1.set_xlim(0, window/1000.)

ax2  = fig.add_subplot(2,1,2)
ax2.set_ylim(-200, 1)
ax2.set_xlim(0, samplerate/2)

ax1.add_line(line1)
ax2.add_line(line2)
ax2.add_line(line3)

#maping to separate channels
mapping = [c - 1 for c in channels] 

#define stream using previous defined parameters
stream = sd.InputStream(
        device=device, channels=max(channels),
        samplerate=samplerate, callback=audio_callback)

#start animation        
ani1 = FuncAnimation(fig, update_plot, interval=interval,blit=True)

#start the process
with stream:
    plt.show()



    








