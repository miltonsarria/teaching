import numpy as np
import time, os, sys
import wav_process as wp
import matplotlib.pyplot as plt
#from scipy.signal import hamming
from wav_rw import wavread, wavwrite
from scipy.signal import get_window
eps = np.finfo(float).eps

"""
A3-Part-1: medir la relacion senal a ruido usando el modelo STFT

Test case 1: piano.wav  'blackman' window, M = 513, N = 2048 H = 128

Test case 2: sax-phrase-short.wav 'hamming' window, M = 512, N = 1024  H = 64

Test case 3: rain.wav 'hann' window, M = 1024, N = 2048 H = 128
"""

def computeSNR(inputFile, window, M, N, H):
    """
    Input:
            inputFile (string): archivo wav 
            window (string): ventana de analisis (rectangular, triangular, hanning, hamming, blackman, blackmanharris)
            M (integer): Longitud de la ventana
            N (integer): numero de puntos de la fft (potencia de 2 y N > M)
            H (integer): incremento entre ventanas
    Output:
            la relacion senal a ruido despues de reconstruir una senal.
            
            
    """
    (fs, x) = wavread(inputFile)
    #generar ventana
    w = get_window(window, M)
    #obtener la transformada de fourier del archivo de audio (magnitud y la fase)
    mX, pX = wp.stftAnal(x, w, N, H)
    #usando la magnitud y fase reconstuir el archivo de audio
    y = wp.stftSynth(mX, pX, w.size, H)
    SNR = 0
    ## su codigo va aqui   
    
    
    ##
    return SNR
###################################################################################
    
inputFile='sound/piano.wav'
#window puede ser rectangular, hanning, hamming, blackman, blackmanharris...........
window = 'rectangular'
M=  1024
N = 1024
H = 500



SNR = computeSNR(inputFile, window, M, N, H)


