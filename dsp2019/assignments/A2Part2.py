import numpy as np
"""
A2-Part-1: Python array indexing

Escribir una funcion que para un arreglo o secuencia x, retorne otro arreglo que contiene L-1 ceros entre cada una de las posiciones 
de x, iniciando desde el primer elemento.

Los argmentos de entrada son: un arreglo tipo numpy x y un entero positivo L, tal que L < que el numero de elementos de x.
La salida deberia ser un arreglo tipo numpy.

Ejemplo: si su codigo recibe el siguiente arreglo x y valor L
x=np.array([0,1,2,3,4,5,6,7,8,9]) y L=3, entonces la salida debe ser: 
array([0,0,0,1,0,0,2,0,0,3,0,0,4,0,0,5,0,0,6,0,0,7,0,0,8,0,0,9,0,0])

"""
def insertSamples(x,L):
    """
    Inputs:
        x: Arreglo de entrada (tipo numpy)
        L: Nueva separacion entre muestras originales(entero positivo)
    Output:
        un arreglo tipo numpy que contiene L-1 ceros entre cada par de muestras de x
    """
    ## Su codigo va a aqui
    values=np.array([])

    return values
  
x=np.array([0,1,2,3,4,5,6,7,8,9]) 
M=2
y=hopSamples(x,M)
print(y)  
