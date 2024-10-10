#include<iostream>
#include<string>
using namespace std;

class Vehicle {
    private:
        string id;
        int mileage;
        Vehicle* friendV;
    public:
        Vehicle(int m, string i) {
            mileage = m; id = i;
            friendV = nullptr;
        }
        Vehicle(int m, string i, Vehicle* f) {
            mileage = m; id = i;
            friendV = f;
        }
        ~Vehicle() {
            if (friendV != nullptr) {
                delete friendV;
            }
        }
        string getID() {
            return id;
        }
        string getFriendID() {
            return friendV->getID();
        }
};

int main() {
    Vehicle* car1 = new Vehicle(10, "BMW");
    Vehicle* car2 = new Vehicle(20, "Benz", car1);
    cout << "car2's friend: " << car2->getFriendID() << endl;
    cout << "car2's ID: " << car2->getID() << endl;
    cout << "car1's ID: " << car1->getID() << endl;
    delete car2;
    return 0;
}