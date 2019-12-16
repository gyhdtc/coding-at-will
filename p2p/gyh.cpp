#include <iostream>
using namespace std;

int main(){
    int n, m;
    int t = 0, k, p;
    int temp, tempmax = 0;
    p = -1;
    cin >> n >> m;
    
    for(int i = 0; i < n; i++) {
        cin >> temp;
        t += temp;
        tempmax = 0;
        for(int j = 0; j < m; j++) {
            cin >> temp;
            t += temp;
            tempmax += temp;
        }
        
        if (-tempmax > p) {
            p = -tempmax;
            k = i + 1;
        }
    }

    printf("%d %d %d", t, k, p);
    return 0;
}