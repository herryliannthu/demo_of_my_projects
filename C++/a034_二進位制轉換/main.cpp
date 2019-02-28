#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int a;
    while (cin>>a){
    if (a==1){
        cout <<1<<endl;
    }
    else{
    int t=0 , b = 0;
    while(a>b){
        t++;
        b = pow(2,t)-1;
    }
    t--;
    for (int i=t;i>=0;i--){
        if (a-pow(2,i)>=0){
            cout << 1 ;
            a = a-pow(2,i);
        }
        else{
            cout <<0 ;
        }
    }
    cout << endl;
    }
    }
    return 0;
}
