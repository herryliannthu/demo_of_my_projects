#include <iostream>
#define pass (void)0

using namespace std;

int main()
{
    int a,sum,t;
    while (cin >> t){
        while (t--){
        cin >> a;
        sum=1;
        while (a/10!=0){
            sum*=a%10;
            a/=10;
        }
        cout << sum*a << endl;
        }
    }

    return 0;
}
