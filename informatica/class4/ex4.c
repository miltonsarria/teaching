#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define str_size 100 //maxima longitud
void main()
{
    char str[str_size];
    int i, wrd;
    printf("\n\nContar cuantas palabras hay en un string :\n");
    printf("------------------------------------------------------\n"); 	
    printf("Input the string : ");
    fgets(str, sizeof str, stdin);	
	
    i = 0;
    wrd = 1;
    while(str[i]!='\0')
    {
       if(str[i]==' ' || str[i]=='\n' || str[i]=='\t')
        {
            wrd++;
        }
        i++;
    }
    printf("El numero total de palabras es : %d\n", wrd-1);
}

