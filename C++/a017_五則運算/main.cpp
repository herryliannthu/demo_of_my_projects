#include <iostream>
#include <string>
#include <sstream>

using namespace std;
int re(string s)
{
    int result = 0;
    string sss="" ;
    string temp = "";
    stringstream ss;
    int num = 0,temp1 =0,temp2 =0;
    int t;
    if (s.find("(",0)<5000)
    {
        sss = sss.assign(s,s.find("(",0)+1,s.find("(",0) - s.find(")",0));
        result = re(sss);
    }
    else if (s.find("*",0)<5000||s.find("/",0)<5000||s.find("%",0)<5000)  //§ïs¤ºªº*/%
    {
        for (int i=0; i<s.length(); i++)
        {
            if (s[i] == '*')
            {
                ss << s[i-1];
                ss >> temp1;
                ss.str("");
                ss.clear();
                ss << s[i+1];
                ss >> temp2;
                ss.str("");
                ss.clear();
                ss << temp1*temp2;
                ss >> temp;
                ss.str("");
                ss.clear();
                s.erase(i-1,3);
                s.insert(i-1,temp);
                temp = "";
            }
            else if (s[i] == '/')
            {
                ss << s[i-1];
                ss >> temp1;
                ss.str("");
                ss.clear();
                ss << s[i+1];
                ss >> temp2;
                ss.str("");
                ss.clear();
                ss << temp1/temp2;
                ss >> temp;
                ss.str("");
                ss.clear();
                s.erase(i-1,3);
                s.insert(i-1,temp);
                temp = "";
            }
            else if (s[i] == '%')
            {
                ss << s[i-1];
                ss >> temp1;
                ss.str("");
                ss.clear();
                ss << s[i+1];
                ss >> temp2;
                ss.str("");
                ss.clear();
                ss << temp1%temp2;
                ss >> temp;
                ss.str("");
                ss.clear();
                s.erase(i-1,3);
                s.insert(i-1,temp);
                temp = "";
            }
        }
    }
    for (int i=0; i<s.length(); i++)
        {
            if (s[i]=='+'){
                ss << s[i-1];
                ss >> temp1;
                ss.str("");
                ss.clear();
                ss << s[i+1];
                ss >> temp2;
                ss.str("");
                ss.clear();
                //ss << temp1+temp2;
                result += temp1+temp2;
                /*ss >> temp;
                ss.str("");
                ss.clear();
                s.erase(i-1,3);
                s.insert(i-1,temp);
                temp = "";*/
            }
            if (s[i]=='-'){
                ss << s[i-1];
                ss >> temp1;
                ss.str("");
                ss.clear();
                ss << s[i+1];
                ss >> temp2;
                ss.str("");
                ss.clear();
                //ss << temp1+temp2;
                result += temp1-temp2;
                /*ss >> temp;
                ss.str("");
                ss.clear();
                s.erase(i-1,3);
                s.insert(i-1,temp);
                temp = "";*/
            }

        }
        return result ;

}
int main()
{
    string s = "2+3*4";
    string sss="" ;
    string temp = "";
    stringstream ss;
    int num = 0,temp1 =0,temp2 =0;
    int t;
    cout << re(s) << endl;

    /* if (s.find("(",0)<5000)
     {
         sss = sss.assign(s,s.find("(",0)+1,s.find("(",0) - s.find(")",0));
         sss.erase(sss.find(")",0),1);
         if (sss.find("*",0)<5000)
         {
             ss << sss[sss.find("*",0)-1];
             ss >> temp1;
             ss.str("");
             ss.clear();
             ss << sss[sss.find("*",0)+1];
             ss >> temp2;
             ss.str("");
             ss.clear();
             ss << temp1*temp2;
             ss >> temp;
             ss.str("");
             ss.clear();
             sss.insert(sss.find("*",0)-1,temp);
             sss.erase(sss.find("*",0)-1,3);
             temp = "";
         }
         if (sss.find("/",0)<5000)
         {
             ss << sss[sss.find("/",0)-1];
             ss >> temp1;
             ss.str("");
             ss.clear();
             ss << sss[sss.find("/",0)+1];
             ss >> temp2;
             ss.str("");
             ss.clear();
             ss << temp1/temp2;
             ss >> temp;
             ss.str("");
             ss.clear();
             s.insert(sss.find("/",0)-1,temp);
             s.erase(sss.find("/",0)-1,3);
             temp = "";
         }
         if (sss.find("%",0)<5000)
         {
             ss << sss[sss.find("%",0)-1];
             ss >> temp1;
             ss.str("");
             ss.clear();
             ss << sss[sss.find("%",0)+1];
             ss >> temp2;
             ss.str("");
             ss.clear();
             ss << temp1%temp2;
             ss >> temp;
             ss.str("");
             ss.clear();
             s.insert(sss.find("%",0)-1,temp);
             s.erase(sss.find("%",0)-1,3);
             temp = "";
         }
         s.insert(s.find("(",0),sss);
         s.erase(s.find("(",0),s.find("(",0)-s.find(")",0));

     }

     if (s.find("*",0)<5000)
     {
         if (s[i] == '*'){
             ss << s[i-1];
             ss >> temp1;
             ss.str("");
             ss.clear();
             ss << s[i+1];
             ss >> temp2;
             ss.str("");
             ss.clear();
             ss << temp1*temp2;
             ss >> temp;
             ss.str("");
             ss.clear();
             sss.erase(i-1,3);
             sss.insert(i-1,temp);
             temp = "";
     }
     if (s.find("/",0)<5000)
     {
         ss << s[s.find("/",0)-1];
         ss >> temp1;
         ss.str("");
         ss.clear();
         ss << s[s.find("/",0)+1];
         ss >> temp2;
         ss.str("");
         ss.clear();
         ss << temp1/temp2;
         ss >> temp;
         ss.str("");
         ss.clear();
         s.insert(s.find("/",0)-1,temp);
         s.erase(s.find("/",0)-1,3);
         temp = "";
     }
     if (s.find("%",0)<5000)
     {
         ss << s[s.find("%",0)-1];
         ss >> temp1;
         ss.str("");
         ss.clear();
         ss << s[s.find("%",0)+1];
         ss >> temp2;
         ss.str("");
         ss.clear();
         ss << temp1%temp2;
         ss >> temp;
         ss.str("");
         ss.clear();
         s.insert(s.find("%",0)-1,temp);
         s.erase(s.find("%",0)-1,3);
         temp = "";
     }
    */

    cout << s << endl;
    cout << num << endl;


    return 0;
}

