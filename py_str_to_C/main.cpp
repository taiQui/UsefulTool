#include <iostream>
#include "C_string_like_python.hpp"

int main(){
  pythString* a = new pythString("BoNjOUr YoLLo mAMENE");
  pythString* b = new pythString("pute");

  cout<<(*a)+(*b)<<endl;
}
