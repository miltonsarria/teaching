/*******************************************************************************
programa que carga y guarda un aimagen bmp, menor que 400x400
Realizado por:
Maria Constanza Torres Madroñero
Milton Orlando Sarria Paja
Ing. Electronica
Universidad Nacional de Colombia
Septiembre 2005
*******************************************************************************/

#include <conio.h>
#include <stdio.h>
#include <iostream.h>
#include <stdlib.h>
#include "fun1.h"
#include "bmp_milton.h"

#define ext ".bmp"
#define ext2 ".txt"
int main()
{
 int fc[3],s,c,op,c1,l1,tm;
 float fil[13][13];
 int brillo,contraste,i,j;
 char nombre1[12],nombre2[12],nombrea[12];
 //-----------------memoria dinamica
 // filas y columnas
 int m = 1000,n = 1000;
 long int **mat; //matriz para la imagen
 mat = new long int*[m];
 if (mat == NULL)
	{
	cout << "no se puede asignar memoria";
   getch();
   return 0;
   //exit(EXIT_FAILURE);
 	}
 for (int j = 0; j < m; j++)
	 {
    mat[j] = new long int[n];
     if (mat[j] == NULL)
    	 	{
	 		 cout << "no se puede asignar memoria";
          getch();
			 return 0;
	 		 //exit(EXIT_FAILURE);
          }
     }
 //-----------------------------------
 cout<<"ingrese archivo:";
 cin>>nombre1;
 //juntar(nombre1,ext);
 strcat(nombre1,ext);
 c=bmp256(nombre1,mat,fc);  //fc[fil,col,numero de ceros]
 if(c==0) {cout<<"no se pudo abrir el archivo!! \n"; getch(); return 0;}
 //operaciones a relizar
 cout<<"\n"<<"Operaciones a realizar  : \n";
 cout<<"1. Ajuste de brillo y contraste \n";
 cout<<"2. Convolucion \n"<<"Op: ";
 cin>>op;
 cout<<"ingrese archivo destino: ";
 cin>>nombre2;
 //
 switch(op)
          {
          case 1:   cout<<"Brillo? (intercepto en x): ";
                    cin>>brillo;
                    cout<<"Contraste (pendiente) ??: ";
                    cin>>contraste;
                    bricont(mat,brillo,contraste,fc);
                    break;
          case 2:   cout<<"Ingrese la mascara : \n";
                    tm=recfil(fil);
                    convolucion(mat,fc,fil,tm);

          }

 ///////////////////////////////////////////////////////////////////////////////

 l1=strlen(nombre2);
 for(i=0;i<l1;i++)
 nombrea[i]=nombre2[i];

 strcat(nombre2,ext);
 //juntar(nombre2,ext);
 s=salvar(nombre1,nombre2,mat,fc);

   if(s==0)   //||
     {
   strcat(nombrea,ext2);
   //juntar(nombrea,ext2);
   cout<<"No se pudo cargar el encabezado, o no se pudo guardar el archivo!! \n";
   cout<<"se guardara como: "<<nombrea<<"\n";
   salvartxt(mat,nombrea,fc);
     }



 cout<<"Finalizado, press. ENTER.....";
 getch();
 des_asignar(mat,m);
 return 1;
}



 //cout<<fc[0]<<" "<<fc[1]<<"\n";
 //imprimo la matriz
 /*
 /-----------------
 for(int f=0;f<fc[0];f++)
  {
   for(int c=0;c<fc[1];c++)
    {
     cout<<mat[f][c]<<" ";
     }
    cout<<"\n";
  }*/
 //getch();
