#include <iostream>
using namespace std;

int main() {
    try { //1st level
        cout << "==1==" << endl;
        //throw 3;
        cout << "==2==" << endl;
        try { //2nd level
            cout << "==3==" << endl;
            throw "test";
            cout << "==4==" << endl;

            //throw 3.5;
            cout << "==5==" << endl;
        }
        catch (int i) { //2nd level
            cout << "==A==" << endl;
        }
        catch (const char* s) { //2nd level
            cout << "==B==" << endl;
        }
        cout << "end of 1st level" << endl;
    }
    catch (double d) { //1st level
        cout << "==C=" << endl;
    }
    catch (...) { //1st level
        cout << "==D==" << endl;
    }

    cout << "end of program" << endl;
    return 0;
}