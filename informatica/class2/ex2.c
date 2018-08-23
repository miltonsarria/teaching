#include<stdio.h>
#include<stdlib.h>
void main()
{
   int a[100],i,j,n,t;

   printf("Ingresar la longitud de la lista\n");
   scanf("%d",&n);
   printf("ingrese %d valores presionando ENTER despues de cada dato:  \n",n);
   for(i=0;i<n;i++)
        scanf("%d",&a[i]);
   printf("Lista ingresada :\n");

   for(i=0;i<n;i++)
     printf("%5d",a[i]);
 
  /* bubble sort logic */
       for(i=1;i<n;i++)
         for(j=0;j<n-i;j++)
            if(a[j]>=a[j+1])
            {
             t=a[j];
             a[j]=a[j+1];
             a[j+1]=t;
            }
   printf("\n\nLista ordenada :\n");
   for(i=0;i<n;i++)
     printf("%5d",a[i]);
   printf("\n");
 
 
}
