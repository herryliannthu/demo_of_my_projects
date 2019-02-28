#include <iostream>

using namespace std;

int main()
{
    int n,m,v,num,sum,cheat=1;
    while(cin >> n >> m){
        num=1;
            for (int i=0;(i+n)<=m;i++){
                m-=(i+n);
                num++;
            }
            cout << num<<endl;



    }
    return 0;
}
