#include <iostream>

using namespace std;

int main()
{
    int n,sum,a;
    while(cin >> n){
        sum = 0;
        for (int i=0;i<n;i++){
            cin >> a;
            sum+=a;
        }
        if (float(sum)/float(n) > 59){
            cout << "no"<<endl;
        }
        else
            cout << "yes" << endl;
    }
    return 0;
}
