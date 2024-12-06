#include <iostream>
using namespace std;


template<typename T> // function template
void Swap(T& a, T& b) {
    T tmp;
    tmp = a;
    a = b;
    b = tmp;
}

template<typename T1, typename T2 = const char*> // class template
//template<typename T1 = int, typename T2> //Not ok (default argument should be at the end)
class Student {
    T1 id;
    T2 name;
public:
    Student(T1 id, T2 name) : id(id), name(name) {}
    void Print() { cout << "id: " << id << " name: " << name << endl; }
};

int main() {
    int a = 10, b = 5;
    Swap<int>(a, b);
    cout << "a = " << a << " b = " << b;
    double c = 1.0, d = 2.0;
    Swap<double>(c, d);
    cout << "\nc = " << c << " d = " << d;

    Student<int> s1(1, "Tom");
    Student<const char*> s2("A001", "Jerry");
    s1.Print();
    s2.Print();
}