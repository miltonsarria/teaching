#include <stdlib.h>
#include <stdio.h> //warning

int main()
{

FILE *fpointer = fopen("archivo1.txt","a");

//sobre escritura
fprintf(fpointer,"\nmi segunda linea");

fclose(fpointer);
return 0;

}
