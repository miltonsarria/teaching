//Milton Orlando Sarria 
//USC
/*
Calcular la distancia entre dos puntos p1 y p2 en el plano xy
*/

#include <stdio.h>
#include <math.h>

int main() {
	float x1, y1, x2, y2, distancia;
	printf("Ingresar x1: ");
	scanf("%f", &x1);
	printf("Ingresar y1: ");
	scanf("%f", &y1);
	printf("Punto (x1,y1): (%2.2f,%2.2f)\n",x1,y1);
	
    printf("Ingresar x2: ");
	scanf("%f", &x2);
	printf("Ingresar y2: ");	
	scanf("%f", &y2);
	printf("Punto (x2,y2): (%2.2f,%2.2f)\n",x2,y2);
	
	distancia = ((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1));
	
	distancia = sqrt(distancia);
	
	printf("Distancia entre los puntos (x1,y1) y (x2,y2): %2.4f\n", distancia);
	printf("\n");
	return 0;
}
