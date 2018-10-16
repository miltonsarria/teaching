#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char str[64];
	int n=64;
	char name[10];
	int age;
	
	fgets(str, n, stdin);  //obtener cadena de caracteres
	n=strnlen(str,64);    //calcular su longitud
	printf("%s %d \n\n",str,n); //imprimir el resultado, la entrada y su longitud
	
	
	sscanf(str,"%s %d",name,&age);
	n=strcmp(name,"Milton");
	printf("name: %s age: %d es: %d",name,age,n);
	  

	return 0;
	
}
