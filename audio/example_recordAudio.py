#Milton Orlando Sarria Paja
#USC
#Procesamiento digital de senales

import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import sys
from wav_rw import wavwrite, enframe
from pandas import Series
#################################################################
#################################################
#detector de actividad vocal usando log energia y un umbral trh
naverage=10
def vad(logE,trh):
    s=Series(logE)
    logE = (s.rolling(window=naverage)).mean().values
    logE[0:naverage-1]=logE[naverage:].min()
    logE=np.roll(logE, -naverage/2, axis=0)    
    wvad=logE>trh
    return wvad
#################################################################
sr      = 16000     #khz
chann   = 1         #numero de canales
duration = 2        # seconds grabar como maximo 2 segundos
#iniciar el proceso
while True:
    print('Seleccionar una opcion:\n1) Iniciar proceso\n2) Salir')
   
    opcion=input()
    if opcion==1:   
        myrecording = sd.rec(int(duration * sr), samplerate=sr, channels=chann)
        sd.wait()
        #######
        #la variable myrecording contiene el audio grabado, se puede iniciar el proceso
        #en este punto, a continuacion se presenta un EJEMPLO        
        #primero se hace un analisis de energia en tiempo corto, se calculan ventanas
        #de 512 puntos y se calcula su energia en decibeles
        frames=enframe(x = myrecording)
        #antes de guardar el audio se debe detectar cuales son los segmentos con silencio
        logE   = 20*np.log10((np.abs(frames)**2).sum(axis=1))
        ### se puede analizar la energia y si supera un umbral de -90 db entonces se unen
        #esos frames y se guarda lo resultante, cortando los frames con muy poca energia
        frames_audio=vad(logE,-90)
        x=np.hstack((frames[frames_audio,:]))
        #su codigo puede continuar dependiendo de lo que se pida es posible agregregar mas
        #procesamiento, filtar..... o decidir si guardar o no si son pocos frames con sonido
        ##
        
        
        #se guarda el audio resultante
        wavwrite(x,16000,'prueba.wav')
        
    else: 
        break
   







