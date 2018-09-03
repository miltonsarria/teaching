/* 
Milton Orlando Sarria Paja
USC
estructuras
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h> 

//nombre de las estructuras con primera letra mayuscula
//tipo especial de dato que se llama Estudiante
struct Estudiante 
{
    char nombre[50];
    char carrera[50];
    int edad;
    float promedio;
};

int main()
{
    struct Estudiante estudiante1;
    
    estudiante1.edad = 22;
    estudiante1.promedio=4.1;
    strcpy(estudiante1.nombre,"Juanito Perez");
    strcpy(estudiante1.carrera,"Ing. Electronica");
    
    printf("Datos del estudiante:\n");
    printf("Nombre  : %s\n", estudiante1.nombre);
    printf("Carrera : %s\n", estudiante1.nombre);
    printf("Edad    : %d\n", estudiante1.edad);
    printf("Promedio: %2.2f\n\n", estudiante1.promedio);
    
    
    struct Estudiante estudiante2;
    estudiante1.edad = 24;
    estudiante1.promedio=3.1;
    strcpy(estudiante1.nombre,"Maria Molina");
    strcpy(estudiante1.carrera,"Ing. Electronica");
    
    
    
    
return 1;
}
