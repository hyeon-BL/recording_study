#include<iostream>
using namespace std;

int sum(int arr[], int size) {
    if (size == 0) {
        return 0;
    }
    return arr[size - 1] + sum(arr, size - 1);
}

int main() {
    int nums1[] = {1, 2, 3};
    cout << sum(nums1, sizeof(nums1) / sizeof(int)) << endl;
    int nums2[] = {1, 3, 5, 7, 9};
    cout << sum(nums2, sizeof(nums2) / sizeof(int)) << endl;
    int nums3[] = {2, 4, 6, 8, 10};
    cout << sum(nums3, sizeof(nums3) / sizeof(int)) << endl;
    return 0;
}