#include <iostream>

using namespace std;

int main()
{
    string s="";
    int a = 1;
    while(cin>>s)
    {
        for (int i=0; i<s.length()/2; i++)
        {
            if (s[i]!=s[s.length()-i-1])
            {
                cout <<"no"<<endl;
                a = 0;
                break;
            }
        }
        if (a == 1)
        {
            cout << "yes"<<endl;
        }
        a = 1;
    }
    return 0;
}
