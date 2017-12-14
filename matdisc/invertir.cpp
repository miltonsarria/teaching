#include <cstdlib>
#include <iostream>

using namespace std;

string invertir(string numero, int i)
{
       if (!numero[i+1]){
            return numero[i];            
                       }
       numeroinv += (numero, i + 1);
       return numeroinv
       
       }


int main(int argc, char *argv[])
{
    string numero;
    cin >> numero;
    cout << "\n" << invertir(numero, 0);
    system("PAUSE");
    return EXIT_SUCCESS;
}
