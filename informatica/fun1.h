/*------------------------------------------------------------------------------
Funciones para sacar los parametros de las caracteristicas
Milton Orlando Sarria Paja Cod. 080155
UNAL
------------------------------------------------------------------------------*/
void des_asignar(float **mat, int n)
{
 for (int i = 0; i < n;  i++)
      delete[] mat[i]; //borrar columnas
 delete[] mat;         //borrar filas
}
//------------------------------------------------------------------------------

 int media(float vm[5][10],float **dat,int fc[],int contcl[])
 {
 int i,j,indc;
 for(i=0;i<fc[2];i++)
 	for(j=0;j<(fc[1]-1);j++)
    vm[i][j]=0;

 for(i=0;i<fc[2];i++)
    contcl[i]=0;
 for(i=0;i<fc[0];i++)
   {
   indc=dat[i][0];
   contcl[indc]+=1;
   for(j=1; j<fc[1]; j++)
     vm[indc][j-1]+=dat[i][j];
   }

 for(i=0;i<fc[2];i++)
 	for(j=0;j<(fc[1]-1);j++)
    vm[i][j]=(float)vm[i][j]/contcl[i];

 return 1;
 }

//------------------------------------------------------------------------------
 int escojer(int cl,float **dat,float **mat,int fc[])
 {
 int f=0;
 for(int i=0;i<fc[0];i++)
 	{
   if(dat[i][0]==cl)
 		{
      for(int j=1;j<fc[1];j++)
         mat[f][j-1]=dat[i][j];
      f++;
      }
   }
 return 1;
 }
//------------------------------------------------------------------------------
int mtcov(int crpc[],int fc[],float **dat,float meanv[5][10],float covm[5][10][10])
 {
 //----
 int m = 1000,n= 1000;
 float **mat;
 mat = new float*[m];
 if (mat == NULL) return 0;
 for (int j = 0; j < n; j++)
	 {
    mat[j] = new float[n];
    if (mat[j] == NULL) return 0;
    }
 //----
 float sum;
 int cl,i,j,x;

 for(cl=0;cl<fc[2];cl++)
  {
  //escojer(int cl,float **dat,float **mat,int fc)
  escojer(cl,dat,mat,fc);
  for(i=0;i<(fc[1]-1);i++)
    for(j=0;j<(fc[1]-1);j++)
     {
     sum=0;
     for(x=0;x<crpc[cl];x++)
       //for(y=0;y<crpc[cl];y++)
        {
        sum=sum+(float)(mat[x][i]-meanv[cl][i])*(mat[x][j]-meanv[cl][j]);
        }
     covm[cl][i][j]=sum/(crpc[cl]-1);
     }
  }
 return 1;
 }
//------------------------------------------------------------------------------
void nrpclf(int fc[],float **dat,int nrpcl[])
{
int ind;
for(int j=0;j<fc[2];j++)
	nrpcl[j]=0;

for(int i=0;i<fc[0];i++)
	{
    ind=dat[i][0];
    nrpcl[ind]+=1;
   }
}
//------------------------------------------------------------------------------

