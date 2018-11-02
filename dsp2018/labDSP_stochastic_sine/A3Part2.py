import numpy as np
import time, os, sys
import wav_process as wp
import matplotlib.pyplot as plt
#from scipy.signal import hamming
from wav_rw import wavread, wavwrite
from scipy.signal import get_window
eps = np.finfo(float).eps

"""
A3-Part-2: medir la envolvente de energia y diferencia entre energias de ventanas sucesivas

Test case 1: piano.wav  'blackman' window, M = 513, N = 2048 H = 128

Test case 2: sax-phrase-short.wav 'hamming' window, M = 512, N = 1024  H = 64

Test case 3: rain.wav 'hann' window, M = 1024, N = 2048 H = 128
"""

def computeEO(inputFile, window, M, N, H):
    """
    Input:
            inputFile (string): archivo wav 
            window (string): ventana de analisis (rectangular, triangular, hanning, hamming, blackman, blackmanharris)
            M (integer): Longitud de la ventana
            N (integer): numero de puntos de la fft (potencia de 2 y N > M)
            H (integer): incremento entre ventanas
    Output:
            la energia calculada para cada ventana, y la diferencia de energia entre ventanas sucesivas
            E = energia
            O = diferencia de energia entre ventanas
            
            
    """
    (fs, x) = wavread(inputFile)
    #dividir la senal en ventanas
    #xf es la version de la senal dividida en ventanas, mX es la magnitud en decibeles de la transformada de fourier de las ventanas
    (xf,mX)=wp.enframe(x, window, M, H, N)
    E=0
    O=0
    ## su codigo va aqui   
    
    
    ##
    return E,O
###################################################################################
    
inputFile='sound/piano.wav'
#window puede ser rectangular, hanning, hamming, blackman, blackmanharris...........
window = 'rectangular'
M=  1024
N = 1024
H = 500

E,O = computeEO(inputFile, window, M, N, H)


