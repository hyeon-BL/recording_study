#include <stdio.h>
#include <stdlib.h>
#ifdef _WIN32
#include <io.h>
// Windows에서는 ssize_t가 기본적으로 정의되어 있지 않으므로 long형으로 정의
typedef long ssize_t;
#else
#include <unistd.h>
#endif
#include <fcntl.h>

int main()
{
    // 버퍼를 초기화합니다.
    // 버퍼에 'A', 'B', 'C', NULL, 'D', 'E', 'F', NULL 이 저장되고 나머지는 0으로 채워짐
    char buf[4096] =
        {'A', 'B', 'C', '\0', 'D', 'E', 'F', '\0'};

    int fd;
    ssize_t nbytes;

    // 파일을 연다. O_CREAT: 파일이 없으면 생성
    // O_RDWR: 읽기 및 쓰기 모드, 0655: 파일 모드(권한) 설정
    // 시스템 콜 open()을 호출하면 커널 내부에서 해당 파일에 대한 파일 디스크립터(fd)를 반환합니다.
    fd = open("hello.txt", O_CREAT | O_RDWR, 0655);

    // 파일에 데이터를 쓴다.
    // write()는 파일 디스크립터를 통해 지정된 버퍼(buf)의 128 바이트를 파일에 씁니다.
    // 실제로 OS에서는 내부적으로 버퍼링, 캐싱 등을 수행할 수 있음
    write(fd, buf, 128);

    // 작업이 끝난 후 파일을 닫아 파일 디스크립터를 해제
    close(fd);

    // 다시 파일을 읽기 위해 O_RDONLY 모드로 open 호출
    fd = open("hello.txt", O_RDONLY);

    // read()를 이용하여 파일에서 최대 buf 크기 만큼 읽는다.
    // 시스템 콜 read()는 실제로 읽은 바이트 수를 반환합니다.
    nbytes = read(fd, buf, sizeof(buf));

    // 파일 디스크립터를 닫아줍니다.
    close(fd);

    // 읽은 바이트 수를 출력합니다.
    printf("%ld\n", nbytes);

    // 파일에서 읽은 버퍼 내용을 문자열로 출력합니다.
    // 버퍼에 NULL 종료가 있는지 확인하여 출력할 수 있음('\0'이 있는 위치까지 출력)
    printf("%s\n", buf);

    return 0;
}