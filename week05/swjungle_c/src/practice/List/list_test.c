#include <stdio.h>
#include "List.h"
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    ListArray * list = (ListArray *)malloc(sizeof(ListArray));
    list->length = 0;
    Add_First(list,1);
    Add_First(list,22222);
    Add(list,3,5);
    Add_Last(list,4);
    Replace(list,1,40440404);
    Output(list);
    // Erase(list,1);
    // Output(list);
    // Erase(list,10);

    // for(int i =0; i< 11; i++){
    //     Add_Last(list,i);
    // }
    // Output(list);
    // Find_Value(list,3);
    // Return_length(list);

    // is_Full(list);

    // Erase(list,3);

    // is_Empty(list);

    // Output(list);
    free(list);
    return 0;
}
