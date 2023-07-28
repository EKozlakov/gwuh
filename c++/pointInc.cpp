
/*

Trying to answer a question: what happens if you increment a pointer?

*/

#include <iostream>
#include <cstdint>
#include <iomanip>

using namespace std;

int main(){
  uint32_t a = 32;
  uint32_t* p = &a; //initializing pointer to address of a.
  int i = 0;

  while(true){
    //cout << setw(6);
    //cout << setw(18);
    cout << "a: "<<  a << ", ";

    cout << "*p: " << setw(12) << *p << ", "; 
    //cout << setw(18);

    cout << "address: " << p << ", " << endl;

    p++;
    i++;
    if (i > 30){
      break;
    }
  }

}