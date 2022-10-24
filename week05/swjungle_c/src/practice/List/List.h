typedef struct ListArray
{
    int Array[10];
    int length;
}ListArray;

void Add_First(ListArray *L, int Value);
void Add(ListArray *L , int Value, int POSITION);
void Add_Last(ListArray *L, int Value);
void Erase(ListArray *L, int POSITION);
void Array_Clear(ListArray *L);
void Find_Value(ListArray *L, int VALUE);
int Replace(ListArray *L, int POSITION, int VALUE);
void Return_length(ListArray *L);
void is_Full(ListArray *L);
void is_Empty(ListArray *L);
void Output(ListArray *L);