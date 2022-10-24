#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "List.h"

void appand(List *list,int newData){
    List *newList = malloc(sizeof(List));
    List *endList = list->prev;
    
    if(list->next == NULL){
        newList->prev = NULL;
        newList->data = newData;
        newList->next = NULL;
        list->next = newList;
        endList->prev = newList;
    }else{
        newList->prev = endList->prev;
        newList->data = newData;
        newList->next = NULL;
        endList->prev->next=newList;
        endList->prev = newList;
       
    }
}


void showAll(List *list,bool reverse){
        printf("[ ");
    if(reverse == false){
        List *cur = list->next;
        while (cur != NULL)
        {   
            if (cur->next == NULL){
                printf("%d ", cur->data);
                cur = cur->next;
            }else{
                printf("%d, ", cur->data);
                cur = cur->next;
            }
        }
    }else{
        List *cur = list->prev->prev;
          while (cur != NULL)
        {   
            if (cur->prev == NULL){
                printf("%d ", cur->data);
                cur = cur->prev;
            }else{
                printf("%d, ", cur->data);
                cur = cur->prev;
            }
        }
    }
  
    printf("]\n");
    
}