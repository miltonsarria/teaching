import numpy as np

"""
A2-Part-3: Operaciones basicas sobre un arreglo

Escribir una funcion que reciba un arreglo tipo numpy y retorne el valor maximo y el valor minimo del arreglo

La entrada es un arreglo x tipo numpy, y la salida dos numeros de punto flotante en una tuppla

si usted ingresa por ejemplo: x=np.array([0,-1.9,10,0.99,2.5,-5.5,10.1])
la salida debe ser (min, max): (-5.5,10.1)

"""
def MinMaxVal(x):

    """
    Input:
        x: arreglo tipo numpy con muestras de una señal
    Output:
        una tupla que contiene los valores minimo y maximo de las muestras en x: (min_val, max_val)
    """
    ## Your code here
    values=()
    
    return values
    
x=np.array([0,-1.9,10,0.99,2.5,-5.5,10.1])
(min_val,max_val)=MinMaxVal(x)
print(min_val,max_val)
