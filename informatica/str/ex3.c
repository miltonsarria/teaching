#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char line[255]; //se pueden guardar 255 caracteres
        FILE *fpointer = fopen("config_file.txt","r"); //puntero a un archivo
        int n=255;
        while(fgets(line, n, fpointer)!=NULL)
              printf("%s",line); //imprimir el resultado, la linea que se ha leido
	
	return 0;
	
}

