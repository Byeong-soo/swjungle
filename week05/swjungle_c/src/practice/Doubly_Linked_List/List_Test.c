#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "List.h"

int main(int argc, char const *argv[])
{
    List *list = malloc(sizeof(List));
    List *endList = malloc(sizeof(List));
    list->next = NULL;
    list->prev = endList;

    endList->next = list;
    endList->prev = NULL;

    for(int i = 0; i<10; i++){
        appand(list,i);
    }

    showAll(list,true);
    showAll(list,false);
    return 0;
}
