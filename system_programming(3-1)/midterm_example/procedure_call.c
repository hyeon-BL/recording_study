#include <stdio.h>
int increment()
{
    static int c = 0;
    return ++c;
}
int sum(int *px)
{
    int y = increment();
    char higher_var;
    if (px > &y)
        higher_var = 'x';
    else
        higher_var = 'y';
    // (Problem 3-2)
    printf("%c has the higher memory "
           "address\n",
           higher_var);
    return *px + y;
}

int main()
{
    // Ⓐ (Problem 3-3)
    int i, x = 0;
    for (i = 0; i < 3; i++)
        x = sum(&x);
    // (Problem 3-1)
    printf("SUM = %d\n", x);
    // Ⓑ (Problem 3-3)
    return 0;
}