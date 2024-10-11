/*Example*/
#include <iostream>
#include <string.h>
using namespace std;
// int main() {
//     int iNums[2][3] = { 1, 2, 3, 4, 5, 6 }; //2D array

//     cout << iNums << endl; //(1) Address of the first row
//     cout << *iNums << endl; //(2) Dereferncing once : Address of the first element of the first row
//     cout << **iNums << endl; //(3) Dereferencing twice : Value of the first element of the first row
//     cout << &(iNums[0][0]) << endl; // Address of iNums[0][0]
    
//     cout << **(iNums + 1) << endl; //(4) iNums + 1 = iNums[1] = {4, 5, 6}
//     cout << *((*iNums) + 1) << endl; //(5) iNums[0] + 1 = 2
//     cout << *((*(iNums + 1)) + 1) << endl; //(6) iNums[1] + 1 = 5
//     cout << *((*(iNums + 1)) + 1) + 100 << endl; //(7) 5 + 100 = 105



//     return 0;
// }
// int main() {
//     int iNum[3]{ 1, 2, 3 };
//     int* pNum = iNum; // &iNum[0];
//     cout << pNum << endl;  // address of iNum[0]
//     cout << pNum + 1 << endl; // address of iNum[1]
//     cout << pNum + 2 << endl; // address of iNum[2]
//     cout << *pNum << endl; //Dereferncing
//     cout << *(pNum + 1) << endl; // pNum[1]

//     return 0;
// }
// int main() {
//     int iNum = 0;
//     int iNums[3] = { 1, 2, 3 };

//     int* pNum = &iNum;
//     int* pNums1 = &iNums[0];
//     int* pNums2 = iNums;                 // &iNums ? -> iNums[0]

//     cout << pNums1 << endl << pNums2 << endl;
//     cout << *pNums1 << endl << *pNums2 << endl; //Dereferencing -> iNums[0]
//     cout << iNums[1] << endl << pNums1[1] << endl << pNums2[1] << endl;

//     return 0;
// }
// int main() {
//     int studentID[][3] = { {1 }, {4, 5, 6} };
//     cout << studentID[0][0] << endl; //1
//     cout << studentID[0][1] << endl; //0 (default value)
//     cout << studentID[0][2] << endl; //0
//     cout << studentID[1][0] << endl; //4
//     cout << studentID[1][1] << endl; //5
//     cout << studentID[1][2] << endl; //6
//     cout << sizeof(studentID) << endl; //4byte * 6 = 24bytes
//     cout << sizeof(studentID[0]) << endl;//4byte * 3 = 12bytes
//     cout << sizeof(studentID[0][0]) << endl; //4byte
//     cout << studentID << endl; //Address of the first row
//     cout << studentID[0] << endl; //Address of the first row
//     cout << studentID[0][0] << endl; //1
//     return 0;
// }
// int main() {   
//     char str[20] = "Hello"; 
//     char str2[] = "World"; //\0 at the end of array ([W][o][r][l][d][\0])
//     cout << strlen(str) << endl;
//     cout << sizeof(str) << endl; // 나머지 요소들은 \0로 채워짐
//     strncat_s(str, str2, 4); //strncat는 str에 str2를 붙이는 함수 (str, str2, 4) -> str에 str2의 4글자를 붙임
//     cout << str << endl;
//     if (strcmp(str, "HelloWorl") == 0) //0: same, -1: different
//         cout << "OK" << endl;
//     else
//         cout << "Fail" << endl;
//     char str01[] = "10";
//     char str02[] = "20";
//     cout << atoi(str01) * atof(str02) << endl; //200 (atoi: string to integer, atof: string to float)

//     cout << strlen(str2) << endl; //5
//     cout << sizeof(str2) << endl; //6 (5 + \0)

//     return 0;
// }

// int main() {


//     // ¡°Hello World¡±, ¡°John¡±
//     char name[] = "John";
//     char name2[] = { 'J', 'o', 'h', 'n' };
//     cout << name[0] << endl;
//     cout << name << endl;
//     cout << "sizeof(name)" << sizeof(name) << endl;
//     cout << "sizeof(name2)" << sizeof(name2) << endl;
  
