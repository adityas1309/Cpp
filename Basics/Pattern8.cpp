/* Print this pattern
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
    for(int i=n;i>0;i--) {
        for(int j=1;j<=n-i;j++) {
            cout << " ";
        }
        for(int k=(2*i-1);k>0;k--) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
