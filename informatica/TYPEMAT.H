/*
	TYPEMAT.H
	Cabcera con funciones para determinar
	el tipo de matriz del que se trata
	y las funciones para operar con matrices

	Programado por Ignacio Rigoni
*/

#define TRUE 1
#define FALSE -1
#define TRIANGULAR_SUPERIOR 1
#define TRIANGULAR_INFERIOR 2
#define DIAGONAL 3
#define ESCALAR 4
#define ESCALONADA 5
#define ESCALONADA_REDUCIDAD 6
#define SIMERTRICA 7
#define ANTISIMETRICA 8
#define INVERSA 9
#define TRANSPUESTA 10

// Definici¢n de la estructura MATRIZ
typedef struct MATRIX {
	float element[20][100]; //elementos de la matriz
	int n; //n§ de columnas
	int m; //n§ de filas
}MATRIX;

///////////////////////
// TIPOS DE MATRICES //
///////////////////////
int es_mts(struct MATRIX a); // Es Triangular Superior?
int es_mti(struct MATRIX a); // ""     "      Inferior?
int es_inversa(struct MATRIX a); // Es Inversa de si misma?
int es_inversible(struct MATRIX a); //Tiene inversa?
int es_simetrica(struct MATRIX a); // simetrica?
int es_antisimetrica(struct MATRIX a); //antisimetrica?
int es_diagonal(struct MATRIX a);//diagonal?
int es_escalar(struct MATRIX a);//escalar?
int es_escalonada(struct MATRIX a);//escalonada?
int es_escalonada_reducida(struct MATRIX a);//esc. reducida?
int es_nula(struct MATRIX a);//es nula?
int es_fila(struct MATRIX a);//es fila?
int es_columna(struct MATRIX a);//es columna?
int es_cuadrada(struct MATRIX a);//es una matrix cuadrada?
int es_identidad(struct MATRIX a); //es la iedntidad?

/////////////////
// OPERACIONES //
/////////////////
struct MATRIX transpuesta(struct MATRIX a); //buscar la transpuesta
struct MATRIX inversa(struct MATRIX a); //buscar la inversa
struct MATRIX sumar(struct MATRIX a, struct MATRIX b); //sumar 2 matrices
struct MATRIX multiplicark(struct MATRIX a, float k); //multiplicar por escalar
struct MATRIX multiplicarm(struct MATRIX a, struct MATRIX b); //multiplicar 2 matries
struct MATRIX restar(struct MATRIX a, struct MATRIX b); //restar 2 matrices
struct MATRIX opuesta(struct MATRIX a);// buscar la opuesta (change sign)
struct MATRIX elevar(struct MATRIX a, int p); //elevar una matriz a una potencia
float traza(struct MATRIX a); //devuelve la traza de una matriz
int son_iguales(struct MATRIX a, struct MATRIX b); //compara dos matrices
int rango(struct MATRIX a); //saca el rango de una matriz
int pot1(int a); //Devuelve 1 si a es PAR, -1 si a es IMPAR: (-1)^(f+c) Recordais?
struct MATRIX submatriz(struct MATRIX a, int , int); //crea una submatriz de a, sin la fila f y columna c
float determinante(struct MATRIX a);//determinante de a
struct MATRIX adjunta(struct MATRIX a); //busca la matriz adjunta (tranpuesta de cofactores)
struct MATRIX reducir(struct MATRIX a); //reduce el orden de la matriz en 1 sin cambiar el determinante


////////////////////////
// TIPOS DE FUNCIONES //
////////////////////////
int es_cuadrada(struct MATRIX a)
{
	if(a.m == a.n) return TRUE;
	return FALSE;
}
int es_mts(struct MATRIX a)
{
	int i, j; //  i = fila    j = columna
	if(es_cuadrada(a)!=TRUE) return FALSE;
	for(i = 0; i < a.n; i++)
		for(j = 0; j < a.m; j++)
			if(i > j && a.element[i][j]!=0) return FALSE;
	return TRUE;
}

int es_mti(struct MATRIX a)
{
	int i, j;
	if(es_cuadrada(a)!=TRUE) return FALSE;
	for(i=0;i<a.n;i++)
		for(j=0;j<a.m;j++)
			if(i < j && a.element[i][j]!=0) return FALSE;
	return TRUE;
}

