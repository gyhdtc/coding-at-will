# ifndef __uart_
#define __uart_

#include<windows.h>

#define RtlZeroMemory(Destination,Length) memset((Destination),0,(Length))
#define ZeroMemory RtlZeroMemory

BOOL Write(char *write_data, DWORD contentLen, DCB &dcb);
BOOL Read(char *read_data, DCB &dcb);
void DCB_init(DCB &dcb);

#endif // !__uart_
