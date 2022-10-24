#include <stdio.h>
#include "node.h"
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    Node *list = (Node*)malloc(sizeof(Node));
    list->next= NULL;

    appendFirst(list,1);

    for(int i=11;i>0;i--){
        append(list,i);
    }

    showList(list);
    printf("%d\n",getNodeLength(list));
    appendFirst(list,999999);
    showList(list);

    insertInList(list,0,20);
    showList(list);
    insertInList(list,200,10);
    showList(list);
    printf("%d\n",getNodeLength(list));

    if(searchList(list,125125)){
        printf("125125는 리스트에 포함되어 있습니다.\n");
    }else{
        printf("125125는 리스트에 없습니다.\n");
        
    }

    if(searchList(list,10)){
        printf("10은 리스트에 포함되어 있습니다.\n");
    }else{
        printf("10은 리스트에 없습니다.\n");
    }

    printf("%d\n",pop(list));
    showList(list);

    bubbleSortNode(list);
    showList(list);
    showListMemory(list);
    
    int abc[5];
    for(int i =0; i<5;i++){
        abc[i] = i;
    }

    arryToList(list,abc,5);
    showList(list);
    
    deleteList(list);

    return 0;
}
