import numpy as np
#A1-Part-1: Generar una sinusoidal real
def genSine(A, f, phi, fs, t):
        """
        Inputs:
                A (float) = Amplitud
                f (float) = Frecuencia de la sinusoidal en Hz
                phi (float) = fase inicial en radianes
                fs (float) = Frecuencia de muestreo en Hz
                t (float) = Duración de la sinusoidal en segundos
        Output:
                La funcion debe retornar un arreglo tipo numpy
                x (numpy array) = la sinusoidal generada (use np.cos())
        """
        if f > fs/2.0:
           print "Warning: se presenta aliasing en la secuencia"
        x=[]
        ## su código va aqui
        
        return x   
           
##########################################################
A   = 1.0;     #amplitud
f   = 10.0;    #frecuencia de la onda
phi = 1.0;     #fase
fs  = 50.0;    #frecuencia de muestreo
t   = 0.1;     #duracion
x=genSine(A, f, phi, fs, t)
print(x)
