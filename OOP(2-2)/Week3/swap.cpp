#include<iostream>
using namespace std;


void intswap1(int num1, int num2) {
    int temp = num1;
    num1 = num2;
    num2 = temp;
}

void intswap2(int* num1, int* num2) {
    int temp = *num1;
    *num1 = *num2;
    *num2 = temp;
}

int main() {
    int num1 = 10;
    int num2 = 30;
    cout << num1 << '\t' << num2 << endl;
    intswap1(num1, num2); // 값이 바뀌지 않음(local 변수로 넘겨줌)
    cout << num1 << '\t' << num2 << endl;
    intswap2(&num1, &num2); // 값이 바뀜(주소로 넘겨줌)
    cout << num1 << '\t' << num2 << endl;
}