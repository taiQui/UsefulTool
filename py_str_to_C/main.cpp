#include <iostream>
#include "C_string_like_python.hpp"

int main(){
  pythString* a = new pythString("BoNjOUr YoLLo mAMENE");
  pythString* b = new pythString("pute");
  pythString c ("HAB");
  pythString d ("UIP");
  c = *a;
  try{
    cout<<c[-1]<<endl;
  }catch(std::out_of_range& e){
    cout << e.what() <<endl;
  }
}
