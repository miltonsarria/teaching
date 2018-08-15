//Milton Orlando Sarria 
//USC
/*
Convertir una entrada que esta dada en segundos a un formato
especifico: H,M,S
*/

#include <stdio.h>
int main() 
{
	int sec, h, m, s;
	printf("Entrada en segundos: ");
	scanf("%d", &sec);
	
	h = (sec/3600); 
	
	m = (sec -(3600*h))/60;
	
	s = (sec -(3600*h)-(m*60));
	
	printf("H:M:S - %d:%d:%d\n",h,m,s);
	
	return 0;
}
