#include <stdio.h>
extern long a;
void foo();
int main()
{
    a = 4;
    foo();
    return 0;
}

/*
file2.c
#include <stdio.h>
int a = 1;
int b = 2;
void foo()
{
    printf("a: %d, b: %d\n", a, b);
}

// This code defines a global variable 'a' in file1.c and uses it in the function foo() defined in file2.c.
// The function foo() prints the values of 'a' and 'b', where 'b' is defined in file2.c.
// The main function in file1.c sets 'a' to 4 and then calls foo(), which will print the values of 'a' and 'b'.

// The output will be:
// a: 4, b: 0
long a -> int a = 4 & overwriting the value of 'b' in file2.c
*/