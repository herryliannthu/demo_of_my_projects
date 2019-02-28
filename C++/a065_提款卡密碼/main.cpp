#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    string input;
    while (cin >> input){
        for (int i=0;i<input.size()-1;i++){
            cout << abs(int(input[i+1]) - int(input[i]));
        }
        cout << endl;
    }

    return 0;
}
