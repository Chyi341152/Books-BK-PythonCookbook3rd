# A Simple Makefile Tutorial
# http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/
main: main.c library.c
	clang -o main main.c library.c -lm

so: library.c
	clang -c -Wall -Werror -fpic library.c 
	clang -shared -o library.so library.o
