#include<iostream>
using namespace std;

void addAll(int input[], int size, int* output) {
    *output = 0;
    for (int i = 0; i < size; i++) {
        *output += input[i];
    }
}
int main() {
    int arr[] = {3, 6, 9};
    int t_out = 0;
    addAll(arr, 3, &t_out);
    cout << t_out << endl;
    return 0;
}

/* 같은 결과
void addAll(int input[], int size, int& output) {
    output = 0;
    for (int i = 0; i < size; i++) {
        output += input[i];
    }
}
int main() {
    int arr[] = {3, 6, 9};
    int t_out = 0;
    addAll(arr, 3, t_out);
    cout << t_out << endl;
    return 0;
}
*/