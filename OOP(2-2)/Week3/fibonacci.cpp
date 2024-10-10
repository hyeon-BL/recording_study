#include <iostream>
using namespace std; 
int fibonacci(int n) { 
    if (n < 2) return 1; 

    int n_minus_1 = fibonacci(n-1); 
    int n_minus_2 = fibonacci(n-2); 
    return n_minus_1 + n_minus_2; 
} 

int main() { 
    int n = 4; 
    cout << fibonacci(n) << endl; 
    return 0; 
}