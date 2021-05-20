#include <iostream>
#include <mutex>
using namespace std;

class A {
public:
    int32_t totalnode = 0x00bfffff;
    mutex x;
};

int8_t GetNodeNumber(A* a) {
    int8_t res = 1;
    int32_t t = 0x00000001;
    lock_guard<mutex> guard(a->x, adopt_lock);
    while ((res <= 32) && ((a->totalnode >> (res++) & t) != 0x00000000));
    return res & 0x3f;
}

int main() {
    A* ptra = new A;
    int8_t b = GetNodeNumber(ptra);
}