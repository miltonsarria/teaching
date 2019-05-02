import numpy as np
"""
A2-Part-1: Python array indexing

Escribir una funcion que para un arreglo o secuencia x, retorne otro arreglo que contiene solamente las posiciones 
de x cada M elementos, iniciando desde el primer elemento.

Los argmentos de entrada son: un arreglo tipo numpy x y un entero positivo M, tal que M < que el numero de elementos de x.
La salida deberia ser un arreglo tipo numpy.

Ejemplo: si su codigo recibe el siguiente arreglo x y valor M
x=np.array([0,1,2,3,4,5,6,7,8,9]) y M=2, entonces la salida debe ser: array([0, 2, 4, 6, 8])

"""
def hopSamples(x,M):
    """
    Inputs:
        x: Arreglo de entrada (tipo numpy)
        M: Salto entre muestras (entero positivo)
    Output:
        un arreglo tipo numpy que contiene elementos cada M muestras de x
    """
     ## Su codigo va a aqui
    values=x[0::M]

    return values
  

x=np.array([1,5,8,9,5,3,8,5,1,0,7,8,1,1,0]) 
M=3
y=hopSamples(x,M)
print(y)
