# Makefile
CC = gcc
CFLAGS = -c -g
OBJECTS = List.o list_test.o

run: all
	program

all: program

program : $(OBJECTS)
	$(CC)  $(LDFLAGS) -o program $(OBJECTS)

list_test.o : list_test.c
	$(CC) $(CFLAGS) list_test.c 

List.o : List.c
	$(CC) $(CFLAGS) List.c

clean:
	rm -f *.o\

.PHONY: all bonus clean fclean re
