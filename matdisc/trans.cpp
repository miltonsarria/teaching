#include <cstdlib>
#include <iostream>

using namespace std;

int funtran(int x[], int n){
    
    int res = 0;
    int aux = 0;
    
    if(n==0){
             res = x[n];
             }
             else{
                  aux = funtran(x, n-1);
                  }
    if (x[n] > aux){
             res = x[n];
             } else{
                    res = aux;
                    }
                    
    return res;
    }

int funitera(int x[], int n){
    int aux = 0;
    while(n > 0){
      if (x[n] > aux )
            aux = x[n];
       n--;     
            }
    return aux;
    }



int main(int argc, char *argv[])
{
    
    int x[6] = {1, 51, 66, 7, 91, 8};
    
    int result = funtran(x, 5);
    
    cout << "resultado: ";
    cout << result << endl;
       
       
    result = funitera(x, 5);
     cout << "\n\nresultado: ";
    cout << result << endl;  
       
       
    system("PAUSE");
    return EXIT_SUCCESS;
}
