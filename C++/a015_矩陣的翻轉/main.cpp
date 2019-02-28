#include <iostream>

using namespace std;

int main()
{
    int col,row;
    while (cin >> row >> col)
    {
        int mat[row][col];
        for (int i=0; i<row; i++)
        {
            for (int n=0; n<col; n++)
            {
                cin >> mat[i][n];
            }

        }
        for (int n=0;n<col;n++)
        {
            for (int i=0;i<row;i++)
            {
                cout << mat[i][n]<<" ";
            }
            cout << endl;
        }
    }

    return 0;
}
