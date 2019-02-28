#include <iostream>
#include <math.h>
#define pass (void)0

using namespace std;

int main()
{
    int t,a,b,sum;
    while(cin >> t){
        for (int i=1;i<=t;i++){
        cin >> a >> b;
        sum=0;
        for (int i=a;i<=b;i++){
            if (i==2||i==3)
            {
                pass;
            }
            else{
            if (pow(int((sqrt(i))),2)==i){
                sum+=i;
            }
            }
        }
        cout << "Case "<<i<<": "<<sum<<endl;
        }
    }
    return 0;
}
