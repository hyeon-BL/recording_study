#include<iostream>
using namespace std;

int main() {
    int num[3]{ 10, 20, 30 };
    int* ptr = num; // num의 주소를 ptr에 저장(num[0]의 주소)
    cout << ptr << endl; // num[0]의 주소
    cout << ptr + 1 << endl; // num[1]의 주소
    cout << *ptr << endl; // num[0]의 값
    cout << *(ptr + 1) << endl; // num[1]의 값
}