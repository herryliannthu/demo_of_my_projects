#include <iostream>

using namespace std;

int main()
{
    int a ,b ,n;
    int flag = 1;
    while(cin>>a>>b){
        if (a>=b){
            for (n=a;n>0;n--){
                if (a%n ==0 && b%n==0){
                    cout << n << endl;
                    break;
                }
            }
        }
        else if (a<b){
            for (n=b;n>0;n--){
                if (a%n ==0 && b%n==0){
                    cout << n << endl;
                    break;
                }
            }
        }

    }
    return 0;
}
