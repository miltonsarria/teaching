#Milton Orlando sarria
#Analisis de respuesta en lazo cerrado ante entrada escalo e impulso
#sistema de dos tanques acoplados

#import control as ctrl
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# Programa que obtiene respuestas de lazo abierto y cerrado para
# la funcion de transferencia obtenida

#definir la funcion de transferencia
num = [200, 0];
den = [1, 102, 200];

#G=ctrl.tf(num, den)
#forma alternativa usando scipy
G=signal.lti(num, den)
#calcular la respuesta en frecuencia
#mag, phase, omega = ctrl.bode(G)
omega, mag, phase = signal.bode(G)

#graficar la respuesta en frecuencia
plt.subplot(211)
l1,=plt.semilogx(omega, mag); 
plt.grid()
plt.title('Respuesta en frecuencia');
plt.ylabel('Magnitud');

##
plt.subplot(212);
l2,=plt.semilogx(omega,phase);
plt.grid()
plt.ylabel('Fase');
plt.xlabel('Frecuencia (rad/seg)');

plt.show()

