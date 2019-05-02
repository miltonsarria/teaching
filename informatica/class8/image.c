#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "bmp_milton.h"

#define ext ".bmp"
#define ext2 ".txt"

int main()
{
 int fc[3],s,c,op,c1,tm;
 float fil[13][13];
 int brillo,contraste,i,j;
 char nombre1[12],nombre2[12];
 //-----------------memoria dinamica
 // filas y columnas
 int m = 1000,n = 1000;
 //long int **mat; //matriz para la imagen
 int **mat = NULL;
 mat = Matrix_Alloc(mat, m, n);
 
 //-----------------------------------
 printf("ingrese archivo:");
 scanf("%s",nombre1);
 //juntar(nombre1,ext);
 strcat(nombre1,ext);
 c=bmp256(nombre1,mat,fc);  //fc[fil,col,numero de ceros]
 if(c==0) 
 {
    printf("no se pudo abrir el archivo!! \n"); 
    getchar(); 
    return 0;
 }
 
 ///
 printf("ingrese archivo destino: ");
 scanf("%s",nombre2);
 //modificar para que nombre 1 sea diferente de nombre2
 //operaciones a relizar
 //modificar el siguiente codigo para
 //-aplicar brillo y contraste
 //-umbralizar
 for (i=0;i<fc[0];i++)
    {
    for(j=0;j<fc[1];j++)
        {
         mat[i][j]=255-mat[i][j];
        }
     }
 ///////////////////////////////////////////////////////////////////////////////

 strcat(nombre2,ext);
 //juntar(nombre2,ext);
 s=salvar(nombre1,nombre2,mat,fc);

 printf("Finalizado, press. ENTER.....\n");
 getchar();
 Matrix_Free(mat,m);
 return 1;
}


