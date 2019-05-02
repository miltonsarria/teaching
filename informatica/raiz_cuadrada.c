#include <stdio.h>
#include <stdlib.h>

int main()
{
float n, a_i=1, a_i_1,d=1000,epsilon=0.00001;
printf("Digite el numero n: ");
scanf("%f",&n);

while(d>epsilon)
    {
     a_i_1=(a_i+n/a_i)/2;    
     d=a_i_1-a_i;
     
     printf("%f\n",a_i_1);
     a_i=a_i_1;
     
     if(d<0) d=-1*d;    
    }


printf("raiz cuadrada de %f es %f \n",n,a_i_1);


return 1;

}
