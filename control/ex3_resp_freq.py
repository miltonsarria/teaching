#Milton Orlando sarria
#Analisis de respuesta en lazo cerrado ante entrada escalo e impulso
#sistema de dos tanques acoplados

import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

# Programa que obtiene respuestas de lazo abierto y cerrado para
# la funcion de transferencia obtenida

#definir la funcion de transferencia
num = [200, 0];
den = [1, 102, 200];

G=ctrl.tf(num, den)
#calcular la respuesta en frecuencia

mag, phase, omega = ctrl.bode(G)

#graficar las respuestas por separado, primero impulso luego escalon
plt.subplot(211)
l1,=plt.plot(omega, mag); 
plt.grid()
plt.title('Respuesta en frecuencia');
plt.ylabel('Magnitud');

##
plt.subplot(212);
l2,=plt.plot(omega,phase);
plt.grid()
plt.ylabel('Fase');
plt.xlabel('Frecuencia (rad/seg)');

plt.show()

