/*------------------------------------------------------------------------------
Milton Orlando Sarria
Ingenieria Electrónica
Universidad Nacional De Colombia (sede manizales)
Modulo de reconocimiento de patrones
------------------------------------------------------------------------------*/
#include <conio.h>
#include <stdio.h>
#include <iostream.h>
#include <stdlib.h>
#include <math.h>
#include "fun1.h"
#include "typemat.h"
//------------------------------------------------------------------------------
void aleatorio(int num,int pos[30],int cant);
int leerarch(float **dat,int fc[]);
void mostrar(struct MATRIX a);
float evaluar(struct MATRIX u,struct MATRIX imc,struct MATRIX car,float det,float p);
void put_matrix(struct MATRIX &a);
int separar(int fc[],float **dat,struct MATRIX &val);
int clase(float meanv[5][10],struct MATRIX inversas[],int fc[],float deter[], float priori[],struct MATRIX x);
//------------------------------------------------------------------------------
int main()
{
 MATRIX inversas[6],aux,x,valid,mtconf;
 int c,fc[3],nrpcl[5],tm[6],clv,r1;
 float meanv[5][10],covm[5][10][10],deter[5],priori[6],err[201];
 //fc[# de registros,(# de caracteristicas por registro)+1,# de clases]
 //------
 cout<<"Universidad Nacional de Colombia (Sede Manizales)"<<endl;
 cout<<"Milton Orlando Sarria Paja  Cod. 80801555"<<endl<<endl;
 cout<<"Bootstrap"<<endl<<endl;
 //------
 int m = 1000,n= 1000;
 float **mat;
 mat = new float*[m];
 if (mat == NULL) return 0;
 for (int j = 0; j < n; j++)
	 {
    mat[j] = new float[n];
    if (mat[j] == NULL) return 0;
    }
 float **mat2;
 mat2 = new float*[m];
 if (mat2 == NULL) return 0;
 for (int j = 0; j < n; j++)
	 {
    mat2[j] = new float[n];
    if (mat2[j] == NULL) return 0;
    }
 //------

 c=leerarch(mat,fc);
 if(c==0) {cout<<"no se puede"; getch(); return 0;}
 cout << "numero de registros                    :" << fc[0] << endl;
 cout << "numero de caracteristicas por registro :" <<( fc[1]-1 )<< endl;
 cout << "numero de clases                       :" << fc[2] << endl;

 nrpclf(fc,mat,nrpcl);

 for(int i=0;i<fc[0];i++)
   for(int j=0;j<fc[1];j++)
     mat2[i][j]=mat[i][j];


 //----------boostrap


 for(int vln=0;vln<200;vln++)
 {
   r1=0.37*fc[0];
   separar(fc,mat,valid);
   mtconf.m=fc[2]; mtconf.n=fc[2];
 	valid.m=r1; valid.n=fc[1];

 	 //extraccion de parámetros
 	media(meanv,mat,fc,nrpcl);
 	mtcov(nrpcl,fc,mat,meanv,covm);

  //-determinantes de las matrices de covarianza
  //-inversas de las matrices de covar
  //-probabilidades a priori
 	aux.m=fc[1]-1;
 	aux.n=fc[1]-1;
 	for(int cl=0;cl<fc[2];cl++)
 		{
  		for(int i=0;i<aux.m;i++)
    	for(int j=0;j<aux.n;j++)
  			 aux.element[i][j]=covm[cl][i][j];

  		deter[cl]=determinante(aux);
      inversas[cl]=elevar(aux, -1);
 		priori[cl]=(float)nrpcl[cl]/fc[0];
 		}

   //--
   x.m=fc[1]-1; x.n=1;
   for(int i=0;i<mtconf.m;i++)
  		for(int j=0;j<mtconf.n;j++)
   		 mtconf.element[i][j]=0;

	for(int i=0;i<valid.m;i++)
     	{
   	 for(int j=1;j<valid.n;j++)
       		x.element[j-1][0]=valid.element[i][j];
       c=clase(meanv,inversas,fc,deter,priori,x);
       clv=valid.element[i][0];
 		 mtconf.element[clv][c]+=1;
      }


    err[vln]=0;
    for(int i=0;i<mtconf.m;i++)
    	err[vln]+=mtconf.element[i][i];

    err[vln]=(float)err[vln]/(r1)*100;

  //--------
 for(int i=0;i<fc[0];i++)
   for(int j=0;j<fc[1];j++)
     mat[i][j]=mat2[i][j];

 }
float erp=0;
 for(int i=0;i<200;i++)
   erp+=err[i];

 cout<<endl<<"Efectividad : "<<erp/200;


 getch();

 des_asignar(mat,n);
 des_asignar(mat2,n);
 return 1;
}
//------------------------------------------------------------------------------
int leerarch(float **dat,int fc[])
 {
 char nombre[12];
 float d,A,B,D;
 int i,j;
 FILE *fp;
 cout << "Base de datos : ";
 cin>>nombre;
 if((fp=fopen(nombre,"rb"))==NULL) return 0;
 fscanf(fp,"%f5.5",&A);
 fscanf(fp,"%f5.5",&B);
 fscanf(fp,"%f5.5",&D);
 fc[0]=A; fc[1]=B; fc[2]=D;
 for(i=0;i<fc[0];i++)
     for(j=0; j<fc[1]; j++)
        {  fscanf(fp,"%f5.5",&d);
           dat[i][j]=d;
        }
 fclose(fp);
 return 1;
}
//------------------------------------------------------------------------------
void mostrar(struct MATRIX a)
 {
 for(int i=0;i<a.m;i++)
   {
    for(int j=0;j<a.n;j++)
			cout<<a.element[i][j]<<"\t";
   cout<<endl;
   }
 }
