#include <stdio.h>
int main()
{
    unsigned char a = 0x24;
    unsigned char b = 0xFE;
    unsigned char c = a ^ (b >> 2);
    printf("%X\n", c);
    return 0;
}