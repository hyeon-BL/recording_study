#include<iostream>
using namespace std;

int main() {
    int iVal1 = 3;
    int iVal2 = iVal1++;
    cout << iVal1 << '\t' << iVal2 << endl;

    int iVal3 = 3;
    int iVal4 = ++iVal3;
    cout << iVal3 << '\t' << iVal4 << endl;
}