//------------------------------------------------------------------------------
float evaluar(struct MATRIX u,struct MATRIX imc,struct MATRIX x,float det,float p)
 {
 MATRIX res1,res2,xt,ut;
 float g,k1,k2,k3,k4;
 xt=transpuesta(x);
 ut=transpuesta(u);
 res1=multiplicarm(xt,imc);
 res2=multiplicarm(res1,x);
 k1=res2.element[0][0];
 k1=-1*k1/2;
 //cout<<k1<<endl;

 res1=multiplicarm(imc,u);
 res2=transpuesta(res1);
 res1=multiplicarm(res2,x);
 k2=res1.element[0][0];
 //cout<<k2<<endl;

 res1=multiplicarm(ut,imc);
 res2=multiplicarm(res1,u);
 k3=res2.element[0][0];
 k3=-1*k3/2;
 k4=log(det);
 k3=k3-1*k4/2;
 k4=log(p);
 g=k1+k2+k3+k4;

 return(g);
 }
//------------------------------------------------------------------------------
void put_matrix(struct MATRIX &a)
{
	int i,j;

	cout<<"Ingrese filas: "; cin>>a.m;
	cout<<"Ingrese columnas: ";cin>>a.n;

	for(i=0;i<a.m;i++)
	{
		for(j=0;j<a.n;j++)
		{
			printf("a[%d][%d]= ", i, j);
			cin>>a.element[i][j];
		}
	}
	clrscr();
}
//------------------------------------------------------------------------------
int separar(int fc[],float **dat,struct MATRIX &val)
{
 int f,i,j;
 int pos[300],tm,ind;
 tm=0.37*fc[0];
 aleatorio(fc[0],pos,tm);
 f=0;
 val.m=tm;
 val.n=fc[1];
 for(i=0;i<tm;i++)
	 {
    ind=pos[i];
    for(j=0;j<fc[1];j++)
       val.element[f][j]=dat[ind][j];
    f++;
    for(j=0;j<fc[1];j++)
       dat[ind][j]=dat[abs(ind-1)][j];
    }


 return 1;
}
//------------------------------------------------------------------------------
int clase(float meanv[5][10],struct MATRIX inversas[],int fc[],float deter[], float priori[],struct MATRIX x)
{
 MATRIX u;
 float g[6];
 u.m=fc[1]-1;
 u.n=1;
 int max=0;
 //--
 for(int cl=0;cl<fc[2];cl++)
  {
 	for(int i=0;i<fc[1]-1;i++)
    u.element[i][0]=meanv[cl][i];

  g[cl]=evaluar(u,inversas[cl],x,deter[cl],priori[cl]);
  }

for(int i=0;i<fc[2];i++)
	if(g[i]>g[max]) max=i;

return(max);
}
//------------------------------------------------------------------------------
void aleatorio(int num,int pos[30],int cant)
{
 int i,j,sel[1000],cont=0;
 randomize();
 for(i=0;i<num;i++)
      sel[i]=0;

 while(cont<cant)
   {
    j=rand()%num;
     if(sel[j]==0)
       {
       pos[cont]=j; cont++;
       sel[j]=1;
       }
   }
}

