#include <iostream>
#include <math.h>

using namespace std;

int sqrt_c(int b,int c,int a){
    return sqrt(pow(b,2)-4*a*c);
}
int main()
{
    int a,b,c,x1,x2;
    while(cin>>a){
        cin>>b;
        cin>>c;
        x1 = (-b+sqrt_c(b,c,a))/2/a;
        x2 = (-b-sqrt_c(b,c,a))/2/a;
        if (pow(b,2)-4*a*c < 0){

            cout << "No real root"<<endl;
        }
        else if (x1 != x2){
            cout<< "Two different roots x1=" <<x1<<" , x2="<<x2<< endl;

        }
        else if (x1 == x2){
            cout<< "Two same roots x=" <<x1<< endl;
        }

    }
    return 0;
}
