#include <iostream>
#include <vector>
#include <list>
#include <ctime>
#include <iomanip>
using namespace std;
#define SideLength 10
#define r_random(x) (rand() % x)

int main(){
    // reset send
    srand((unsigned)time(NULL));
    cout << r_random(100);
    cout << r_random(99);
    cout << r_random(99);
    cout << r_random(90);
    return 0;
}