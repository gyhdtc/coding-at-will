#include "uart.h"
#include <iostream>
using namespace std;

void DCB_init(DCB &dcb)
{
	dcb.BaudRate = 9600;
	dcb.ByteSize = 8;
	dcb.Parity = 0;
	dcb.StopBits = 1;
}

BOOL Write(char *write_data, DWORD contentLen,DCB &dcb)
{
	HANDLE hcom;
	char *tmpBuf;
	DWORD dwBytesWrite = 0;
	int dwBytesToWrite;

	hcom = CreateFile("COM9", GENERIC_WRITE | GENERIC_READ, 0, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);

	if (hcom == INVALID_HANDLE_VALUE)
	{
		printf("create file error!\n");
		CloseHandle(hcom);
		return FALSE;
	}
	else
	{
		printf("create file!\n");
	}

	SetupComm(hcom, 1024, 1024);
	GetCommState(hcom, &dcb);
	SetCommState(hcom, &dcb);

	dwBytesToWrite = contentLen;
	dwBytesWrite = 1;

	tmpBuf = write_data;
	
	printf("a");
	do
	{
		printf("%d , %d\n", dwBytesToWrite, dwBytesWrite);
		WriteFile(hcom, tmpBuf, dwBytesToWrite, &dwBytesWrite, NULL);
		dwBytesToWrite -= dwBytesWrite;
		tmpBuf += dwBytesWrite;
	}while (dwBytesToWrite > 0);
	printf("b");
	if (hcom != INVALID_HANDLE_VALUE)
	{
		CloseHandle(hcom);
		hcom = INVALID_HANDLE_VALUE;
	}

	return TRUE;
}

BOOL Read(char *read_data,DCB &dcb)
{
	HANDLE hcom;
	DWORD fileSize;
	char *buffer;
	DWORD dwBytesRead, dwBytesToRead, tmpLen;
	printf("1");
	hcom = CreateFile("COM9", GENERIC_WRITE | GENERIC_READ, 0, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
	printf("2");
	if (hcom == INVALID_HANDLE_VALUE)
	{
		printf("open file error!\n");
		CloseHandle(hcom);
		return FALSE;
	}
	else
	{
		printf("create file!\n");
	}
	printf("3");
	fileSize = GetFileSize(hcom, NULL);
	buffer = (char *)malloc(fileSize);
	ZeroMemory(buffer, fileSize);
	dwBytesToRead = fileSize;
	dwBytesRead = 0;
	read_data = buffer;
	printf("4");
	do
	{
		ReadFile(hcom, read_data, dwBytesToRead, &dwBytesRead, NULL);
		if (dwBytesRead == 0)
			break;
		dwBytesToRead -= dwBytesRead;
		read_data += dwBytesRead;
	}while (dwBytesToRead > 0);
	printf("5");
	
	free(buffer);
	CloseHandle(hcom);

	return TRUE;
}