//     // char name[10];
//     name[0] = 'J';
//     name[1] = 'o';
//     name[2] = 'h';
//     name[3] = 'n';
//     name[4] = '\0'; //end of string
//     cout << name << endl;
    
//     return 0;
// }

/*
void intSwap1(int num1, int num2) {
    int temp{ num1 };
    num1 = num2;
    num2 = temp;
}

void intSwap2(int* num1, int* num2) {
    int temp{ *num1 };
    *num1 = *num2;
    *num2 = temp;
}

int main() {
    int iNum1{ 10 };
    int iNum2{ 30 };
    cout << iNum1 << " " << iNum2 << endl; //10 30
    intSwap1(iNum1, iNum2);
    cout << iNum1 << " " << iNum2 << endl; //10 30
    intSwap2(&iNum1, &iNum2);
    cout << iNum1 << " " << iNum2 << endl; //30 10
    return 0;
}
*/

// int main() {


//     char* name{ 0 };
//     int iNum1 = 10;
//     int* pNum1 = &iNum1;

//     cout << "value:" << iNum1 << endl; //10
//     cout << "its address : " << pNum1 << endl; //address of iNum1
//     *pNum1 = 20;
//     cout << "Pointer Value : " << *pNum1 << endl; //20
//     cout << "Pointer Value : " << iNum1 << endl;  //20
//     cout << "Value: " << &iNum1 << endl;          //address of iNum1
//     cout << "Address of pNum1: " << &pNum1 << endl; //address of pNum1
//     cout << "Address of pNum1: " << &(*pNum1) << endl; //address of iNum1

//     cout << "sizeof(pNum1)" << sizeof(pNum1) << endl; //4bytes (int*)
//     cout << "sizeof(iNum1)" << sizeof(iNum1) << endl; //4bytes (int)

//     //int studentID = 201911999;
//     //cout << "address:" << &studentID << endl;
//     //cout << "value: " << *(&studentID) << endl;

   
//     return 0;
// }



// namespace CIRCLE
// {
//     double PI = 3.14;
//     double calArea(int radius) {
//         double dVal = radius * radius * PI;
//         return dVal;
//     }
//     double calCircumference(int radius) {
//         double dVal = 2 * radius * PI;
//         return dVal;
//     }
// }

// using namespace CIRCLE;

// int main() {
//     //cout << CIRCLE::PI << endl;
//     //cout << CIRCLE::calArea(1) << endl;

//     cout << PI << endl;
//     cout << calArea(1) << endl;
//     return 0;
// }



// double g_count = 0;       // global variable

// void counter() {
//     static int iCount{ 0 }; // static variable initialization (only once)
//     //int iCount{ 0 }; //Local variable
//     iCount++; // static variable update
//     g_count = iCount;
//     cout << iCount << endl;
// }
// int main() {
//     double g_count = 1000; //Local variable
//     int iCount = 10000; //Local variable
//     counter();
//     counter();
//     counter();
//     cout << g_count << endl;
//     cout << iCount << endl; // error
//     return 0;
// }

// long calFact(int = 0); //Default value
// int main() {
    
//     int iVal{ 0 }; long dVal{ 0 };
//     cout << "Enter the number? ";
//     cin >> iVal;

//     dVal = calFact(iVal);
//     cout << dVal << endl;
//     cout << calFact() << endl; //Default value
//     cout << "long" << sizeof(long) << endl;
//     return 0;
    
// }
// long calFact(int num) {
//     if (num == 0) return 1;
//     else return num * calFact(num - 1);
// }

/*
//Function Declaration
double calArea(int);
void main() {
    int iVal(0);    double dVal{ 0 };
    cout << "Enter the radius? ";
    cin >> iVal;
    dVal = calArea(iVal);
    cout << dVal << endl;
    //return 0;
    
}
double calArea(int radius) {
    double dVal;
    dVal = radius * radius * 3.14;
    return dVal;
}
*/