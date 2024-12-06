#include <iostream>
#include <string.h>
using namespace std;

class Complex {
    int* m_r = nullptr;  // real part
    int* m_i = nullptr;  // imaginary part
public:
    // Constructor overloading : different ways to initialize the object
    Complex();
    Complex(int, int);
    Complex(int);
    ~Complex();
    Complex(const Complex& rhs);
    void print() const;
    //Operator overloading + (Complex + Complex)
    Complex operator+(const Complex& c2);
    //Operator overloading + (Complex + int)
    Complex operator+(int r);
    //Operator overloading + (Complex + double)
    Complex operator+(double r);
    //Operator overloading + (double + Complex)
    friend Complex operator+(double r, const Complex& c);
    //Operator overloading ==
    bool operator==(const Complex&);
    //Operator overloading +=
    void operator+=(const Complex&);

    Complex& operator++(); // prefix 
    Complex operator++(int dummy); // postfix 
    Complex& operator=(const Complex& c); // = operator overloading

};

Complex::Complex(int r, int i) {
    m_r = new int(r);
    m_i = new int(i);
}
Complex::~Complex() {
    if (m_r) delete m_r;
    if (m_i) delete m_i;
    m_r = m_i = nullptr;
}
Complex::Complex() : Complex(0, 0) { }
Complex::Complex(int r)
    : m_r{ new int(r) }, m_i{ new int(0) } { }
Complex::Complex(const Complex& rhs) : Complex(*rhs.m_r, *rhs.m_i) { }
void Complex::print() const {
    cout << *m_r << (*m_i < 0 ? "" : "+") << *m_i << "j" << endl;
}
//Operator overloading+ (Complex + Complex)
Complex Complex::operator+(const Complex& c2) {
    Complex result;
    *(result.m_r) = *(m_r)+*(c2.m_r);
    *(result.m_i) = *(m_i)+*(c2.m_i);
    return result;
}
//Operator overloading+ (Complex + int)
Complex Complex::operator+(int r) {
    Complex result;
    *(result.m_r) = *(m_r)+r;
    *(result.m_i) = *(m_i);
    return result;
}
//Operator overloading+ (Complex + double)
Complex Complex::operator+(double r) {
    return Complex((static_cast<int> (r)) + *(m_r), *(m_i)); // static_cast<int> (r) : convert double to int rounded down
}

//Operator overloading+ (double + Complex)
Complex operator+(double r, const Complex& c) {
    Complex result((static_cast<int> (r)) + *(c.m_r), *(c.m_i));
    return result;
}

bool Complex::operator==(const Complex& rhs) {
    if ((*m_r == *rhs.m_r) && (*m_i == *rhs.m_i))
        return true;
    else
        return false;
}
void Complex::operator+=(const Complex& rhs) {
    *m_r += *rhs.m_r;
    *m_i += *rhs.m_i;
}
//Prefix
Complex& Complex::operator++() {
    (*m_r)++;
    return *this;
}
//Postfix
Complex Complex::operator ++(int dummy) {
    Complex ret(*this);
    (*m_r)++;
    return ret;
}
//= operator overloading
Complex& Complex ::operator=(const Complex& c) {
    if (this == &c)
        return *this;
    delete m_r;
    delete m_i;
    m_r = new int(*c.m_r);
    m_i = new int(*c.m_i);
    return *this;
}



int main() {
    Complex c1; // 0 + 0j
    Complex c2(3, 1234); // 3 + 1234j
    Complex c3(-3); // -3 + 0j
    Complex c4(c2); // 3 + 1234j
    c1.print();
    c2.print();
    c3.print();
    c4.print();

    Complex c5(c2 + c3); //Complex + Complex
    c5.print(); // 0 + 1234j
    Complex c6(c2 + 4); //Complex + Int
    c6.print(); // 7 + 1234j
    Complex c7(c2 + 4.1); //Complex + double
    c7.print(); // 7 + 1234j

    Complex c8(5.2 + c3); //double + Complex
    c8.print(); // 2 + 0j

    Complex c9(3, 1234);
    if (c2 == c9) {
        cout << "Same" << endl; //Same
    }
    else {
        cout << "Different" << endl;
    }

    c3 += c2; //c3 = c3 + c2
    c3.print(); // 0 + 1234j


    int a = 1; int b = 1111;
    int c = 2; int d = 2222;
    int e = 3; int f = 3333;

    Complex c10(a, b); Complex c11(c, d); Complex c12(e, f);
    (c12 = c11) = c10;      //Expect 1.1111

    c10.print();   c11.print(); c12.print();
    return 0;
}