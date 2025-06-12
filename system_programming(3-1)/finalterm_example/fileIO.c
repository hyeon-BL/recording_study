#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
int main()
{
    char buf[4096] =
        {'A', 'B', 'C', '\0', 'D', 'E', 'F', '\0'};
    int fd;
    ssize_t nbytes;
    fd = open("hello.txt", O_CREAT | O_RDWR, 0655);
    write(fd, buf, 128);
    close(fd);
    fd = open("hello.txt", O_RDONLY);
    nbytes = read(fd, buf, sizeof(buf));
    close(fd);
    printf("%ld\n", nbytes);
    printf("%s\n", buf);
    return 0;
}