# Makefile
CC = gcc
CFLAGS = -c -g
OBJECTS = List.o List_Test.o

run: all
	program

all: program

program : $(OBJECTS)
	$(CC)  $(LDFLAGS) -o program $(OBJECTS)

List_Test.o : List_Test.c
	$(CC) $(CFLAGS) List_Test.c 

List.o : List.c
	$(CC) $(CFLAGS) List.c

clean:
	rm -f *.o\

.PHONY: all bonus clean fclean re
