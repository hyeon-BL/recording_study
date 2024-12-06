#include <iostream>
#include <string.h>
using namespace std;

class Teacher {
private:
    int* m_pId;
    string m_name;
    string teacher_hobby = "Play a Video Game";
    friend class Student; //Stduent becomes a freiend of Teacher
    //friend string GetTeacherHobby(Teacher t) { return t.teacher_hobby; };
    string GetTeacherHobby(Teacher t) { return t.teacher_hobby; };
};
class Student {
private:
    int* m_pId = nullptr;
    string m_name = "";
public:
    static int StudentCnt; //Static member variable
    Student(int, string); //Constructor
    Student(const Student& rhs); //Copy Constructor
    ~Student();
    int Get_ID() { return *(this->m_pId); }
    int* Get_ID_Addr() { return this->m_pId; }
    string Get_Name() const { return this->m_name; }
    void Set_Name(string newName)  { this->m_name = newName; }
    void ShowTeacherHobby(Teacher t) {
        //cout << GetTeacherHobby(t) << endl;
        cout << t.GetTeacherHobby(t) << endl;
        cout << t.teacher_hobby << endl; //Directly access private member of Teacher
    }
};
//Initialize static variable
int Student::StudentCnt = 0;
//Constructor
Student::Student(int id, string name) : m_pId{ new int{id} }, m_name{ name } {
    cout << "Constructor" << endl;
    Student::StudentCnt++;
}
//Copy Constructor
Student::Student(const Student& rhs) {
    this->m_pId = new int(*rhs.m_pId); //Heap allocation and copy.
    this->m_name = rhs.m_name;
    cout << "Copy Constructor" << endl;
    Student::StudentCnt++;
}
//Destructor
Student::~Student() {
    delete m_pId; 
    cout << "Destructor" << endl;
    Student::StudentCnt--; //Decrease student count
}

//Test Function
// void printStudentName(Student s){ //Call by value -> Copy constructor should be called
void printStudentName(Student* s) { //Call by reference -> Pass the address of s
    cout << "===Start function===" << endl;
    // cout << s.Get_Name() << endl;
    cout << s->Get_Name() << endl;
    cout << "===End function===" << endl;
    cout << "Total students A: " << Student::StudentCnt << endl;
}

int main() {

    int iNum1 = 10;
    int iNum2{ iNum1 }; // different address 
    Student s1(201911999, "Alice");
    Student s2(s1); // same address

    cout << "iNum1: " << iNum1 << " iNum1 address: " << &iNum1 << endl; 
    cout << "iNum2: " << iNum2 << " iNum2 address: " << &iNum2 << endl;
    cout << "s1: " << s1.Get_Name() << " " << s1.Get_ID() << " " << s1.Get_ID_Addr() << endl;
    cout << "s2: " << s2.Get_Name() << " " << s2.Get_ID() << " " << s2.Get_ID_Addr() << endl;
    
    // printStudentName(s2);
    printStudentName(&s2);
    cout << "Total students B: " << Student::StudentCnt << endl;
    return 0;
}
