/*Example*/
#include <iostream>
#include <string.h>
using namespace std;





// class Lecture;

// //Student class
// class Student {
// private:
//     int* m_pId;
//     string m_name;
//     Lecture* m_lName;

// public:
//     Student();
//     Student(int, string);
//     string GetName();
//     void SetID(int id);
// };

// //Student implementation
// Student::Student() {
//     m_pId = new int(0);
//     m_name = "Alice";
// }
// Student::Student(int id, string name) {
//     m_pId = new int(id);
//     m_name = name;
// }

// string Student::GetName() {
//     return m_name;
// }

// void Student::SetID(int id) {
//     *(this->m_pId) = id;
// }

// //Teacher definition
// class Teacher {
// private:
//     int* m_pId;
//     string m_name;
//     Lecture* m_lecture;

// public:
//     Teacher();
//     Teacher(int, string);
//     string GetName();
//     void SetID(int id);
// };
// //Teacher implementation
// Teacher::Teacher() {
//     m_pId = new int(0);
//     m_name = "Alice";
// }

// Teacher::Teacher(int id, string name) {
//     m_pId = new int(id);
//     m_name = name;
// }

// string Teacher::GetName() {
//     return m_name;
// }
// void Teacher::SetID(int id) {
//     *(this->m_pId) = id;
// }

// //Lecture definition
// class Lecture {
// private:
//     int* m_pId;
//     string m_name;
//     Student* s_group; //A list of students
//     Teacher* m_Teacher; //Teacher

// public:
//     Lecture();
//     Lecture(int, string);
//     Lecture(int, string, Teacher*); //new constructor
//     string GetName();
//     void SetID(int id);
//     string getTeacherName() {
//         return m_Teacher->GetName();
//     }
// };

// //Lecture implementation
// Lecture::Lecture() {
//     m_pId = new int(0);
//     m_name = "Alice";
// }

// Lecture::Lecture(int id, string name) {
//     m_pId = new int(id);
//     m_name = name;
// }
// //New constructor
// Lecture::Lecture(int id, string name, Teacher* t) {
//     m_pId = new int(id);
//     m_name = name;
//     this->m_Teacher = t; //Assign teacher to the lecture
// }

// string Lecture::GetName() {
//     return m_name;
// }
// void Lecture::SetID(int id) {
//     *(this->m_pId) = id;
// }

// int main() {
//     Student s1(201911999, "Alice");
//     Teacher t1(111111111, "Tom");
//     Lecture l1(222222222, "OOP");
//     Lecture l2(33333, "OOP2", &t1); //3rd constructor -> Lecture(int, string, Teacher*)

//     cout << s1.GetName() << endl;
//     cout << t1.GetName() << endl;
//     cout << l1.GetName() << endl;

//     cout << l2.GetName() << endl;
//     cout << l2.getTeacherName() << endl;



//     return 0;
// }






// class Student {
// private:
//     int* m_pID;
//     string m_name;
// public:
//     Student(); //Constructor 1
//     Student(int, string); //Constructor 2
//     ~Student(); //Destructor
//     void InitVariables(int, string);
//     int GetID() { return *m_pID; }
//     string GetName();
//     //string GetName() { return m_name; }
// }; //end of class definition

// //Implementation of the member fuctions
// //Constructor 1 (Modified)
// //Student::Student() : m_pID{ new int{0} }, m_name{ "Alice" } {
// Student::Student() : Student(0, "Alice"){
//     //m_pID = new int(0);
//     //m_name = "Alice";
//     cout << "Constructor 1: " << m_name<<  endl;
// }

// //Constructor 2 (Modified)
// Student::Student(int id, string name) :m_pID{ new int{id} }, m_name{ name } {
//     //m_pID = new int(id);
//     //m_name = name;
//     cout << "Constructor 2: " <<m_name<< endl;
// }
// //Destructor implementation
// Student::~Student() {
//     cout << "Destructor: " << m_name << endl;
//     if (m_pID != nullptr) {
//         delete m_pID;
//         m_pID = nullptr;
//     }
    
// }
// void Student::InitVariables(int id, string m_name) {
//     //m_pID = new int(id);
//     this->m_pID = new int(id);
//     this->m_name = m_name;
//     //this->m_name = m_name;
// }
// string Student::GetName() {
//     return m_name;
// }


// int main() {
//     Student s1; //in stack -> Constructor 2 and then Constructor 1
//     Student* s2; //in stack
//     s2 = new Student(123, "Jenny"); //in heap -> Constructor 2
//     delete s2; //Remove from heap

//     //Student s1;
//     //cout << s1.GetName() << endl;
//     //Student s2;
//     //s1.InitVariables(2011, "Alice");
//     //s2.InitVariables(2022, "Tom");
    
//     //cout << s2.GetName() << endl;

//     cout << "==== Place 1===" << endl;
//     Student student1; //in stack -> Constructor 2 and then Constructor 1
//     Student student2(2, "Jenny"); // in stack -> Constructor 2
//     cout << "==== Place 2===" << endl;
//     Student* student3; //Pointer -> 공간만 확보(initialize X)
//     cout << "==== Place 3===" << endl;
//     student3 = new Student(4, "Tom"); // Heap -> Constructor 2
//     cout << "==== Place 4===" << endl;
//     delete student3; //Remove from heap -> Destructor
//     cout << "==== Place 5===" << endl;
    

