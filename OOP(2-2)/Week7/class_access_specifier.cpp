#include<iostream>
#include<string>
using namespace std;

class Vehicle {
    private:
        string id;
    public:
        int mileage;
        Vehicle() {
            mileage = 10; id = "None";
        }
        Vehicle(int m) : Vehicle(m, "None") {}
        Vehicle(string i) : Vehicle(10, i) {}
        Vehicle(int m, string i) {
            mileage = m; id = i;
        }
        string getID() {
            return id;
        }
        void setID(string i) {
            id = i;
        }
        int getMileage() {
            return mileage;
        }
};
Vehicle* cloneVehicle(Vehicle* v) {
    Vehicle* newV = new Vehicle(v->getID());
    newV->mileage = v->getMileage();
    return newV;
}

int main() {
    Vehicle car1;
    car1.setID("BMW");
    Vehicle* car1_clone = cloneVehicle(&car1);
    cout << "Clone ID: " << car1_clone->getID() << endl;
    cout << "Clone Mileage: " << car1_clone->getMileage() << endl;
    return 0;
}