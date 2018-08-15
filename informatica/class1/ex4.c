///Milton Orlando Sarria 
//USC
/*
Dados los datos de ancho y alto de un rectangulo
calcular el area y el perimetro
*/

#include <stdio.h> 
/* altura y ancho del rectangulo en cm */
int ancho;          
int alto;         

int area;           
int perimetro;      

int main() 
{
	alto = 7;
	ancho = 5;

    perimetro = 2*(alto + ancho);
	printf("Perimetro del rectangulo = %d cm\n", perimetro);
	
	area = ancho * alto;
	printf("Area del rectangulo = %d cm cuadrados \n", area);

return(0);
}
