#include <iostream>

using namespace std;

int main()
{

    int t,a,b,c,d,f,i;
    int dis1,dis2,dis3;
    cin>>t;
    if (t<=20)
    {
        for (i=0;i<t;i++)
        {
            cin>>a,cin>>b,cin>>c,cin>>d;
            if (b-a == c-b)
            {
                dis1 = c-b;
                f = d+dis1;
                cout<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<f<<endl;

            }
            else if(float(b)/float(a) == float(c)/float(b))
            {
                dis1 = float(b)/float(a) ;
                f = d*dis1;
                cout<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<f<<endl;
            }
        }
    }

return 0;
}
