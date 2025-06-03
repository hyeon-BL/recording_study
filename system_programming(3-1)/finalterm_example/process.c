#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main()
{
    pid_t pid;
    int x = 1; // 지역 변수

    pid = fork(); // fork() 호출

    if (pid < 0)
    { // 오류 처리
        fprintf(stderr, "Fork Failed\n");
        return 1;
    }
    else if (pid == 0)
    {
        // 자식 프로세스 영역
        printf("Child PID is %d, my x before change = %d\n", getpid(), x);
        x++; // 자식의 x 값 변경
        printf("CHILD: I am child process (PID: %d), my parent is %d. My x = %d\n", getpid(), getppid(), x);
    }
    else
    {
        // 부모 프로세스 영역
        printf("Parent PID is %d, my x before change = %d\n", getpid(), x);
        x--; // 부모의 x 값 변경
        printf("PARENT: I am parent process (PID: %d), my child is %d. My x = %d\n", getpid(), pid, x);
    }
    printf("Common part by PID %d, x = %d\n", getpid(), x); // 부모와 자식 모두 각자의 x 값을 가짐
    return 0;
}