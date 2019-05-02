#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>

int** Matrix_Alloc(int** matrix, int rows, int columns)
{
    int i;
    matrix=malloc(sizeof(int)*rows*columns);
    if(matrix!=NULL)
    {
        /*Asignar espacio para cada fila*/
        for(i=0; i<rows;i++)
        {
            matrix[i] = malloc(sizeof(int)*columns);
            if(matrix[i]==NULL)
            {
                return NULL;
            }
        }
    }
    return matrix;
}
/*liberar memoria*/
void Matrix_Free(int** matrix, int rows)
{
    int i;
    for(i = 0; i < rows; i++)
    {
        free(matrix[i]);
    }
    free(matrix);
}
/*imprimir matriz*/
void Matrix_Print(int** matrix, int rows, int columns)
{
    int i,j;
    for(i=0; i<rows;i++)
    {
        for(j=0; j<columns; j++)
        {
            printf("%d ",matrix[i][j]);
        }
        putchar('\n');
    }
}

/*funcion principal*/
int main(void)
{
    int **matrix = NULL;
    int i, j, fil, col;

    printf("Ingresar el numero de filas:\n");
    scanf("%d",&fil);
    printf("Ingresar el numero de columnas:\n");
    scanf("%d",&col);
    

    /*Asignar memoria para la matriz*/
    matrix = Matrix_Alloc(matrix, fil, col);

    /*asignar valores a la matriz*/
    int valor;
    for (i = 0; i < fil; i++)
    {
        for (j = 0; j < col; j++)
        {
         printf("ingresar valor X(%d,%d): ",i,j);
         scanf("%d",&valor);
        
         matrix[i][j] = valor;
        }
    }

    /*imprimir resultados*/
    Matrix_Print(matrix,fil,col);

    /*Liberar memoria*/
    Matrix_Free(matrix,fil);
    puts("Memoria liberada");

    return 0;
}
