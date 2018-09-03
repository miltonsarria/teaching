#include <stdio.h>

void main()
{
   int i,n,a[100];
   
       printf("\n\nLeer N valores en un arreglo e imprimirlo en orden inverso:\n");
       printf("------------------------------------------------------------------------\n");
   
   printf("Numero de elementos (N) :");
   scanf("%d",&n);
   
   printf("Ingrese %d elementos en el arreglo :\n",n);
   for(i=0;i<n;i++)
      {
	  printf("element - %d : ",i);
	  scanf("%d",&a[i]);
	  }
      
   printf("\nArreglo original : \n");
   for(i=0;i<n;i++)
     {
	   printf("% 5d",a[i]);
	 }
 
   printf("\n\nLos valores en orden inverso son :\n");
   for(i=n-1;i>=0;i--)
      {
	   printf("% 5d",a[i]);
	  }
   printf("\n\n");
} 
