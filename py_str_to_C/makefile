all: main
	
main: string ./main.cpp
	g++ -Wall -o prog string.o ./main.cpp
string: C_string_like_python.cpp
	g++ -Wall -c -o string.o C_string_like_python.cpp
