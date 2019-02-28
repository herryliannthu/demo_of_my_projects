#include <iostream>

using namespace std;

int main()
{
    int n;
    while (cin >> n){
    int a ,j=0,k=0,l=0;
    for (int i=0;i<n;i++)
    {
    cin >> a;
        if (a%3==0){
            j++;
        }
        else if (a%3==1){
            k++;
        }
        else if (a%3==2){
            l++;
        }
    }
    cout << j << " " << k << " " << l <<endl;
    j=0;k=0;l=0;

    }
    return 0;
}
