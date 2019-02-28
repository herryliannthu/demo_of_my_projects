#include <iostream>
#include<math.h>

using namespace std;

int main()
{
    int m,k,c=0,t=0,com=0,i,flag=0;
    while (cin>>m>>k){
        flag=0;
    for (int temp=m; temp<=k; temp++)
    {
        i = temp ;
        while(i-pow(10,c)>=0)
        {
            c++;
        }
        t=c-1;
        while(t>=0)
        {
            com += pow(int(i/pow(10,t)),c);
            i-=int(i/pow(10,t))*pow(10,t);
            t--;
        }
        if (temp == com)
        {
            cout << temp<<" " ;
            flag = 1;
        }
        com =0;
        c=0;
        t=0;
    }
    if (flag==0)
    {
        cout <<"none"<<endl;
    }
    else{
        cout <<endl;
    }
    }
    return 0;
}
