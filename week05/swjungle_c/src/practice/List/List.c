#include <stdio.h>
#include "List.h"

void Add_First(ListArray *L, int Value)
{
    if (L->length >= 10)
        printf("Can not add Value in List any more.\n");
    else
    {
        L->Array[L->length] = Value;
        L->length +=1;
    };
}

void Add(ListArray *L, int Value, int POSITION)
{
    if (L -> length >= 10)
    {
        printf("더이상 값을 넣을수 없습니다\n");
        return;
    }

    if (L -> length < POSITION)
    {
        Add_Last(L,Value);
        return;
    }
    for (int i = L->length; i> POSITION; i--)
    {
        L->Array[i] = L->Array[i-1];
    }
    L->Array[POSITION] = Value;
    L->length+=1;
}

void Add_Last(ListArray *L, int Value)
{
    if (L->length >= 10)
    {
        printf("더이상 값을 저자할 수 없습니다\n");
        return;
    }
    else
        L->Array[L->length] = Value;
        L->length+=1;
        printf("길이 %d\n",L->length);
        printf("값 %d\n",Value);
}

void Erase(ListArray *L, int POSITION)
{
    if(L->length ==0)
    {
        printf("리스트가 비어있습니다\n");
        return;
    }
    if (POSITION> L->length)
    {
        printf("선택한 위치에 데이터가 없습니다\n");
        return;
    }
    for (int i = POSITION -1; i < L->length -1; i++)
    {
        L->Array[i] = L->Array[i+1];
    }
    L->length -=1;
}

void Array_Clear(ListArray *L)
{
    L->length = 0;
}

void Find_Value(ListArray *L, int VALUE)
{
    for(int i=0; i< L-> length-1;i++)
        if (L->Array[i] == VALUE)
            printf("입력값 %d가 %d 번째 배열에서 발견됐습니다.\n",VALUE,i);
}

int Replace(ListArray *L, int POSITION, int VALUE)
{
    L->Array[POSITION-1] = VALUE;
    return 0;
}

void Return_length(ListArray *L)
{
    printf("리스트의 길이는 %d 입니다\n",L->length);
}

void is_Full(ListArray *L)
{
    if (L->length < 10)
        printf("리스트에 공간이 남아있습니다\n");
    else
        printf("리스트가 가득 찼습니다\n");
}

void is_Empty(ListArray *L)
{
    if(L->length < 10)
        printf("리스트에 공간이 남아 있습니다\n");
    else
        printf("리스트가 가득 찼습니다\n");
}

void Output(ListArray *L)
{
    for(int i=0; i< L ->length; i++)
        printf("%d  ",L->Array[i]);

    printf("\n");
}


