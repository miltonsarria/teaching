#include <stdio.h>  
#include <stdlib.h>  
  
void main()
{
    char str[50];
	
    printf("\n\nRecibir un string desde el teclado :\n");
    printf("-----------------------------------\n"); 	
    printf("Ingresar el string : ");
    fgets(str, sizeof str, stdin);
    printf("usted ingreso : %s\n", str);
}
