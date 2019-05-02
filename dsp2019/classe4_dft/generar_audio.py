#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.io.wavfile import read
from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt

fs=16e3
longitud = 2# sec
n=np.linspace(1./fs,longitud,fs*longitud);
F=400             #frecuencia fundamental 
w=2*np.pi*F       #frecuencia angular
Vm=1            #valor de amplitud de la onda
#generar onda sinusoidal pura
x=Vm*np.cos(w*n)

#definir un nombre y guardar el archivp
filename = 'ejemplo1.wav'
write(filename,fs,x)

#mostrar en una grafica la sinusoidal guardada
plt.plot(x)
plt.show()
