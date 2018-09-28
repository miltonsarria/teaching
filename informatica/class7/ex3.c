#include <stdio.h>

#define MAX_STUDENTS 20
struct student
{
    char  name[50];
    int   numero;
    float nota;
};


int showInfo(struct student registro[], int n);
int getInfo(struct student *registro, int n);

int main()
{
    int i;
    struct student sts[MAX_STUDENTS];
    printf("Ingresar la informacion de estudiantes:\n");
    for(i=0;i<3;i++)
       getInfo(&sts[i], i+1);

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
        printf("\nEstudiante numero: %d\n",registro[i].numero);
        printf("Nombre: ");
        puts(registro[i].name);
        printf("Calificacion: %.1f",registro[i].nota);
        printf("\n");
    }
}


/* Funcion para obtener la informacion */
int getInfo(struct student *registro, int n)
{


// guardar la informacion

        printf("\nPara el estudiante: %d\n",n);
         
        registro->numero = n;
        printf("Ingrese el nombre: ");
        scanf("%s",registro->name);

        printf("Ingresar calificacion: ");
        scanf("%f",&registro->nota);

        printf("\n");
}

