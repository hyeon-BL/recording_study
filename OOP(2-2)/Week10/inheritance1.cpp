#include <iostream>
#include <string.h>
using namespace std;

class Person {
private:
    // private members of the base class are not accessible in the derived class        
protected:
    string m_name; //Moved from private
    int* m_Id;    
public:
    string GetName() { return m_name; }
    void SetName(string name) { m_name = name; }
    Person() { m_Id = new int(1111); m_name = "None"; }; //Constructor
    int GetID() { return *(this->m_Id); }
    void SetID(int id) { *(this->m_Id) = id; }
  
};

class Student : public Person {
private:
public:
    string GetStudentName() { return this->m_name; } //OK
};

class Teacher : protected Person {
private:
public:
    int GetTeacherID() { 
        return this->GetID();
        //return *(this->m_Id); 
    } //NOT OK
    void SetTeacherName(string name) { this->SetName(name); } //OK
    string GetTeacherName() { return this->GetName(); } // OK
};

int main() {
    Student s1;
    Teacher t1;
    s1.SetName("Tom");
    // t1.SetName("Jenny"); // Person::SetName is protected in Teacher
    t1.SetTeacherName("Jenny");
    cout << s1.GetName() << endl;
    // cout << t1.GetName() << endl; // Person::GetName is protected in Teacher
    cout << t1.GetTeacherName() << endl;
    cout << s1.GetStudentName() << endl;
    cout << t1.GetTeacherID() << endl;  //OK
    // cout << s1.m_name << endl; //m_name is protected in Student
    return 0;
}