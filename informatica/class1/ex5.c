//Milton Orlando Sarria 
//USC
/*
Recibir datos de entrada con scanf
recibir entradas desde el teclado asignarlas a una variable y mostrar
un el resultado de hacer un calculo con tales datos
*/

#include <stdio.h>
int main() 
   {
	int x, y, sum;
    printf("\nIngresar el primer entero: "); 
    scanf("%d", &x);
    printf("\nIngresar el segundo entero: ");
    scanf("%d", &y);
    sum = x + y;
    printf("\nSuma de dos enteros = %d\n", sum);
    return 0;
}
