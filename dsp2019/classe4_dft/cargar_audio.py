#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.io.wavfile import read
from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt


#definir un nombre y cargar el contenido del archivo
filename = 'ejemplo1.wav'
fs,x=read(filename)

#mostrar en una grafica la sinusoidal guardada
plt.plot(x)
plt.show()
