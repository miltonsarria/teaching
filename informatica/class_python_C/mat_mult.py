#Milton Orlando Sarria
#Fundamentos de informatica electronica
#USC

import numpy as np
import time 
#definir filas y columnas
m=1000
n=1000
#inicializar matrices
A=np.random.randint(0, high=10, size=(m,n))
B=np.random.randint(0, high=10, size=(m,n))
C=np.zeros((m,n))
sum=0
'''
#multiplicar matrices
start = time.time()
for i in range(m):
  for j in range(n):
    for k in range(n):
      sum=sum+A[i][k]*B[k][j]
        
    C[i][j]=sum
    sum=0
end = time.time()
#imprimir tiempo
total=end - start
print('Tiempo total: ' + str(total) + ' segundos')
'''

start = time.time()
C=np.matmul(A,B)
end = time.time()
print(end - start)

