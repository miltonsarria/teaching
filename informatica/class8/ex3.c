#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "cifrado.h"

int main () {
    char *buffer;
    size_t bufsize = 256;
    size_t n;

    /*buffer = (char *)malloc(bufsize * sizeof(char));
    if( buffer == NULL)
    {
        perror("ERROR: no se puede asignar memoria");
        exit(1);
    }*/
    
   char cipher[50];
   int shift; 
   buffer=cipher;
   printf("Texto a cifrar (solo mayusculas): ");
   n=getline(&buffer,&bufsize,stdin);
   buffer[n-1]='\0';
   printf("Usted digito: %s\nEn total %zu caracteres \n",buffer,n);
  
   //strcpy(cipher,buffer);
   printf("Ingresar el corrimiento: ");
   scanf("%d", &shift);

   cesar_cifrado(cipher, shift);
   cesar_descifrado(cipher, shift);
  
   return 0;
}

