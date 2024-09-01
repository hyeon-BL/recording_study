// cout precision is 6 by default.

#include <iostream>
using namespace std;
int main() {
    cout << 5.0 << '\n'; // 5
    cout << 6.7f << '\n'; // 6.7
    cout << 9876543210.123456789 << '\n'; // 9.87654e+09 -> 9876540000 (6 digits without information loss)
    return 0;
}