#include <stdio.h>
#include <stdlib.h>
#ifdef _WIN32
#include <io.h>
#else
#include <unistd.h>
#endif
#include <fcntl.h>

int main()
{
    int fd1, fd2, fd3, fd4, fd5;
    char c;

    // 5개의 별도 파일 디스크립터를 open으로 생성합니다.
    fd1 = open("hello.txt", O_RDONLY);
    fd2 = open("hello.txt", O_RDONLY);
    fd3 = open("hello.txt", O_RDONLY);
    fd4 = open("hello.txt", O_RDONLY);
    fd5 = open("hello.txt", O_RDONLY);

    // dup2(fd1, fd2): fd2는 fd1을 복제하므로 fd1과 fd2는 같은 파일 설명자(파일 오프셋 공유)
    dup2(fd1, fd2);
    // dup2(fd4, fd5): fd5는 fd4를 복제하므로 fd4와 fd5는 같은 파일 설명자(파일 오프셋 공유)
    dup2(fd4, fd5);
    // dup2(fd3, fd4): fd4를 fd3의 복제로 변경, 이제 fd3와 fd4는 같은 파일 설명자
    // (원래 fd4와 fd5가 공유하던 오프셋은 fd5만 그대로 남음)
    dup2(fd3, fd4);

    // 현재 각 그룹별 파일 오프셋 상태 (hello.txt의 내용은 file_IO1에서 작성한 대로)
    // 오프셋: 읽기/쓰기 위치를 나타내는 포인터, 파일 디스크립터마다 독립적
    // file_IO1에서 작성된 buf: {'A', 'B', 'C', '\0', 'D', 'E', 'F', '\0', 0, 0, ...} (총 128바이트)
    //
    // 그룹 A: fd1, fd2 (공유 오프셋)
    // 그룹 B: fd3, fd4 (공유 오프셋)
    // 그룹 C: fd5 (별도 오프셋)
    //
    // 각 파일 디스크립터의 초기 오프셋은 0 (파일의 시작)
    //
    // read(fd1, &c, 1);
    //   그룹 A에서 첫 번째 바이트 'A'를 읽고, 그룹 A의 오프셋이 1로 증가.
    // read(fd2, &c, 1);
    //   fd2는 그룹 A와 공유하므로 오프셋은 이미 1인 상태, 'B'를 읽고 오프셋이 2가 됨.
    // read(fd3, &c, 1);
    //   그룹 B의 초기 오프셋 0에서 'A'를 읽고, 그룹 B 오프셋은 1로 증가.
    // read(fd4, &c, 1);
    //   fd4는 그룹 B와 공유하므로 현재 오프셋 1에서 'B'를 읽고 오프셋이 2가 됨.
    // read(fd5, &c, 1);
    //   그룹 C의 독자적 오프셋 0에서 'A'를 읽고, 오프셋은 1로 증가.

    // 따라서 예상 출력:
    // A   (from fd1)
    // B   (from fd2)
    // A   (from fd3)
    // B   (from fd4)
    // A   (from fd5)

    read(fd1, &c, 1);
    printf("%c\n", c);
    read(fd2, &c, 1);
    printf("%c\n", c);
    read(fd3, &c, 1);
    printf("%c\n", c);
    read(fd4, &c, 1);
    printf("%c\n", c);
    read(fd5, &c, 1);
    printf("%c\n", c);

    close(fd1);
    close(fd2);
    close(fd3);
    close(fd4);
    close(fd5);
    return 0;
}