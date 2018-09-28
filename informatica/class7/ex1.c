#include <stdio.h>

struct student
{
    char  name[50];
    int   numero;
    float nota;
} sts[10];



int main()
{
    int i;

    printf("Ingresar la informacion de estudiantes:\n");

    // guardar la informacion
    for(i=0; i<10; ++i)
    {
        sts[i].numero = i+1;

        printf("\nPara el estudiante: %d,\n",sts[i].numero);

        printf("Ingrese el nombre: ");
        scanf("%s",sts[i].name);

        printf("Ingresar calificacion: ");
        scanf("%f",&sts[i].nota);

        printf("\n");
    }

    printf("Mostrar informacion:\n\n");
    // Mostrar toda la informacion guardada
    for(i=0; i<10; ++i)
    {
        printf("\nEstudiante numero: %d\n",i+1);
        printf("Nombre: ");
        puts(sts[i].name);
        printf("Calificacion: %.1f",sts[i].nota);
        printf("\n");
    }
    return 0;
}
