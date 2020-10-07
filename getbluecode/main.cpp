#include "uart.h"
#include <iostream>
using namespace std;

int main(){
	int a;
	DCB mybt;
	char *read_blue;
	char *write_blue;
	DCB_init(mybt);
	write_blue = "111111111111111111111111111111111111111111111111111111111111111111111";
	
	Write(write_blue, 1, mybt);
	Read(read_blue, mybt);
	cout << read_blue;
	cin >> a;
	return 1;
}

