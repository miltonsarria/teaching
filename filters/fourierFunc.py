#Milton Orlando Sarria Paja
#USC 2017
#analisis de fourier para datos de ondas entregados por argumentos
import numpy as np
from scipy.fftpack import fft
import math
##################################################################################
##################################################################################
def fourierAn(y):
        #aplicar transformada de fourier a los datos
        Y = fft(y)
        # Calcular magnitud y angulo, normalizar por el num de muestras
        absY = abs(Y)/(y.size)                               
        #fase
        pY = np.unwrap(np.angle(Y))
        ###########################################
        #reorganizar el espectro para graficar
        #numero de muestras hasta la mitad del espectro
        hN=int(math.floor((Y.size+1)/2))
        absY=np.hstack((absY[hN:],absY[:hN]))
        pY=np.hstack((pY[hN:],pY[:hN]))

        #calcular la magnitud en dB
        absY[absY < np.finfo(float).eps] = np.finfo(float).eps    # Si hay ceros, reemplazar por un valor muy pequeno, antes de aplicar el log
        Ydb = 20 * np.log10(absY) 
        #retornar la magnitud, la magnitud en decibeles y la fase
        return absY,Ydb,pY

