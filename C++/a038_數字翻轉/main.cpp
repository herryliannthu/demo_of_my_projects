#include <iostream>

using namespace std;

int main()
{
    string a ;
    while (cin >> a)
    {
        int c=0;
        while(a[c]=='0')
        {
            c++;
        }
        if (c == a.length())
        {
            cout << 0<<endl;
        }
        else
        {
            a.erase(0,c);
            c = a.length()-1;
            if (a[c]=='0')
            {
                while(a[c]=='0')
                {
                    c--;
                }
                a.erase(c+1,a.length());

            }
            for (int i = a.length()-1; i>=0; i--)
            {
                cout << a[i];
            }
            cout << endl;
        }
    }
    return 0;
}
