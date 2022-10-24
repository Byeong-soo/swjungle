#include <stdbool.h>

typedef struct List
{
    struct List *prev;
    int data;
    struct List *next;
}List;



void appand(List *ptr,int newData);
void showAll(List *ptr,bool reverse);

