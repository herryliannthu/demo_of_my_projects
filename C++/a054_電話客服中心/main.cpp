#include <bits/stdc++.h>

using namespace std;

int main(){
    int s;
    int op[9];
    int k[26] = {1,10,19,28,37,46,55,54,39,73,82,2,11,20,48,29,38,47,56,65,74,83,21,3,12,30};
    char a[26] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    while(cin>>s){
        int sum=0;
        for(int i = 0;i<9;i++){
            op[i] = s%10;
            s = s/10;
        }
        sum = op[1]*1 + op[2]*2 + op[3]*3 + op[4]*4 + op[5]*5 + op[6]*6 + op[7]*7 + op[8]*8;

        for(int i=0; i<26; i++){
            if( (sum+k[i]+op[0])%10 == 0 ){
                cout << a[i];
            }
        }

        cout << endl;

    }

    return 0;
}

