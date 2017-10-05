#Milton Orlando sarria
#Analisis de respuesta en lazo cerrado ante entrada escalo e impulso
#sistema de dos tanques acoplados

import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

# Programa que obtiene respuestas de lazo abierto y cerrado para
# la funcion de transferencia obtenida

#definir la funcion de transferencia de lazo abierto
num = [1];
den = [72048.90, 1817.887, 1];

G=ctrl.tf(num, den)
#calcular la respuesta a impulso y a escalon
[ti, yout_i] = ctrl.impulse_response(G);
[ts, yout_s] = ctrl.step_response(G);

#calcular la funcion de transferencia de lazo cerrado
Glc=ctrl.feedback(G,1)
#calcular la respuesta a impulso y escalon
[ti_lc, yout_i_lc] = ctrl.impulse_response(Glc);
[ts_lc, yout_s_lc] = ctrl.step_response(Glc);

print('La   funcion   de   transferencia   de   lazo   abierto   para   el   sistema es : .......')
print(G)

print('Y la funcion de transferencia en lazo cerrado es : ............');
print(Glc)

#graficar las respuestas por separado, primero impulso luego escalon
plt.subplot(211)
l1,=plt.plot(ti, yout_i,label='Lazo abierto'); 
l2,=plt.plot(ti_lc, yout_i_lc,label='lazo cerrado');
plt.grid()
plt.title('Respuesta Impulso');
plt.ylabel('Amplitud');
plt.legend(handles=[l1, l2])

##
plt.subplot(212);
l1,=plt.plot(ts, yout_s,label='Lazo abierto'); 
l2,=plt.plot(ts_lc, yout_s_lc,label='lazo cerrado');
plt.grid()
plt.title('Respuesta Escalon');
plt.ylabel('Amplitud');
plt.legend(handles=[l1, l2])
plt.xlabel('Tiempo(seg)');

plt.show()

