#include <iostream>
#include <map>
#include <string>
#include <sstream>
using namespace std;
int eng(char c)
{
    map<char,int> engtonum;
    engtonum['A']=1;
    engtonum['B']=10;
    engtonum['C']=19;
    engtonum['D']=28;
    engtonum['E']=37;
    engtonum['F']=46;
    engtonum['G']=55;
    engtonum['H']=64;
    engtonum['I']=39;
    engtonum['J']=73;
    engtonum['K']=82;
    engtonum['L']=2;
    engtonum['M']=11;
    engtonum['N']=20;
    engtonum['O']=48;
    engtonum['P']=29;
    engtonum['Q']=38;
    engtonum['R']=47;
    engtonum['S']=56;
    engtonum['T']=65;
    engtonum['U']=74;
    engtonum['V']=83;
    engtonum['W']=21;
    engtonum['X']=3;
    engtonum['Y']=12;
    engtonum['Z']=30;
    return engtonum[c];
}

int main()
{
    static map<char,int> engtonum;
    string s;
    stringstream ss;
    int temp=0;
    int checker=0,n=0;

    engtonum['A']=1;
    engtonum['B']=10;
    engtonum['C']=19;
    engtonum['D']=28;
    engtonum['E']=37;
    engtonum['F']=46;
    engtonum['G']=55;
    engtonum['H']=64;
    engtonum['I']=39;
    engtonum['J']=73;
    engtonum['K']=82;
    engtonum['L']=2;
    engtonum['M']=11;
    engtonum['N']=20;
    engtonum['O']=48;
    engtonum['P']=29;
    engtonum['Q']=38;
    engtonum['R']=47;
    engtonum['S']=56;
    engtonum['T']=65;
    engtonum['U']=74;
    engtonum['V']=83;
    engtonum['W']=21;
    engtonum['X']=3;
    engtonum['Y']=12;
    engtonum['Z']=30;
    while (cin >> s)
    {
        for (int i=0 ; i<s.length()-1; i++)
        {
            if (i==0)
            {
                checker += eng(s[i]);

            }
            else
            {
                ss << s[i];
                ss >> temp;
                ss.str("");
                ss.clear();
                checker += temp*(8-n);
                n++;
            }
        }
        ss << s[s.length()-1];
        ss >> temp;
        ss.str("");
        ss.clear();
        checker += temp;
        if (checker % 10 ==0)
        {
            cout << "real" << endl;
        }
        else
        {
            cout << "fake"<<endl;
        }
        n=0;
        temp=0;
        checker=0;

    }



    return 0;
}
