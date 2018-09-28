#include <stdlib.h>
#include <stdio.h> //warning

int main()
{

FILE *fpointer = fopen("archivo1.txt","w");

//sobre escritura
fprintf(fpointer,"mi primer linea");

fclose(fpointer);
return 0;

}
