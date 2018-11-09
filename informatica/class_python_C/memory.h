#include <stdio.h>
#include <string.h>
#include <stdlib.h>
//////////////////////////////////////////////////////////

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
