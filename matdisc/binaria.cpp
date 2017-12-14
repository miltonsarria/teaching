#include <cstdlib>
#include <iostream>

using namespace std;

int buscarbin(int a[], int i, int n, int x)
{
    int m = (int)((i+n)/2);
    if (a[m]==x) return m;
    else if (x<a[m] & i<m)
    return buscarbin(a,i,m-1,x);
    else if (x>a[m] & n>m)
    return buscarbin(a,m+1,n,x);
    else return -1;
}

int main(int argc, char *argv[])
{

int a[10] = {1,3,4,6,7,8,9,11,55,66};

int result = -1;
int i = 0; // extremo inferior
int n = 10; // limite superior
int x = 0; // numero a buscar

cout << "Que numero busca?\n";
cin>> x;

result = buscarbin(a, i, n, x);

if (result >=0)
{
           cout << "\nElemento ";
           cout << x;
           cout << " encontrado en la posicion ";
           cout << result + 1;
           }
           else
           {
               cout <<"\nNo se encontro el elemento\n";
               }

cin >> x;

}
