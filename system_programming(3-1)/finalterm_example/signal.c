#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

void handler(int sig)
{
    printf("I’m Dying\n");
    exit(0);
}
int main()
{
    pid_t pid1;
    signal(SIGUSR1, handler);
    if ((pid1 = fork()) == 0)
    {
        printf("Ready to Die\n");
        exit(0);
    }
    kill(pid1, SIGUSR1);
    printf("Die!\n");
    return 0;
}
