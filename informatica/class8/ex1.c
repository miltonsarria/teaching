#include <stdlib.h>
#include <stdio.h>
#include <string.h>
void cesar_cifrado(char cipher[], int shift);
int main () {
    char *buffer;
    size_t bufsize = 256;
    size_t n;

    buffer = (char *)malloc(bufsize * sizeof(char));
    if( buffer == NULL)
    {
        perror("ERROR: no se puede asignar memoria");
        exit(1);
    }
    
   char cipher[50];
   int shift; 
   printf("Texto a cifrar (solo mayusculas): ");
  //scanf("%s", cipher);
  n=getline(&buffer,&bufsize,stdin);
  buffer[n-1]='\0';
  strcpy(cipher,buffer);
  
  printf("Usted digito: %s\nEn total %d caracteres \n",cipher,n);
    
  printf("Ingresar el corrimiento: ");
  scanf("%d", &shift);

  cesar_cifrado(cipher, shift);
    
  return 0;
}

void cesar_cifrado(char cipher[], int shift) {
  for(int i=0; cipher[i] != '\0'; i++)
    cipher[i] = 65 + (cipher[i]-65+shift)%26;
  printf("Texto cifrado: %s\n", cipher);

}




