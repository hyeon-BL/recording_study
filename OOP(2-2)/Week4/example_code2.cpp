/*Example*/
#include <iostream>
#include <string.h>
using namespace std;

// int main() {
    // int* ptr3 = new int{ 40 };
    // delete ptr3;
    // *ptr3 = 10; //Error


    // int* ptr = new int{ 10 };
    // int* ptr2 = new int{ 20 };
    // *ptr = 30;
    // ptr = ptr2;


    // int* ptr; 
    // while (1) {
    //     cout << "Hello";
    //     ptr = new int[100000]; //Heap allocation
    //     // delete[] ptr; //Heap deallocation(하지 않으면 memory leak)
    // }

//     int* ptr;
//     ptr = new int[10];
//     // ptr = new int[10] {0};
//     ptr[0] = 0;
//     *(ptr + 1) = 1;
//     for (int i = 0; i < 10; i++)
//         *(ptr + i) = i;
//     for (int i = 0; i < 10; i++)
//         cout << ptr[i] << " ";
//     // delete ptr; -> 단일 메모리 해제
//     delete[] ptr; //Should use this version for array deallocation 
//     return 0;
// }



// void fun(int arr[])// SAME AS void fun(int *arr)
// {
//     unsigned int n = sizeof(arr) / sizeof(arr[0]);
//     cout << "Array size inside fun() is :" << n << endl; // 1 (pointer size / int size)
//     cout << "sizeof(arr)" << sizeof(arr) << endl;        // 4 (pointer size)
//     cout << "sizeof(arr[0])" << sizeof(arr[0]) << endl;  // 4 (int size)
// }

// void fun2(int arr[], unsigned int n)// SAME AS void fun(int *arr)
// {
//     int i;
//     for (int i = 0; i < n; i++) {
//         cout << arr[i] << endl;
//         arr[i] = arr[i] + 100;
//     }    
// }
// int main()
// {
//     int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8 };
//     unsigned int n = sizeof(arr) / sizeof(arr[0]);
//     cout << "Array size inside main() is :" << n << endl;
//     cout << "sizeof(arr)" << sizeof(arr) << endl;
//     cout << "sizeof(arr[0])" << sizeof(arr[0]) << endl;
//     fun(arr); //memory address of the array
//     fun2(arr, n); //memory address of the array + # of elements
//     cout << "======after fun2======" << endl;
//     for (int i = 0; i < n; i++) {
//         cout << arr[i] << endl;
//     }
//     return 0;
// }



// int main() {
//     double arr[3]; //array of double type
//     double* ptr; //pointer of double type

//     cout << "Displaying address using arrays: " << endl;

//     for (int i = 0; i < 3; i++) {
//         cout << "&arr[" << i << "]=" << &arr[i] << endl;
//     }

//     ptr = arr; 
//     cout << "\nDisplaying address using pointers: " << endl;
    
//     for (int i = 0; i < 3; i++) {
//         cout << "ptr+" << i << "=" << ptr + i << endl;
//     }

//     return 0;
// }