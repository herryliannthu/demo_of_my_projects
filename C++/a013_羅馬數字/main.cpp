#include <iostream>
#include <string>
#include <map>
using namespace std;

void NumToRoma(int sum)
{
    while(sum>0)
    {
        if(sum>=1000)
        {
            cout << "M";
            sum-=1000;
        }
        else if(sum>=900)
        {
            cout <<"CM";
            sum-=900;
        }
        else if(sum>=500)
        {
            cout <<"D";
            sum-=500;
        }
        else if(sum>=400)
        {
            cout <<"CD";
            sum-=400;
        }
        else if(sum>=100)
        {
            cout <<"C";
            sum-=100;
        }
        else if(sum>=90)
        {
            cout <<"XC";
            sum-=90;
        }
        else if(sum>=50)
        {
            cout <<"L";
            sum-=50;
        }
        else if(sum>=40)
        {
            cout <<"XL";
            sum-=40;
        }
        else if(sum>=10)
        {
            cout <<"X";
            sum-=10;
        }
        else if(sum>=9)
        {
            cout <<"IX";
            sum-=9;
        }
        else if(sum>=5)
        {
            cout <<"V";
            sum-=5;
        }
        else if(sum>=4)
        {
            cout <<"IV";
            sum-=4;
        }
        else if(sum>=1)
        {
            cout <<"I";
            sum-=1;
        }
    }
    cout << endl;
}


int main()
{
    string s1,s2;
    map <char,int> roma;
    roma['I'] = 1;
    roma['V'] = 5;
    roma['X'] = 10;
    roma['L'] = 50;
    roma['C'] = 100;
    roma['D'] = 500;
    roma['M'] = 1000;
    while (cin>>s1)
    {
        int num1=0,num2=0;
        if (s1 == "#")
        {
            break;
        }
        cin>>s2;
        if (s1 == s2)
        {
            cout << "ZERO" << endl;
        }
        for (int n = 0 ; n<s1.size(); n++)
        {
            if (roma[s1[n]]<roma[s1[n+1]])
            {
                num1 += roma[s1[n+1]] - roma[s1[n]];
                n++;
            }

            else
            {
                num1 += roma[s1[n]];
            }
        }
        for (int n = 0 ; n<s2.size(); n++)
        {
            if (roma[s2[n]]<roma[s2[n+1]])
            {
                num2 += roma[s2[n+1]] - roma[s2[n]];
                n++;
            }
            else
            {
                num2 += roma[s2[n]];
            }
        }
        NumToRoma(abs(num1-num2));
    }




    return 0;
}
