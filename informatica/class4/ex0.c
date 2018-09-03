/**
 * Triangulo invertido
 */

#include <stdio.h>

int main()
{
    int i, j, rows;

    /* Numero de filas definidas por usuario */
    printf("numero de filas : ");
    scanf("%d", &rows);

    /* iterar en las filas */
    for(i=1; i<=rows; i++)
    {
        /* iterar en las columnas */
        for(j=i; j<=rows; j++)
        {
            printf("*");
        }
       
        /* moverse a la siguiente linea */
        printf("\n");
    }

    return 0;
}
