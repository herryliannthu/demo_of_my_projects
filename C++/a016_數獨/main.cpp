#include <iostream>

using namespace std;
static int n1=0,n2=0,n3=0,n4=0,n5=0,n6=0,n7=0,n8=0,n9=0;
static int mat[9][9];
void re_counter(int i)
{

    if (i == 1)
    {
        n1++;
    }
    if (i == 2)
    {
        n2++;
    }
    if (i == 3)
    {
        n3++;
    }
    if (i == 4)
    {
        n4++;
    }
    if (i == 5)
    {
        n5++;
    }
    if (i == 6)
    {
        n6++;
    }
    if (i == 7)
    {
        n7++;
    }
    if (i== 8)
    {
        n8++;
    }
    if (i == 9)
    {
        n9++;
    }

}
void Zero()
{
    n1=0;
    n2=0;
    n3=0;
    n4=0;
    n5=0;
    n6=0;
    n7=0;
    n8=0;
    n9=0;
}
string check(){
    int i=0,n=0;
    for (i=0; i<9; i++)  //恆線是否違規
        {
            for (n=0; n<9; n++)
            {
                re_counter(mat[i][n]);

            }
            if (n1>1 || n2>1 || n3>1 || n4>1 || n5>1 || n6>1 || n7>1 || n8>1 || n9>1)
            {
                return "no";
                break;
            }
            Zero();
        }
        for (n=0; n<9; n++)  //質線是否違規
        {
            for (i=0; i<9; i++)
            {
                re_counter(mat[i][n]);
            }
            if (n1>1 || n2>1 || n3>1 || n4>1 || n5>1 || n6>1 || n7>1 || n8>1 || n9>1)
            {
                return "no";
                break;
            }
            Zero();
        }
        for (i=0; i<3; i++)
        {
            for (n=0; n<3; n++)
            {
                re_counter(mat[i][n]);
            }
        }
        if (n1>1 || n2>1 || n3>1 || n4>1 || n5>1 || n6>1 || n7>1 || n8>1 || n9>1)
        {
            return "no";
        }
        Zero();
        for (i=0; i<3; i++)
        {
            for (n=3; n<6; n++)
            {
                re_counter(mat[i][n]);
            }
        }
        if (n1>1 || n2>1 || n3>1 || n4>1 || n5>1 || n6>1 || n7>1 || n8>1 || n9>1)
        {
            return "no";
        }
        Zero();
        for (i=0; i<3; i++)
        {
            for (n=6; n<9; n++)
            {
                re_counter(mat[i][n]);
            }
        }
        if (n1>1 || n2>1 || n3>1 || n4>1 || n5>1 || n6>1 || n7>1 || n8>1 || n9>1)
        {
            return "no";
        }
        Zero();


        for (i=3; i<6; i++)
        {
            for (n=0; n<3; n++)
            {
                re_counter(mat[i][n]);
            }
        }
        if (n1>1 || n2>1 || n3>1 || n4>1 || n5>1 || n6>1 || n7>1 || n8>1 || n9>1)
        {
            return "no";
        }
        Zero();
        for (i=3; i<6; i++)
        {
            for (n=3; n<6; n++)
            {
                re_counter(mat[i][n]);
            }
        }
        if (n1>1 || n2>1 || n3>1 || n4>1 || n5>1 || n6>1 || n7>1 || n8>1 || n9>1)
        {
            return "no";
        }
        Zero();
        for (i=3; i<6; i++)
        {
            for (n=6; n<9; n++)
            {
                re_counter(mat[i][n]);
            }

        }
        if (n1>1 || n2>1 || n3>1 || n4>1 || n5>1 || n6>1 || n7>1 || n8>1 || n9>1)
        {
            return "no";
        }
        Zero();
        for (i=6; i<9; i++)
        {
            for (n=0; n<3; n++)
            {
                {
                    re_counter(mat[i][n]);
                }

            }
        }
        if (n1>1 || n2>1 || n3>1 || n4>1 || n5>1 || n6>1 || n7>1 || n8>1 || n9>1)
        {
            return "no";
        }
        Zero();
        for (i=6; i<9; i++)
        {
            for (n=3; n<6; n++)
            {
                re_counter(mat[i][n]);
            }


        }
        if (n1>1 || n2>1 || n3>1 || n4>1 || n5>1 || n6>1 || n7>1 || n8>1 || n9>1)
        {
            return "no";
        }
        Zero();

        for (i=6; i<9; i++)
        {
            for (n=6; n<9; n++)
            {
                re_counter(mat[i][n]);

            }

        }
        if (n1>1 || n2>1 || n3>1 || n4>1 || n5>1 || n6>1 || n7>1 || n8>1 || n9>1)
        {
            return "no";
        }
        Zero();
        return "yes";


}

int main()
{
    int i=0,n=0;
    while (cin>>mat[0][0]>>mat[0][1]>>mat[0][2]>>mat[0][3]>>mat[0][4]>>mat[0][5]>>mat[0][6]>>mat[0][7]>>mat[0][8])
    {
        for (i=1; i<9; i++)
        {
            for (n=0; n<9; n++)
            {
                cin >> mat[i][n];
            }
        }
        Zero();
        cout << check() << endl;

    }


    return 0;
}
