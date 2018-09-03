#include <stdlib.h>
#include <stdio.h>

int main ()
{
   

//Definamos estas variables:
int x[100],b,*pa,*pb;
//...
x[50]=10; //Le asignamos el valor de 10, al array #50
pa=&x[50]; //Le asignamos al puntero pa, la direccion de memoria que tiene x[50]
//Ahora mostramos algunas posibles operaciones:
b = *pa+1; //Esto es como decir el valor que tiene el array de x[50] sumarle 1.
           //Esto es igual a: b=x[50]+1; => Su valor seria igual a 11.
b = *(pa+1); //Esto primero pasa a la siguiente direccion de memoria y luego lo referencia
             //El resultado es: b = x[51];
pb = &x[10]; //al puntero pb se le asigna la direccion de x[10]
*pb = 0; //Al valor que tiene el puntero se le asigna 0
             //Esto es igual que decir: x[10] = 0
*pb += 2; //El valor del puntero se incrementa en dos unidades, es decir x[10] += 2
(*pb)--; //El valor del puntero se decrementa en una unidad.
x[0] = *pb--; //A x[0] se le pasa el valor de x[10] y el puntero pb, pasa a apuntar a x[9]
              //recuerda, que -- es post-decremento, primero asignará y luego restará.
//EJERCICIO
//en cada linea completar e incluir los comandos necesarios para imprimir o visualizar el resultado

}
