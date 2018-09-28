#include <stdio.h>

#define MAX_STUDENTS 20
struct student
{
    char  name[50];
    int   numero;
    float nota;
};


int showInfo(struct student registro[], int n);

int main()
{
    int i;
    struct student sts[MAX_STUDENTS];
    printf("Ingresar la informacion de estudiantes:\n");
    
    // guardar la informacion
    for(i=0; i<3; ++i)
    {
        sts[i].numero = i+1;

        printf("\nPara el estudiante: %d,\n",sts[i].numero);

        printf("Ingrese el nombre: ");
        scanf("%s",sts[i].name);

        printf("Ingresar calificacion: ");
        scanf("%f",&sts[i].nota);

        printf("\n");
    }

    showInfo(sts,3);
    return 0;
}

/* Funcion para mostrar registros*/
int showInfo(struct student registro[], int n)
{
    int i;
    printf("Mostrar informacion:\n\n");
    // 
    for(i=0; i<n; ++i)
    {
        printf("\nEstudiante numero: %d\n",i+1);
        printf("Nombre: ");
        puts(registro[i].name);
        printf("Calificacion: %.1f",registro[i].nota);
        printf("\n");
    }
}
