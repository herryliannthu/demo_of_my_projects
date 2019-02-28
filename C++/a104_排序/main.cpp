#include <iostream>

using namespace std;

int main()
{
    int n;
    while (cin >> n){
            int input[n];
            for (int i=0;i<n;i++){
                cin >> input[i];
            }
            int len = n;
            for (int i=0;i<len-1;i++){
                for (int j=0;j<len-1-i;j++){
                    if (input[j]>input[j+1])
                        swap(input[j],input[j+1]);
                }
                }
          for (int i=0;i<n;i++)
              cout <<input[i] <<" ";

          cout <<endl ;
    }


    return 0;
}
