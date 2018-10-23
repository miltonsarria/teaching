/*******************************************************************************
programa que carga y guarda una imagen bmp, menor que 400x400
Realizado por:
Milton Orlando Sarria Paja
Ing. Electronica
*******************************************************************************/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
//////////////////////////////////////////////////////////

int** Matrix_Alloc(int** matrix, int rows, int columns)
{
    int i;
    matrix=malloc(sizeof(int)*rows*columns);
    if(matrix!=NULL)
    {
        /*Asignar espacio para cada fila*/
        for(i=0; i<rows;i++)
        {
            matrix[i] = malloc(sizeof(int)*columns);
            if(matrix[i]==NULL)
            {
                return NULL;
            }
        }
    }
    return matrix;
}
/*liberar memoria*/
void Matrix_Free(int** matrix, int rows)
{
    int i;
    for(i = 0; i < rows; i++)
    {
        free(matrix[i]);
    }
    free(matrix);
}


//////////////////////////////////////////////////////////
/*----------------------------------------------------------------------------*/
int bmp256(char *imagen, int **mat,int tfc[])
{
  int cont=-1,i,fila,tamc,tamf,c1,log,n;
  FILE *fi;

  if((fi=fopen(imagen,"rb"))==NULL) return 0;

  while(cont++<=117)
	if(cont==18){tamc=fgetc(fi)|fgetc(fi)<<8;cont++;}
	else if(cont==22){tamf=fgetc(fi)|fgetc(fi)<<8;cont++;}
	else fgetc(fi);
   tfc[0]=tamf;
   tfc[1]=tamc;

 
i=0;
fila=0;
fseek(fi,0,2);
log=ftell(fi);
n=(log-1078-tamf*tamc)/tamf;
fseek(fi,1078,0);

tfc[2]=n;
do
{
  c1=fgetc(fi);
  if(c1!= -1)
   {
    mat[fila][i]=c1;
    i+=1;
    if(i==tamc)
    {
     i=0; fila+=1;
     for(log=0;log<n;log++) fgetc(fi);
    }
   }

} while (c1 != -1);
  fclose(fi);
  return 1;
}
/*----------------------------------------------------------------------------*/
//////////////////////////////////////////////////////////

int salvar(char *name,char *name2, int **mat,int fc[])
{
 FILE *fp1;
 FILE *fp2;
 int cont=-1,encab[1080],c1;


 if((fp1=fopen(name,"rb"))==NULL) return 0;
 while(cont++<1079)
  encab[cont]=fgetc(fp1);
  fclose(fp1);

 if((fp2=fopen(name2,"wb"))==NULL) return 0;
 for(cont=0;cont<1078;cont++)
 fprintf(fp2, "%c",encab[cont]);
 int fi;
 for(fi=0;fi<fc[0];fi++)
  {
   int co;
   for(co=0;co<fc[1];co++)
     {
      c1=mat[fi][co];
      fprintf(fp2,"%c",c1);
     }
   int i;
   for(i=0;i<fc[2];i++) fprintf(fp2,"%c",'\0');
  }

 fclose(fp2);
 return 1;
}                   //[103][103]
/******************************************************************************/
int juntar(char *name,char *ex)
{
int n;
n=strlen(name);
name[n]=ex[0];
name[n+1]=ex[1];
name[n+2]=ex[2];
name[n+3]=ex[3];
name[n+4]='\0';
}
/****************************************salvar txtx***************************/
int salvartxt( int **mat,char *nombrea,int fc[])
{
int c1;
FILE *text;
 
   text=fopen(nombrea,"w");
   int f;
   for(f=(fc[0]-1);f>=0;f--)
  	    {
  	int c;    	
   	for(c=0;c<fc[1];c++)
    		{
         	c1=mat[f][c];
     		fprintf(text,"%d",c1);
            fprintf(text,"%c",'\t');
     		}
    		fprintf(text,"%c",10);
        }

return 1;
}
