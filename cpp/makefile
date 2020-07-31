CC = g++
CFLAGS = -c -Wall
LFLAGS = -Wall
#include_directories("/home/gyh/cpp/include")
all: main
main: main.o string.o
	$(CC) $(LFLAGS) main.o string.o -o main
main.o: main.cpp
	$(CC) $(CFLAGS) main.cpp
string.o: string.cpp
	$(CC) $(CFLAGS) string.cpp

clean:
	rm -rf *.o main