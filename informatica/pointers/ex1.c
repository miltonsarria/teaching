#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    char *message0 = "Hello world!";
    printf("%p\n",message0);
    printf("%s\n",message0);
   
    char *message1;
    message1 = "Hello world!";

    printf("%p\n",message1);
    printf("%s\n",message1);

    
    return 1;    
}
