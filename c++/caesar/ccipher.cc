#include <iostream>
#include <fstream>
#include <cstdint>
//#include <istream>
#include <string>

using namespace std;

int main(int argc, char* argv[]){
  string filename = argv[1];
  fstream f(filename);
  uint8_t shiftIndex = 1;
  char letter;
  //int n = 0;

  while(f){
    f.get(letter); //why does "char letter" need to be a pointer in order for get to function?
    cout << letter;
  }

}