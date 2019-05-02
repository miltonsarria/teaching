import numpy as np

#A1-Part-3: Implementar la transformada discreta de Fourier (DFT)
# es necesario usar la funcion genComplexSine(k, N) que genero en la parte 2
    
def compDFT(x):
    """
    Input:
        x (numpy array) = secuencia de entrada delongitud N
    Output:
        la funcion debe retornar una secuencia de longitud N
        X (numpy array) = La DFT de N puntos de la seceuncia de entrada x
    """
    ## su codigo va aqui
    X=[]
    return X
    
##########################################################    
x = np.array([1, 2, 3, 4]) #secuencia en el dominio del tiempo
X=compDFT(x)               #aplicar transformada de fourier
print(X)                   #imprimir los resultados

