#include <stdlib.h>
#include <stdio.h> 

int main()
{
 char line[255]; //se pueden guardar 255 caracteres
 FILE *fpointer = fopen("archivo1.txt","r");

 fgets(line,255,fpointer); //primera linea
 printf("%s",line);
 
 fgets(line,255,fpointer); //segunda linea
 printf("%s",line);

 fclose(fpointer);

return 0;

}

