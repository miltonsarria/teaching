close all
clear all

num1 = [12.287 23.876];
den1 = [1 5.646 16.933 23.876];
num2 = [9];
den2 = [1 3 9];
num = [10];
den = [ 1 1 10];
t = 0:0.05:5;
c1 = step(num1,den1,t);
c2 = step(num2,den2,t);
c = step(num,den,t);
plot(t,c1,'-r',t,c2,'-b',t,c,'-k')
grid
title('Respuesta a escalón unitario de sistemas compensado y no compensado')
xlabel ('t Seg')
ylabel ('Salidas c1, c2 y c')
legend('Sistema compensado (Método 1)','Sistema compensado (Método 2)','Sistema no compensado')