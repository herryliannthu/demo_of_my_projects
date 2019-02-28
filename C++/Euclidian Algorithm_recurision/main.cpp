#include <iostream>

using namespace std;
// demonstrate how to implement Euclidian Algorithm using recursion function.
int gcd(int a, int b){
    int r=0;
    if (a%b!=0){
        cout << a <<" = " << b << " * " << a/b << " + " << a%b <<endl;
        gcd(b,a%b);
    }
    else{
        cout << "The answer is "<< b <<endl;
    }


}
int main()
{
    gcd(3768,1701);
    return 0;
}
