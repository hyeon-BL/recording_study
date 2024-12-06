#include <iostream>
#include <string.h>
using namespace std;

class Teacher {
private:
    int* m_pId;
    string m_name;
    string teacher_hobby = "Play a Video Game";


    friend class Student; //Stduent becomes a freiend of Teacher ( private member can be accessed by Student )
    friend string GetTeacherHobby(Teacher t) { return t.teacher_hobby; }; 
    string GetTeacherHobby(Teacher t) { return t.teacher_hobby; };


};
class Student {
private:
    int* m_pId = nullptr;
    string m_name = "";
public:
    static int StudentCnt;
    Student(int, string); 
    Student(const Student& rhs); 
    ~Student();
    int Get_ID() { return *(this->m_pId); }
    int* Get_ID_Addr() { return this->m_pId; }
    string Get_Name() const { return this->m_name; }
    void Set_Name(string newName)  { this->m_name = newName; } // const can't be used here



    void ShowTeacherHobby(Teacher t) {
        cout << GetTeacherHobby(t) << endl;
        cout << t.GetTeacherHobby(t) << endl;
        cout << t.teacher_hobby << endl; //Directly access private member of Teacher
    }



};
//Initialize static variable
int Student::StudentCnt = 0;
Student::Student(int id, string name) : m_pId{ new int{id} }, m_name{ name } {
    cout << "Constructor" << endl;
    Student::StudentCnt++;
}
Student::Student(const Student& rhs) {
    this->m_pId = new int(*rhs.m_pId); //Heap allocation and copy.
    this->m_name = rhs.m_name;
    cout << "Copy Constructor" << endl;
    Student::StudentCnt++;
}
Student::~Student() {
    delete m_pId; 
    cout << "Destructor" << endl;
    Student::StudentCnt--; //Decrease student count
}

void printStudentName(Student s){ //Call by value
    cout << "===Start function===" << endl;
    cout << s.Get_Name() << endl;
    cout << "===End function===" << endl;
    cout << "Total students A: " << Student::StudentCnt << endl;
}

int main() {
    Student s1(201911999, "Alice");
    Teacher t1;
    cout << GetTeacherHobby(t1) << endl; //Directly access private member (friend)
    s1.ShowTeacherHobby(t1);

    return 0;
}
