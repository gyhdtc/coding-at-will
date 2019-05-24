#include <iostream>
using namespace std;

bool iszhishu(long n) {
    long i;
    for (i = 2; i * i <= n; i++) {
        if (n%i == 0) return false;
    }
    return true;
}
int main(){
    long num = 1;
    long endnum;
    cin >> endnum;
    long j;
    for (j = 3; num != endnum; j += 2) 
        if (iszhishu(j)) num ++;
    cout << j-2 << endl;
}