int es_inversa(struct MATRIX a)
{
	if(son_iguales(a, inversa(a))==TRUE) return TRUE;
        return FALSE;
}

int es_simetrica(struct MATRIX a)
{
	struct MATRIX b;
	if(es_cuadrada(a)==FALSE) return FALSE;

	b = transpuesta(a);
	if(son_iguales(a, b)==TRUE) return TRUE;
	return FALSE;
}

int es_antisimetrica(struct MATRIX a)
{
	// -A = A^t
	struct MATRIX b;

	if(es_cuadrada(a)==FALSE) return FALSE;
	if(son_iguales(a, opuesta(transpuesta(a)))==TRUE) return TRUE;
	return FALSE;

}

int es_diagonal(struct MATRIX a)
{
	int i, j;
	if(es_cuadrada(a)!=TRUE) return FALSE;
	for(i=0;i<a.n;i++)
		for(j=0;j<a.m;j++)
			if(i!=j && a.element[i][j]!=0) return FALSE;
	return TRUE;
}

int es_escalar(struct MATRIX a)
{
	int i, j;
	if(es_diagonal(a)!=TRUE) return FALSE;
	for(i=1;i<a.m;i++)
		for(j=1;j<a.n;j++)
			if(i==j && a.element[i][j] != a.element[0][0]) return FALSE;
	return TRUE;
}

int es_nula(struct MATRIX a)
{
	int i, j;
	for(i=0;i<a.m;i++)
		for(j=0;j<a.n;j++)
			if(a.element[i][j]!=0) return FALSE;
	return TRUE;
}

int es_fila(struct MATRIX a)
{
	if(a.n==1) return TRUE;
	return FALSE;
}

int es_columna(struct MATRIX a)
{
	if(a.m==1) return TRUE;
	return FALSE;
}

int es_escalonada(struct MATRIX a)
{
	//ver las tres garchas
        return 0;
}

int es_escalonada_reducida(struct MATRIX a)
{
	int i,j;
	if(es_escalonada(a)!=TRUE) return FALSE;
	//agregar la cuarta garcha
        return 0;
}

int es_identidad(struct MATRIX a)
{
	if(es_escalar(a)==TRUE && a.element[0][0] == 1) return TRUE;
	return FALSE;
}

int es_inversible(struct MATRIX a)
{
	if(determinante(a)!=0) return TRUE;
	return FALSE;
}

//////////////////////////////
// FUNCIONES DE OPERACIONES //
//////////////////////////////

int son_iguales(struct MATRIX a, struct MATRIX b)
{
	int i, j;
	if(a.m != b.m || a.n != b.n) return FALSE;
	for(i=0;i<a.m;i++)
		for(j=0;j<a.n;j++)
			if(a.element[i][j] != b.element[i][j]) return FALSE;
	return TRUE;
}
struct MATRIX transpuesta(struct MATRIX a)
{
	int i, j;
	struct MATRIX b;

	b.n = a.m;
	b.m = a.n;

	for(i=0;i<a.m;i++) {
		for(j=0;j<a.n;j++) {
			b.element[j][i]=a.element[i][j];
		}
	}
	return b;
}

struct MATRIX opuesta(struct MATRIX a)
{
	struct MATRIX b;
	int i, j;

	b.m=a.m; b.n=a.n;
	for(i=0;i<a.m;i++)
		for(j=0;j<a.n;j++)
			b.element[i][j] = -a.element[i][j];
	return b;
}

struct MATRIX sumar(struct MATRIX a, struct MATRIX b)
{
	int i, j;
	struct MATRIX c;

	c.m=a.m; c.n=a.n;
	for(i=0;i<a.m;i++)
		for(j=0;j<a.n;j++)
			c.element[i][j] = a.element[i][j] + b.element[i][j];
	return c;
}

struct MATRIX multiplicark(struct MATRIX a, float k)
{
	int i, j;
	struct MATRIX c;

	c.m=a.m; c.n=a.n;
	for(i=0;i<a.m;i++)
		for(j=0;j<a.n;j++)
			c.element[i][j] = a.element[i][j] * k;
	return c;
}

float rtc(float k)
{
	//Si k est  entre -1e-5 y 1e-5 devuelve 0 (por el problema del rdondeo)
	if (k<0.00001 && k>-0.00001) return 0;
	return k;
}

