# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:55:54 2018

@author: Andres
"""

import audioop
import wave
import sys
import time

frec_e2 = 82.41      # Cuerda E menor Frecuecia en Hz
frec_a2 = 110.00     # Cuerda A Frecuecia en Hz
frec_d3 = 146.83     # Cuerda D Frecuecia en Hz
frec_g3 = 196.00     # Cuerda G Frecuecia en Hz
frec_b3 = 246.94     # Cuerda B Frecuecia en Hz
frec_e4 = 329.63     # Cuerda E mayor Frecuecia en Hz

frec_cue =   1       # Frecuecia obtenida

'''
El codigo aun no esta completo la idea es juntar este codigo con el espectro en
tiempo real para que la frecuencia de la cuerda (frec_cue) obtenga los valores en 
frecuencia del sonido capturado
'''

while (frec_cue < frec_e2 - 5) or (frec_cue > frec_e2 + 5):
    if frec_cue < frec_e2:                                     # Mira si es muy alta
        frec_dif = frec_e2 - frec_cue                          # Calcula la diferencia
        print("Apretar cuerda:\t" + str(frec_cue))             # Salida
    elif frec_cue > frec_e2:                                   # Mira si es muy baja
        frec_dif = frec_cue - frec_e2                          # Calcular la diferencia
        print("Aflojar cuerda:\t" + str(frec_cue))             # Salida
    time.sleep(0.5)                                            # Tiempo de espera de lectura
    print("Cuerda E2 ok!")                                     # Salida
    frec_cue # Frecuecia obtenida

while (frec_cue < frec_a2 - 5) or (frec_cue > frec_a2 + 5):
    if frec_cue < frec_a2:                                             
        frec_dif = frec_a2 - frec_cue                               
        print("Apretar cuerda:\t" + str(frec_cue))                            
    elif frec_cue > frec_a2:                                           
        frec_dif = frec_cue - frec_a2                                 
        print("Aflojar cuerda:\t" + str(frec_cue))                           
    time.sleep(0.5)                                                 
    print("Cuerda A2 ok!")                                                   
    frec_cue  # Frecuecia obtenida

while (frec_cue < frec_d3 - 5) or (frec_cue > frec_d3 + 5):
    if frec_cue < frec_d3:                                             
        frec_dif = frec_d3 - frec_cue                                 
        print("Apretar cuerda:\t" + str(frec_cue))                           
    elif frec_cue > frec_d3:                                          
        frec_dif = frec_cue - frec_d3                                 
        print("Aflojar cuerda:\t" + str(frec_cue))                          
    time.sleep(0.5)                                                
    print("Cuerda D3 ok!")                                                  
    frec_cue  # Frecuecia obtenida

while (frec_cue < frec_g3 - 5) or (frec_cue > frec_g3 + 5):
    if frec_cue < frec_g3:                                             
        frec_dif = frec_g3 - frec_cue                                 
        print("Apretar cuerda:\t" + str(frec_cue))                            
    elif frec_cue > frec_g3:                                           
        frec_dif = frec_cue - frec_g3                                 
        print("Aflojar cuerda:\t" + str(frec_cue))                          
    time.sleep(0.5)                                                 
    print("Cuerda G3 ok!")                                                   
    frec_cue # Frecuecia obtenida

while (frec_cue < frec_b3 - 5) or (frec_cue > frec_b3 + 5):
    if frec_cue < frec_b3:                                            
        frec_dif = frec_b3 - frec_cue                                 
        print("Apretar cuerda:\t" + str(frec_cue))                         
    elif frec_cue > frec_b3:                                        
        frec_dif = frec_cue - frec_b3                                 
        print("Aflojar cuerda:\t" + str(frec_cue))                          
    time.sleep(0.5)                                                
    print("Cuerda B3 ok!")                                                   
    frec_cue # Frecuecia obtenida

while (frec_cue < frec_e4 - 5) or (frec_cue > frec_e4 + 5):
    if frec_cue < frec_e4:                                             
        frec_dif = frec_e4 - frec_cue                                 
        print("Apretar cuerda:\t" + str(frec_cue))                           
    elif frec_cue > frec_e4:                                           
        frec_dif = frec_cue - frec_e4                                 
        print("Aflojar cuerda:\t" + str(frec_cue))                           
    time.sleep(0.5)                                                
    print("Cuerda E4 ok!")                                                   
    frec_cue # Frecuecia obtenida


sys.exit()

