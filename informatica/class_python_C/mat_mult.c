#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include "memory.h"
#define BILLION  1000000000.0;

void Matrix_Print(int **matrix, int rows, int columns);
 
int main()
{
 //variables para medir tiempo e iniciar el generador de numeros aleatorios
 struct timespec start, end;
 time_t t;
 //memoria dinamica
 int m = 1000, n = 1000, i, j,k,sum;
 //matrices
 int **A = NULL, **B = NULL, **C=NULL;
 A = Matrix_Alloc(A, m, n);
 B = Matrix_Alloc(B, m, n);
 C = Matrix_Alloc(C, m, n);
 printf("\nMemoria asignada de forma exitosa\n"); 
/////////////////////////////////////  
/*
 srand((unsigned) time(&t));
 printf("\nInicializar posiciones de memoria\n"); 
 for(i=0;i<m;i++)
 {
     for(j=0;j<n;j++)
     {
        A[i][j] = rand()%10; 
        B[i][j] = rand()%10; 
     }
 }
 */
 sum=0;
 printf("\nMultiplicar matrices y medir tiempo\n"); 
 clock_gettime(CLOCK_REALTIME, &start);
 for (i = 0; i < m; i++) 
 {
      for (j = 0; j < n; j++)
      {
        for (k = 0; k < n; k++) 
        {
          sum = sum + A[i][k]*B[k][j];
        }
 
        C[i][j] = sum;
        sum = 0;
      }
    }
 clock_gettime(CLOCK_REALTIME, &end);
 //mostrar el tiempo medido
 double time_spent = (end.tv_sec - start.tv_sec) +  (end.tv_nsec - start.tv_nsec) / BILLION;
 printf("Tiempo total: %f segundos\n", time_spent);

	   
 Matrix_Free(A,m);
 Matrix_Free(B,m);
 
 return 0;
 }
 
  
 void Matrix_Print(int **matrix, int rows, int columns)
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




