#include <iostream>
#include <string>

using namespace std;

int main()
{
    string c ;
    int n = 0,g = 0;
    while(getline(cin,c)){
    for (n = 0;n<c.size();n++){
        c[n] -= 7;
    }
    cout << c << endl;
    }
    return 0;
}
