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
        if f < 2*fs:
           print "Warning: Habra aliasing en la secuencia"
        x=[]
        ## su código va aqui
        
        return x   
           
##########################################################
A=1.0; f = 10.0; phi = 1.0; fs = 50.0; t =0.1;
x=genSine(A, f, phi, fs, t)
print(x)
