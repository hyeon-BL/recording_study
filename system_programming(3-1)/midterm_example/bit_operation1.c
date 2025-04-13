#include <stdio.h>

unsigned int partial_mul(unsigned short a, unsigned short b)
{
    unsigned int a_part = a & 0x3F;
    unsigned int b_part = (b >> 8) & 0x7F;
    printf("a_part: %d\n", a_part);
    printf("b_part: %d\n", b_part);
    return a_part * b_part;
}

int main()
{
    unsigned short a = 0xF0BD;
    unsigned short b = 0xF0BD;
    unsigned int result = partial_mul(a, b);
    printf("Result: %X\n", result);
    printf("Result: %d\n", result);
    return 0;
}