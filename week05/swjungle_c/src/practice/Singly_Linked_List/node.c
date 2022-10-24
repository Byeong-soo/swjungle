#include "node.h"
#include <stdlib.h>
#include <stdio.h>

void appendFirst(Node *list, int newData){
    Node *newNode = malloc(sizeof(Node));
    newNode ->next = list->next;
    newNode ->data = newData;

    list->next = newNode;
}

void append(Node *list,int newData){
    if(list->next == NULL){
        Node *newNode = malloc(sizeof(Node));
        newNode->data = newData;
        newNode->next = NULL;

        list->next = newNode;
    }
    else
    {
        Node *cur = list;
        while (cur->next != NULL)
        {
            cur = cur->next;
        }
        Node * newNode = malloc(sizeof(Node));
        newNode->data = newData;
        newNode->next = NULL;

        cur->next = newNode;
    }
}

void showList(Node *list){
    if(list == NULL){
        printf("리스트가 존재하지 않습니다.");
    }else{
        Node *cur = list->next;
         printf("[ ");
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
        printf("]\n");
    }
}

void deleteList(Node *list){
    Node *cur = list;
    Node *next;
    while(cur != NULL)
    {
        next = cur->next;
        free(cur);
        cur = next;
    }
}

int getNodeLength(Node *list){
    Node *cur = list->next;
    Node *next;
    int count = 0;

    while(cur != NULL)
    {
        count +=1;
        cur = cur->next;
    }
    return count;
}

void insertInList(Node *list,int position,int NewData){
    Node *cur = list;
    int count = 0;

    while (cur != NULL)
    {
         if (count == position){
            Node *newNode = malloc(sizeof(Node));
            newNode ->next = cur->next;
            newNode ->data = NewData;

            cur->next = newNode;
            break;
        }
        cur = cur->next;
        count +=1;
    }

    if(count < position){
        printf("리스트의 크기를 벗어납니다.%d의 위치에 저장됩니다.\n",count);
        append(list,NewData);
    }
    
}

void swapNodeData(Node *node1,Node *node2){
    int temp = node1->data;
    node1->data = node2->data;
    node2->data = temp;
}

Node* createList(){
    Node *newList = malloc(sizeof(Node));
    newList->data = 0;
    newList->next = NULL;
    return newList;
}

bool searchList(Node *list,int number){
    Node *cur = list->next;

    while(cur != NULL){
        if (cur->data == number){
            return true;
        }
        cur = cur->next;
    }
    return false;
}

int pop(Node *list){
    Node *cur = list;
    Node *checkNode = cur->next;

    while (checkNode->next != NULL)
    {
        cur = cur->next;
        checkNode = cur->next;
    }
    int temp = checkNode->data;
    free(checkNode);
    cur->next = NULL;
    return temp;
}

void bubbleSortNode(Node *list){
    int size = getNodeLength(list);
        Node * cur = list->next;
        Node * nextNode;
    for(int i = size -1; i > 0; i--){
        cur = list->next;
        nextNode;
        for(int j = 0; j < i; j ++){
            nextNode = cur->next;
            if(nextNode->data < cur->data){
                swapNodeData(cur,nextNode);
            }
            cur = cur->next;
        }
    }
}

void showListMemory(Node *list){
    Node * cur = list->next;
    int size = getNodeLength(list);

    for(int i = 0; i < size; i++){
        printf("=================%d 번째 ====================\n",i);
        printf("cur     :%p\n",cur);
        printf("cur-next:%p\n",cur->next);
        printf("cur-data:%d\n",cur->data);
        cur = cur->next;
    }
}

void arryToList(Node *list,int array[],int size){

    for(int i = 0; i < size; i ++){
        append(list,array[i]);
    }

}