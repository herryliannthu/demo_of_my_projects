#include <iostream>
#include <math.h>
using namespace std;
int is_prime(int input){
    if (input == 1){
        return 0;
    }
    if (input==2)
        return 1;
    if (input%2==0){
        return 0;
    }
    for (int i=3;i<=sqrt(input);i+=2){
        if (input%i==0){
            return 0;
        }
    }
    return 1;
}
int main()
{
    int a,b,cont;
    while(cin >> a>>b){
        cont = 0;
        for (int i=a;i<=b;i++){
            if (is_prime(i)){
                cont++;
            }
        }
        cout << cont << endl;
    }
    return 0;
}
