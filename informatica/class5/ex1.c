#include <stdlib.h>
#include <stdio.h>

int main ()
{
    int *num = malloc(sizeof(int)*3);
    
    num[0]=10;
    num[1]=15;
    num[2]=20;
    
    #if 1
    
    printf("%p -> %d \n", num, *num);
    printf("%p -> %d \n", num+1, *(num+1));
    printf("%p -> %d \n", num+2, *(num+2));
    
    #endif
    
    /*
    printf("%d \n", num[0]);
    printf("%d \n", num[1]);
    printf("%d \n", num[2]);                
    */
}
