# Makefile
CC = gcc
CFLAGS = -c -g
OBJECTS = node.o test_node.o

run: all
	program

all: program

program : $(OBJECTS)
	$(CC)  $(LDFLAGS) -o program $(OBJECTS)

test_node.o : test_node.c
	$(CC) $(CFLAGS) test_node.c 

node.o : node.c
	$(CC) $(CFLAGS) node.c

clean:
	rm -f *.o\

.PHONY: all bonus clean fclean re
