#include <stdio.h>
#include <stdlib.h>

int main()
{
    int     edad;
    float   estatura;
    char    genero;
        
    edad=20;
    estatura=1.80;
    genero ='M';
    
    printf("Valores de las variables:\n");    
    printf("Edad: %d, Estatura: %f, Genero: %c \n\n",edad, estatura,genero);
    

    int     *pEdad     = &edad;
    float   *pEstatura = &estatura;
    char    *pGenero   = &genero;
      
    printf("Direcciones de memoria:\n");
    printf("Edad: %p, Estatura: %p, Genero: %p \n\n",pEdad, pEstatura,pGenero);

    printf("Referenciar el valor del apuntador:\n");
    printf("Edad: %d, Estatura: %f, Genero: %c \n\n",*pEdad, *pEstatura,*pGenero);
    
    *pEdad = 50;
    printf("Modificar datos:\n");
    printf("Edad *: %d, Edad: %d \n\n",*pEdad, edad);
    
    printf("Direccion de memoria:\n");
    printf("Edad *: %p, Edad: %p \n\n",&*pEdad, &edad);
    
    
    
    
    
    
        
return 1;    
}
