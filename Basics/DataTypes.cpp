#include<bits/stdc++.h>
using namespace std;
int main()
{
    //Data Types in C++

    int x=10; // -2,147,483,648 to 2,147,483,647
    long r=10000*10000; // -2,147,483,648 to 2,147,483,647
    long long s=10000*100000; // -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
    float y=5.2; // 3.4E +/- 38 (seven digits)
    double z=288.566; // 1.7E +/- 308 (fifteen digits)
    char se = 'G'; //stores a character
    cout << x << " " << y << " "<< z << " " << r << " "<< s << " "<<se;
    cout << "\n" << "Enter a line:";
    string str;
    getline(cin,str); // to take input the whole line use getline
    cout << str;
    string s1,s2;
    cout << "\n"; cin >> s1 >> s2; //if input is 'hi junior'
    cout << s1 << " " << s2; //s1 will only show 'hi' to give output 'junior' we have to use another variable s2
    return 0;
}
