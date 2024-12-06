#include <iostream>
#include <vector>
using namespace std;

// Driver Code
int main()
{
    // Creating a sample vector
    vector<int> v = { 1, 5, 10, 15, 20 };
    // (Option 1) Changing vector while iterating over it
    // (This causes iterator invalidation)
    // for (auto it = v.begin(); it != v.end(); it++)
    //    if ((*it) == 5)
    //        v.push_back(-1);
    
    //(Option 2) index based loop
    for (int i = 0; i < v.size(); i++) {  // index based loop
        if (v[i] == 5)
            v.push_back(-1);
    }

    for (auto it = v.begin(); it != v.end(); it++) // iterator based loop
        cout << (*it) << " ";

    return 0;
}