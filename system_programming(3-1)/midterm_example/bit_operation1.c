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
    unsigned short c = 0b1111000010111101;
    unsigned short d = 0b1111000010111101;
    unsigned int result_hex = partial_mul(a, b);
    unsigned int result_bin = partial_mul(c, d);
    printf("Result: %X\n", result_bin);
    printf("Result: %d\n", result_bin);

    printf("Result: %X\n", result_hex);
    printf("Result: %d\n", result_hex);
    return 0;
}