//Milton Orlando Sarria 
//USC
/*
Juego simple donde se usan diferentes elementos del lenguaje C
se debe inicializar un entero de forma aleatoria y el usuario debe adivinarlo
el programa termina cuando el usuario ha adivinado el entero
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    int x, n, run;
    time_t t;
   
    
    srand((unsigned) time(&t));
    
    n = rand()%10;  
    printf("Estoy pensando un numero entre 1 y 10, adivinalo!!\n") ;
    run =1;
    while(run==1)
    {
    printf("Tu piensas que es el numero:  ");
    scanf("%d",&x);
    if(n==x)
        {
        printf("Muy bien, %d es correcto! \n",x) ;
        run=0;
        }
    else
        {
        if (x<n)
            printf("Intenta con un numero mayor\n");
        else
            printf("Intenta con un numero menor\n");
        }
     
    }
    
    return 1;
}
