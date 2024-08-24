#include<bits/stdc++.h>
using namespace std;
int main()
{
    int x;
    cout << "Enter the input:";
    cin >> x;
    switch(x) {
        case 1:
            cout << "Monday";
            break; //if break is not used rest cases will also be executed
        case 2:
            cout << "Tuesday";
            break;
        case 3:
            cout << "Wednesday";
            break;
        case 4:
            cout << "Thursday";
            break;
        case 5:
            cout << "Friday";
            break;
        case 6:
            cout << "Saturday";
            break;
        case 7:
            cout << "Sunday";
            break;
        default:
            cout <<"Invalid choice"; // if nothing mathes the case this will get executted
    }
    return 0;
}
