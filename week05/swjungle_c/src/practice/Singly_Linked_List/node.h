#ifndef _NODE_H_
#define _NODE_H_


#include <stdbool.h>

typedef struct Node
{
    struct Node *next;
    int data;
}Node;

void appendFirst(Node *ptr, int newData);
void append(Node *ptr,int newData);
void showList(Node *ptr);
void deleteList(Node *ptr);
int getNodeLength(Node *ptr);
void insertInList(Node *ptr,int position,int NewData);
void swapNodeData(Node *node1,Node *node2);
void bubbleSortNode(Node *ptr);
void showListMemory(Node *ptr);
void arryToList(Node *ptr,int array[],int size);
bool searchList(Node *ptr,int number);
Node* getList();
int pop(Node *list);
// void generateLottoList(Node *list);

#endif