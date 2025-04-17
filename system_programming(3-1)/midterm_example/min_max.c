#include <stdio.h>

int main()
{
    int i_max = 0x7FFFFFFF; // 2147483647 in decimal
    int i_min = 0x80000000; // -2147483648 in decimal
    printf("i_max: %d\n", i_max);
    printf("i_min: %d\n", i_min);

    int i_max2 = (1 << 31) - 1; // 2147483647 in decimal
    printf("i_max2: %d\n", i_max2);

    int i_max3 = 0b01111111111111111111111111111111; // 2147483647 in decimal
    printf("i_max3: %d\n", i_max3);

    unsigned int u_max = 0xFFFFFFFF; // 4294967295 in decimal
    printf("u_max: %u\n", u_max);    // %u for unsigned int
    printf("u_max: %d\n", u_max);    // %d for signed int
    printf("u_max: %x\n", u_max);    // %x for hexadecimal
}