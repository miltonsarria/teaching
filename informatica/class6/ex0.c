<<<<<<< HEAD
/* punteros
Milton Orlando Sarria Paja
*/

#include <stdio.h>
#include <stdlib.h>
//prototipo
int receiv_M(int M1[10][10], int M,int N);

/*funcion principal*/
int main()
{

    int A[10][10], fil,col;
    
    printf("Ingresar el numero de filas:\n");
    scanf("%d",&fil);
    printf("Ingresar el numero de columnas:\n");
    scanf("%d",&col);
    
    receiv_M(A,fil,col);
    
    printf("La matriz ingresada es: \n");
    for (int i=0; i < fil; i++)
        {
        for (int j=0; j < col; j++)
            {
            printf("%d\t",A[i][j]);
            }
           printf("\n");
        }
}    

/*funcion para recibir una matriz definida por el usuario    */
int receiv_M(int M1[10][10], int M,int N)
{
int valor;
for (int i=0; i < M; i++)
    for (int j=0; j < N; j++)
        {
        printf("ingresar valor (%d,%d): ",i,j);
        scanf("%d",&valor);
        M1[i][j]=valor;
        }
return 1;
}    

=======
#include <stdio.h>

int main()
{
    int i=1;
    while(++i <= 5)
        printf("%d ",i++);
    return 1;
    
}
>>>>>>> exam
