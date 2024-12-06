#include <iostream>
#include <string.h>
using namespace std;

class Person {
private:
protected:
    string m_name;
    int* m_Id;
public:
    string GetName() { return m_name; }
    void SetName(string name) { m_name = name; }
    Person() { //Constructor 1
        m_Id = new int(1111); m_name = "None"; 
       cout << "Person constructor 1 called" << endl;
    }; 
    Person(int id) {//Constructor 2
        m_Id = new int(id); m_name = "None"; 
       cout << "Person constructor 2 called" << endl;
    }
    virtual ~Person() { cout << "Person Destructor" << endl; }
    int GetID() { return *(this->m_Id); }
    void SetID(int id) { *(this->m_Id) = id; }

};

class Student : public Person {
private:
    int stu_temp = 10;
    int* stu_arr;
public:
    Student() : Person(10) { //Constructor
        stu_arr = new int[1000000]; //Heap allocation
       cout << "Student constructor called" << endl;
    }
    ~Student() { 
       cout << "Student Destructor" << endl; 
        delete[] stu_arr; //Deallocate from heap
    }
    string GetStudentName() { return this->m_name; } //OK
    int GetStudentTemp() { return stu_temp; }
};

class Teacher : public Person {
private:
public:
    Teacher() { //Constructor
       cout << "Teacher constructor called" << endl;
    }
    ~Teacher() { 
       cout << "Teacher Destructor" << endl; 
    }
    int GetTeacherID() {
        // return this->GetID();
        return *(this->m_Id); 
    } //NOT OK
    void SetTeacherName(string name) { this->SetName(name); } //OK
    string GetTeacherName() { return this->GetName(); } // OK
};

int main() {
    //Example 1 - constructor(person->teacher) and destructor(teacher->person)
    Teacher* tea = new Teacher(); //Heap
    delete tea;

    //Example 2 - constructor(person->student) and destructor(student->person)
    Person* p_person = new Student();//(1) Create student (2) Up casting to Person
    delete p_person;
    

    Student s1; //Student constructor called
    Teacher t1; //Teacher constructor called
    s1.SetName("Tom");
    s1.SetID(5555);
    t1.SetName("Jenny");
    t1.SetID(6666);

    Person* p_arr[] = { &s1, &t1 }; //IMPORTANT UP CASTING
    //p_arr[0] is Student, p_arr[1] is Teacher
    cout << ((Student*)p_arr[0])->GetStudentName() << endl; //DOWNCASTING
    cout << ((Teacher*)p_arr[0])->GetTeacherID() << endl; //DOWNCASTING
    cout << ((Teacher*)p_arr[1])->GetTeacherID() << endl; //DOWNCASTING
    cout << ((Student*)p_arr[1])->GetStudentName() << endl; //DOWNCASTING

    cout << ((Student*)p_arr[0])->GetStudentTemp() << endl;
    cout << ((Student*)p_arr[1])->GetStudentTemp() << endl; // information loss (Teacher does not have stu_temp)

    for (int i = 0; i < 2; i++) {
       cout << p_arr[i]->GetID() << "\t" << p_arr[i]->GetName() << endl;
    }
    cout << s1.GetStudentName() << endl;
    // cout << p_arr[0]->GetStudentName() << endl; //Error because Person does not have GetStudentName
    // cout << p_arr[1]->GetTeacherID() << endl; //Error because Person does not have GetTeacherID
    
    return 0;
}