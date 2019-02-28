#include <iostream>

using namespace std;

int f(int n){
    if (n==1)
        return 1;
    else
        return n+f(n-1);
}

int main()
{
    long long int n,g[30001];
    g[1]=1;
    for(int i=2;i<30001;i++){
    g[i]=g[i-1]+f(i);
        }
    while(cin >> n){
        cout << f(n) <<" " << g[n]<< endl;
    }
    return 0;
}