struct MATRIX multiplicarm(struct MATRIX a, struct MATRIX b)
{
	int i, j, k;
	struct MATRIX c;
	float val=0;
	c.m = a.m;
	c.n = b.n;
	i=j=k=0;

	for(i=0; i < a.m; i++) {

		for(k=0; k<b.n; k++) {
			for (j=0;j<a.n; j++) {
				val = val + a.element[i][j] * b.element[j][k];
			}
			c.element[i][k]=rtc(val);
			val=0;
		}
	}
	return c;
}

struct MATRIX restar(struct MATRIX a, struct MATRIX b)
{
	struct MATRIX c;
	return c=sumar(a, opuesta(b));
}

struct MATRIX elevar(struct MATRIX a, int p)
{
	int i, j;
	struct MATRIX c;
	c.m=a.m;
	c.n = a.n;

	//// pone a C como la Matriz Identidad (o elem. neutro)
	for(i=0;i<c.m;i++) {
		for(j=0;j<c.n;j++) {
			if(i==j) c.element[i][j]=1;
			else c.element[i][j]=0;
		}
	}

	//Si p es negativo, antes de empezar, saca la inversa de a
	//y pone a p positivo
	if(p<0) {
		a = inversa(a);
		p = -p;
	}

	// hace la multiplicaci¢n p-1 veces
	for(i=0;i < p; i++)
		c=multiplicarm(a,c);
	return c;
}

float traza(struct MATRIX a)
{
	int i, j;
	float val=0;

	for(i=0;i<a.m;i++)
		for(j=0;j<a.n;j++)
			if(i==j) val=val+a.element[i][j];
	return val;
}

float determinante(struct MATRIX a)
{
	float val=0;
	int i;

	switch(a.m) {

		case 2: //dvuelve el "este por este menos este por este"
			return (a.element[0][0]*a.element[1][1] - a.element[1][0] * a.element[0][1]);
		case 3: //utiliza a sarrus (no al senor, sino a su metodo)
			return a.element[0][0]*a.element[1][1]*a.element[2][2] + a.element[1][0]*a.element[2][1]*a.element[0][2] + a.element[2][0]*a.element[0][1]*a.element[1][2] - (a.element[0][2]*a.element[1][1]*a.element[2][0] + a.element[1][2]*a.element[2][1]*a.element[0][0] + a.element[2][2]*a.element[0][1]*a.element[1][0]);
		default://La Place o el Desarrola por el adjunto bla bla bla.
			for(i=0; i<a.m; i++)
			{
				val = val + a.element[i][0] * pot1(i+2) * determinante(submatriz(a, i+1, 1));
			}
	}
	return val;
}

struct MATRIX adjunta(struct MATRIX a)
{
	int i, j;
	struct MATRIX b;

	b.m=a.m; b.n=a.n;

	if(a.m==2) {
		b.element[0][0]=a.element[1][1];
		b.element[0][1]=-a.element[1][0];
		b.element[1][0]=-a.element[0][1];
		b.element[1][1]=a.element[0][0];
		return transpuesta(b);
	}
	for(i=0;i<a.m;i++) {
		for(j=0;j<a.n;j++) {
			b.element[i][j]=pot1(i+j)*determinante(submatriz(a, i+1, j+1));
		}
	}
	b=transpuesta(b);
	return b;
}

struct MATRIX inversa(struct MATRIX a)
{
	struct MATRIX b;
	b.m = a.m; b.n = a.n;
	b = multiplicark(adjunta(a), 1/determinante(a));
	return b;
}

int rango(struct MATRIX a)
{
	if(es_inversible(a)==TRUE) return a.m;
	return 0;
}

int pot1(int a)
{
	if(a%2==0) return 1;
	return -1;
}

struct MATRIX submatriz(struct MATRIX a, int f, int c)
{
	int i, j, ci, cj;
	struct MATRIX sb;

	sb.m = a.m-1;  sb.n = a.n-1;
	ci=cj=0;
	for(i=0;i<sb.m;i++) {
		if(i==f-1) ci++;
		for(j=0;j<sb.n;j++) {
			if(j==c-1) cj++;
			sb.element[i][j]=a.element[i+ci][j+cj];
		}
		cj=0;
	}
	return sb;
}
