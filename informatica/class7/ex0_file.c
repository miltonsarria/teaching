#include <stdlib.h>
#include <stdio.h> //warning

int main()
{

FILE *fpointer = fopen("archivo1.txt","w");

fclose(fpointer);
return 0;

}
