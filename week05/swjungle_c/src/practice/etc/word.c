#include <stdio.h>

void main(int argc, char const *argv[])
{
    // char *s = "Hello, "
    // "word!";

    // printf("%s",s);

    // return 0;

    char *s = "ddbbcc";


    printf("%s\n",s);
    s++;
    printf("%s\n",s);

    printf("%d\n",*s);


    char c1 = 'b';
    char c2 = 'c';

    c1++;
    c2--;

    printf("c1의 변경된 값은 %c\n",c1);
    printf("c2의 변경된 값은 %c\n",c2);
}
