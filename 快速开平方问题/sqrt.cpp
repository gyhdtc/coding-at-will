#include <iostream>
#include <cmath>
#include <time.h>
using namespace std;

float Q_rsqrt( float number )
{
	long i;
	float x2, y;
	const float threehalfs = 1.5F;
    
	x2 = number * 0.5F;
	y   = number;
	i   = * ( long * ) & y;   // evil floating point bit level hacking
	i   = 0x5f3759df - ( i >> 1 ); // what the fuck?
	y   = * ( float * ) & i;
	y   = y * ( threehalfs - ( x2 * y * y ) ); // 1st iteration
 	// 2nd iteration, this can be removed
	// y   = y * ( threehalfs - ( x2 * y * y ) );

	#ifndef Q3_VM
	#ifdef __linux__
		 assert( !isnan(y) ); // bk010122 - FPE?
	#endif
	#endif
	return y;
}

int main(){
    float x = 1325.97;
    float y1, y2;
    clock_t startTime, endTime1, endTime2;
    long int k = 100000000;

    startTime = clock();
    for (long int i = 0; i < k; i ++)
        y2 = 1.0f / sqrt(x);
    endTime1 = clock();
    for (long int i = 0; i < k; i ++)
        y1 = Q_rsqrt(x);
    endTime2 = clock();

    cout << y1 << " --- ";
    cout << (endTime1 - startTime) << endl;

    cout << y2 << " --- ";
    cout << (endTime2 - endTime1) << endl;
    return 0;
}