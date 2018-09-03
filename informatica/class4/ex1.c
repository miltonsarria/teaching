/**
 * programa en C imprimir triangulo rectangulo
 */
#include <stdio.h>

int main()
{
    int i, j, rows;
    /* filas definidas por el usuario */
    printf("ingrese numero de filas: ");
    scanf("%d", &rows);
    /* iterar en las filas */
    for(i=1; i<=rows; i++)
    {
        /* imprimir espacios en orden descendente */
        for(j=i; j<rows; j++)
        {
            printf(" ");
        }
        /* imprimir asterisco en forma ascendente */
        for(j=1; j<=i; j++)
        {
            printf("*");
        }
        /* moverse a la siguiente linea */
        printf("\n");
    }
   return 0;
}
