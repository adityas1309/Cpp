#include<bits/stdc++.h>
using namespace std;
int main()
{
    int x;
    cout << "Enter the input:";
    cin >> x;
    if(x>0) {// Checks first if True will not check rest blocks
        cout << "Positive";
    }
    else if(x<0) {// if 1st block fails then it will check otherwise not
        cout << "Negative";
    }
    else if (x==0) {// if 1st and 2nd block fails then it will check otherwise not
        cout << "Zero";
    }
    else {// if everything fails this will get executed
        cout << "Invalid";
    }
    return 0;
}
