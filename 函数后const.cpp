#include <iostream>
using namespace std;
class Person
{
private:
    static const int LIMIT = 25;
    string lname;
    char fname[LIMIT];
public:
    Person(){ lname = ""; fname[0] = '/0';}
    Person(const string &ln, const char * fn = "heyyou");
    void show() const;
    void Formashow() const; 
    // 也就是说，这些函数是"只读"函数，而有一些函数要修改类数据成员的值。
    // 如果把不改变数据成员的函数都加上const关键字进行标识，显然，可提高程序的可读性。
    // 其实，它还能提高程序的可靠性，已定义成const的成员函数，一旦企图修改数据成员的值，则编译器按错误处理。
};

int main(){
    Person one;
    Person two("gyh");
    Person three("gyh", "gyh");
    one.show();
    one.Formashow();
}