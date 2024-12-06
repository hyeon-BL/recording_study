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

    /*
        virtual invokes the most derived function in the hierarchy
    */

    //Virtual Destructor to call derived class destructor (if not virtual, only base class destructor is called)
    virtual ~Person() { 
        cout << "Person Destructor" << endl; 
    }
    int GetID() { return *(this->m_Id); }
    void SetID(int id) { *(this->m_Id) = id; }
    //Virtual functions
    virtual void work() { cout << "Person Work" << endl; }
    virtual string GetClassName() { return "Person"; }
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


    //Override Person's functions
    void work() { cout << "Student studies" << endl; }
    string GetClassName() { return "Student"; }
};

class DGISTStudent : public Student {
public:
    DGISTStudent() { cout << "DGIST Student Constructor" << endl; }
    ~DGISTStudent() { cout << "DGIST Student Destructor" << endl; }


    //Override
    void work() { cout << "DGIST Student studies" << endl; }
    string GetClassName() { return "DGIST Student"; }
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
        return this->GetID();
        //return *(this->m_Id); 
    } //NOT OK
    void SetTeacherName(string name) { this->SetName(name); } //OK
    string GetTeacherName() { return this->GetName(); } // OK


    //Override
    void work() { cout << "Teacher teaches" << endl; }
    string GetClassName() { return "Teacher"; }

};

int main() {
    DGISTStudent dgs1;
    Person* s2 = &dgs1; //Up casting
    s2->work();
    cout << dgs1.GetClassName() << endl;
    cout << s2->GetClassName() << endl;
    cout << "===Place 1===" << endl;

    Person p1;
    Student s1;
    Teacher t1;
    DGISTStudent ds1;
    p1.work();
    s1.work();
    t1.work();
    cout << p1.GetClassName() << endl;
    cout << s1.GetClassName() << endl;
    cout << t1.GetClassName() << endl;
    cout << ds1.GetClassName() << endl;
    cout << "===Place 2===" << endl;

    Person* p_arr[] = { &s1, &t1, &ds1 }; //Up casting
    for (int i = 0; i < 3; i++) {
       p_arr[i]->work();
       cout << p_arr[i]->GetClassName() << endl;
    }

    return 0;
}