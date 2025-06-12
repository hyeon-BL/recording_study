#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
int main()
{
    int fd1, fd2, fd3, fd4, fd5;
    char c[3];
    fd1 = open("hello.txt", O_RDONLY);
    fd2 = open("hello.txt", O_RDONLY);
    fd3 = open("hello.txt", O_RDONLY);
    fd4 = open("hello.txt", O_RDONLY);
    fd5 = open("hello.txt", O_RDONLY);
    dup2(fd1, fd2);
    dup2(fd4, fd5);
    dup2(fd3, fd4);
    read(fd1, &c, 3);
    printf("%s\n", c);
    read(fd2, &c, 3);
    printf("%s\n", c);
    read(fd3, &c, 3);
    printf("%s\n", c);
    read(fd4, &c, 3);
    printf("%s\n", c);
    read(fd5, &c, 3);
    printf("%s\n", c);
    close(fd1);
    close(fd2);
    close(fd3);
    close(fd4);
    close(fd5);
    return 0;
}
