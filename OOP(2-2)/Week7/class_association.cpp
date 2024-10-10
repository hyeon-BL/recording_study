#include <iostream>
#include <string>
using namespace std;
//Vehicle class represents an individual vehicle
class Vehicle {
    private:
        string id;
        int mileage;
    public:
        Vehicle(int m, string c) {
            mileage = m; id = c;
            cout << "[Vehicle]: Constructor [Car ID]: " << id << endl;
    }
    ~Vehicle(){cout<<"[Vehicle]: Destructor [Car ID]: "<<id<<endl;}
};
//VehicleGroup class manages a group of multiple vehicles
class VehicleGroup {
    private:
        Vehicle** vGroup; // Store a list of the [Vehicle*]
        int vNum; //The number of vehicles in the group
        int lastEmptyIndex; //The index of the first empty place in the vGroup array 
    public:
        //Constructor
        VehicleGroup(int size) {
            cout << "[VehicleGroup]: Constructor" << endl;
            //Dynamically allocate the array of [Vehicle*] type
            vGroup = new Vehicle*[size]; 
            vNum = size;
            lastEmptyIndex = 0;
    }
    //Add Vehicle object to vGroup
    void addVehicle(Vehicle* t_vehicle) {
        //Question 1: Implement addVehicle member function
        //Hint: Add Vehicle* to the last empty index of vGroup
        if (lastEmptyIndex >= vNum) {
            cout << "The group is full" << endl;
            return;
        }
        vGroup[lastEmptyIndex] = t_vehicle;
        lastEmptyIndex++;
    }
    //Destructor
    ~VehicleGroup() {
        //Question 2: Implement the destructor of VehicleGroup
        //Hint: Deallocate the heap memory
        for (int i = 0; i < vNum; i++) {
            delete vGroup[i];
        }
        delete[] vGroup;
        cout << "[VehicleGroup]: Destructor" << endl;
    }
};
int main() {
    Vehicle* car1 = new Vehicle(1000, "BMW");
    Vehicle* car2 = new Vehicle(2000, "GM");
    Vehicle* car3 = new Vehicle(3000, "TESLA");
    Vehicle* car4 = new Vehicle(4000, "Audi");
    VehicleGroup* group = new VehicleGroup(3);
    group->addVehicle(car1);
    group->addVehicle(car2);
    group->addVehicle(car3);
    group->addVehicle(car4);
    delete group;
    return 0;
}