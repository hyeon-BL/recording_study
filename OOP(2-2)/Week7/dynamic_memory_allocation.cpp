#include<iostream>
using namespace std;

struct Teacher {
    int id;
    string t_name;
};
struct Student {
    int s_id;
    Teacher* myTeacher; // pointer to Teacher object
};

int main() {
    const int NUM_T = 2;
    const int NUM_S = 4;
    Teacher* t_arr = new Teacher[NUM_T]; // Teacher t_arr[NUM_T] = {Teacher(), Teacher()};
    Student** s_arr = new Student* [NUM_S]; // Student* s_arr[NUM_S] = {new Student(), new Student(), new Student(), new Student()};

    t_arr[0] = {555, "David"}; // t_arr[i]는 sta
    t_arr[1] = {666, "John"};

    for (int i = 0; i < NUM_S; i++) {
        s_arr[i] = new Student();
        (*s_arr[i]).s_id = i;
        (*s_arr[i]).myTeacher = &t_arr[i % 2];
    }
    for (int i = 0; i < NUM_S; i++) {
        cout << (*s_arr[i]).s_id << " " << (*s_arr[i]).myTeacher->t_name << endl;
    }

    
    
    for (int i = 0; i < NUM_S; i++) {
        delete s_arr[i];
    }
    delete[] s_arr;
    delete[] t_arr;



    return 0;
}