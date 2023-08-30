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

  while(f.get(letter)){ //f.eof()){
    //f.get(letter); 
    //why does "char letter" need to be a pointer in order for get to function?
    //resolved: see following link: https://cplusplus.com/forum/beginner/205483/ //silly.
    cout << letter << endl;
  }

}