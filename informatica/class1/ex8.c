//Milton Orlando Sarria 
//USC
/*
Introduccion al ciclo for
*/

#include <stdio.h>
void main()
{
   int j,n;
   printf("Ingrese el numero (Tabla a calcular) : ");
   scanf("%d",&n);
   printf("\n");
   for(j=1;j<=10;j++)
   {
     printf("%d X %d = %d \n",n,j,n*j);
   }
} 