//     return 0; //Destructor(student1), Destructor(student2)
// }







// class Student {
// private:
//     int* m_pID;
//     string m_name;
// public:
//     Student(); //Constructor 1
//     Student(int, string); //Constructor 2
//     int GetID() { return *m_pID; }
//     string GetName();
//     //string GetName() { return m_name; }
// }; //end of class definition

// //Implementation of the member fuctions
// //Constructor 1
// Student::Student() {
//     m_pID = new int(0);
//     m_name = "Alice";
//     cout << "Constructor 1" << endl;
// }
// //Constructor 2
// Student::Student(int id, string name) {
//     m_pID = new int(id);
//     m_name = name;
//     cout << "Constructor 2" << endl;
// }
// string Student::GetName() {
//     return m_name;
// }


// int main() {
//     Student* student1; //Pointer -> 공간만 확보
//     cout << "==== Place 1===" << endl;
//     Student* student2; //Pointer -> 공간만 확보
//     cout << "==== Place 2===" << endl;
//     student1 = new Student(201911999, "John"); //Object is created in heap -> Constructor 2
//     cout << "==== Place 3===" << endl;
//     student2 = new Student(); //Object is created in heap -> Constructor 1
//     cout << "==== Place 4===" << endl;
//     Student student3; //Object is created in stack -> Constructor 1
//     cout << "==== Place 5===" << endl;
//     Student student4(12345, "Tom");//Object is created in stack -> Constructor 2
//     cout << "==== Place 6===" << endl;
//     Student many_students[3]; //Object is created in stack -> Constructor 1 (3 times)
//     cout << "==== Place 7===" << endl;
//     Student* ptr_many_students2; //Pointer
//     cout << "==== Place 8===" << endl;
//     ptr_many_students2 = new Student[5]; //in Heap -> Constructor 1 (5 times)
//     cout << "==== Place 9===" << endl;
//     for (int i = 0; i < 5; i++) {
//         cout << (ptr_many_students2 + i)->GetName() << endl; //pointer arithmetic
//         cout << ptr_many_students2[i].GetName() << endl;     //array notation
//     }
//     cout << "==== Place 10===" << endl;


//     delete student1; //Remove from heap -> Destructor
//     delete student2; //Remove from heap -> Destructor
//     delete[] ptr_many_students2; //Remove from heap -> Destructor (5 times)

// }







// struct Student {
//     int id;
//     string name;
//     Student* friends; //Added
// };

// int main() {
//     Student students[10];
//     Student* student1 = new Student{ 201911999, "John", nullptr };
//     Student* student2 = new Student{ 12345, "Tom", student1 };

//     student1->friends = student2;
//     cout << student1->friends->name << endl;
//     cout << student2->friends->name << endl;

//     cout << students[0].id << endl; // 초기화 안된 값
//     delete student1; // 삭제

//     //Dangling pointer
//     cout << student2->friends->name << endl; //삭제된 메모리를 참조

//     return 0;
// }







// int main()
// {
//     //const int value{ 5 }; //constant
//     int value{ 5 }; //non-constant
//     const int* ptr = &value;
//     // *ptr = 6; //Dereferencing for update
//     cout << "value: " << value << "\t*ptr" << *ptr << endl;

//     const int value2 = 3;
//     ptr = &value2;
//     cout << "value: " << value << "\t*ptr" << *ptr << endl;

   

//     return 0;
// }






// int foo()
// {
//     return 5;
// }
// double goo()
// {
//     return 6;
// }
// int hoo(int n)
// {
//     return n;
// }
// int main() { 
//     int (*fcnPtr)() { &foo }; // fcnPtr points to function foo (함수 포인터를 선언할 때 괄호 두 쌍)
//     double (*dfcnPtr)();
//     int (*pfcnPtr)(int);
//     dfcnPtr = &goo;
//     pfcnPtr = &hoo;
//     cout << fcnPtr() << endl;
//     cout << dfcnPtr() << endl;
//     cout << pfcnPtr(8) << endl;
//     return 0;
// }






// void intSwap1(int  num1, int  num2) {
//     int temp{ num1 };
//     num1 = num2;
//     num2 = temp;
// }
// void intSwap2(int* num1, int* num2) { //Pointer
//     int temp{ *num1 };
//     *num1 = *num2;
//     *num2 = temp;
// }
// void intSwap3(int& num1, int& num2) { //Reference
//     int temp{ num1 };
//     num1 = num2;
//     num2 = temp;
// }
// int* f1() {
//     //int iNums[3]{ 1,2,3 };
//     int* iNums = new int[3]; //Allocate in Heap
//     iNums[0] = 1;
//     iNums[1] = 2;
//     iNums[2] = 3;
//     return iNums; //return the Heap address of array
// }
// void f2() {
//     double i = 10;
//     double j = 20;
//     double k = i + j;
// }

// int main() {
//     int iNum1{ 1 };
//     int iNum2{ 3 };
//     cout << iNum1 << " " << iNum2 << endl;
//     intSwap3(iNum1, iNum2);
//     cout << iNum1 << " " << iNum2 << endl;
//     int* pNums = f1(); // pNums points to the array in Heap
//     f2();
//     f2();
//     f2();
//     cout << *pNums << endl; //?? -> 1
//     delete[] pNums;
//     return 0;
// }