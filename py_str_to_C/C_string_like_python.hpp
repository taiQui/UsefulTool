#ifndef C_string
#define C_string

#include <string>
#include <iostream>
#include <vector>
using namespace std;

class pythString {

private:
  string _attr;

public:
  pythString(string);
  string getAttr();
  friend ostream& operator<<(ostream& os,const pythString& attr){
    return os<<attr._attr;
  }
  void setAttr(string);
  string capitalize();
  string center(int,string);
  int getSize(){return this->_attr.size();}
  int count(string,int= 0,int=0);
  //encode
  //decode
  bool endswith(string,int = 0,int=0);
  bool startswith(string,int=0,int=0);
  string expandtabs(int=8);
  int find(string,int=0,int=0);
  bool isalnum();
  bool isalpha();
  bool isdigit();
  bool islower();
  bool isupper();
  bool isspace();
  bool istitle();  // A FAIRE QUAND J'AURAI FAIS SPLIT
  string join(string[],int);
  int size();
  string ljust(int,string);
  string rjust(int,string);
  string lower();
  string upper();
  string switchcase();
  string lstrip(string=" ");
  string rstrip(string=" ");
  string strip(string=" ");
  string to_l33t(string="aeiost",string="431057");
  string max();
  string min();
  string replace(string,string,int=0);
  vector<string> split(string,int=0);
  vector<string> splitline(int=0);
  string zfill(int);
  string title();
};

#endif
