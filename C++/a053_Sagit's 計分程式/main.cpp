#include <iostream>

using namespace std;

int main()
{
    int n;
    while(cin >> n){
        if (n>=40){
            cout << 100 << endl;
        }
        else if (n>=21){
            cout << 60+20+(n-20)*1 << endl;
        }
        else if (n>=11){
            cout << 60+(n-10)*2 << endl;
        }
        else if (n>=0){
            cout << n*6 << endl;
        }
    }
    return 0;
}
