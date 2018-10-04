void cesar_cifrado(char cipher[], int shift);
void cesar_descifrado(char cipher[], int shift);


void cesar_cifrado(char cipher[], int shift) 
{
  for(int i=0; cipher[i] != '\0'; i++)
    cipher[i] = 65 + (cipher[i]-65+shift)%26;
  printf("Texto cifrado: %s\n", cipher);
}


void cesar_descifrado(char cipher[], int shift) {
  for(int i=0; cipher[i] != '\0'; i++)
    cipher[i] = 65 + (cipher[i]-65-shift)%26;
  printf("Texto descifrado: %s\n", cipher);
}

