#include <stdio.h>

/*
Setting a flag: x |= (1 << n)(turns the nth bit on).
Clearing a flag: x &= ~(1 << n) (turns the nth bit off).
Checking a flag: x & (1 << n) (checks if the nth bit is on).
*/

int count_ones(unsigned int n)
{
    unsigned int count = 0;
    while (n > 0)
    {
        count += n & 1; // Increment count if the last bit is 1
        n >>= 1;        // Right shift n by 1 to check the next bit
    }
    return count;
}

int count_zeros(unsigned int n)
{
    unsigned int count = 0;
    while (n > 0)
    {
        count += !(n & 1); // Increment count if the last bit is 0
        n >>= 1;           // Right shift n by 1 to check the next bit
    }
    return count;
}

int main()
{
    unsigned int n = 0xF0BD; // Example number (1111000010111101 in binary)
    unsigned int result = count_ones(n);
    unsigned int result_zeros = count_zeros(n);
    printf("Number of 1's in %X: %d\n", n, result);
    printf("Number of 0's in %X: %d\n", n, result_zeros);
    return 0;
}