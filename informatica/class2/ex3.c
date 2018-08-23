#include <stdio.h>
#include <stdlib.h>


int swap(int *a, int *b);

int main()
{
    int i, n, a[2];
    n=2;
    for(i=0;i<n;i++)
            scanf("%d",&a[i]);
    printf("Valores ingresados:\n");
    
    for(i=0;i<n;i++)
     printf("%5d",a[i]);
    
    printf("\nIntercambio de valores:\n");
    swap(&a[0],&a[1]);
    for(i=0;i<n;i++)
     printf("%5d",a[i]);

    printf("\n");

}

int swap(int *a, int *b)
{
int t;
  t=*a;
  *a=*b;
  *b=t;
             
return 1;
}

/*

int max(int num1, int num2) {

  
   int result;
 
   if (num1 > num2)
      result = num1;
   else
      result = num2;
 
   return result; 
}

*/
