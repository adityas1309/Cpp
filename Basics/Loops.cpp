#include<bits/stdc++.h>
using namespace std;
int main()
{
    //Loops
    // it will do the updation and checking
    for(int i=1;i<=5;i++) {
        cout << "for count: " << i << endl;
    }
    //it will check the condition and the updation will be inside the loop
    int j=1;
    while(j<=3) {
        cout << "while count: " << j << endl;
        j++;
    }
    //even if the condition doesn't meet the code will get executed 1 time
    int k=4;
    do {
        int c=1;
        cout << "do-while count: " << c << endl;
        c++;k++;
    } while(k<0);
    return 0;
}
