#include <stdio.h>

#define MAX_STUDENTS 20
struct student
{
    char  name[50];
    float nota;
};


int showInfo(struct student registro);
int getInfo(struct student *registro);

int main()
{
    int i;
    struct student sts;
    printf("Ingresar la informacion del estudiante:\n");
    
    getInfo(&sts);

    showInfo(sts);
    return 0;
}

/* Funcion para mostrar registros*/
int showInfo(struct student registro)
{
    printf("Mostrar informacion:\n\n");

    printf("\nEstudiante: \n");
    printf("Nombre: ");
    puts(registro.name);
    printf("Calificacion: %.1f",registro.nota);
    printf("\n");

}


/* Funcion para obtener la informacion */
int getInfo(struct student *registro)
{


// guardar la informacion

        printf("\nPara el estudiante: \n");

        printf("Ingrese el nombre: ");
        scanf("%s",registro->name);

        printf("Ingresar calificacion: ");
        scanf("%f",&registro->nota);

        printf("\n");
}

