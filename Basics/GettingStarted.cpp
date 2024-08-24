//#include <iostream> //includes the library to take input and give output
#include<bits/stdc++.h> //includes all the library in c++ to avoid many lines of #include
using namespace std;
int main()
{
    std::cout << "Hello,World!" ; //for every cout & cin we have to use std:: to avoid this we will use namespace
    cout << "New World!!" << "\n"; // '\n' adds a new line
    cout << "New line" << endl; //endl is also used for adding a new line
    int x;
    cout << "Enter a number:";cin >> x;
    cout << x*x;
    return 0;
}
