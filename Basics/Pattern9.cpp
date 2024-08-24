/* Print this pattern
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
*/
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cout << "Enter the number:";
    cin >> n;
    for(int i=1;i<=n/2;i++) {
        for(int j=1;j<=(n/2)-i;j++) {
            cout << " ";
        }
        for(int k=1;k<=(2*i-1);k++) {
            cout << "*";
        }
        cout << endl;
    }
    for(int i=(n/2);i>0;i--) {
        for(int j=1;j<=(n/2)-i;j++) {
            cout << " ";
        }
        for(int k=(2*i-1);k>0;k--) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
