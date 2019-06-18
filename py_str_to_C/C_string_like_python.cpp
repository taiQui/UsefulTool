#include "C_string_like_python.hpp"

pythString::pythString(string attr){
  this->_attr = attr;
}

string pythString::capitalize(){
  string aux = this->_attr;
  if((int)aux[0] >= 97 && (int)aux[0] <= 122){
    aux[0] = char((int)aux[0] -32);
    return aux;
  }
  return aux;
}

string pythString::getAttr(){
  return this->_attr;
}

void pythString::setAttr(string aux){
  this->_attr = aux;
}


string pythString::center(int index,string character){
  string aux = this->_attr;
  int sizeL = (index-aux.size())%2==0?(index-aux.size())/2:((index-aux.size())/2)+1;
  int sizeR = (index-aux.size())%2==0?(index-aux.size())/2:((index-aux.size())/2);
  // cout<<"l "<<sizeL<<endl<<"r "<<sizeR<<endl;
  for(int i = 0; i < sizeL ; i++){
    aux.insert(0,character);
  }
  for(int i = 0; i < sizeR; i++){
    aux.insert(aux.size(),character);
  }
  return aux;
}


int pythString::count(string arg,int s_index,int e_index){
  if(e_index<=0 || e_index > this->_attr.size()) e_index = this->_attr.size();
  if(s_index<=0 || s_index > this->_attr.size()) s_index = 0;
  int count = 0;
  for(int i = s_index; i < e_index;i++){
    if(i+arg.size() <= e_index )
      if(this->_attr.substr(i,arg.size())==arg)
        count++;
  }
  return count;
}

bool pythString::endswith(string arg,int s_index,int e_index){
  if(e_index<= 0 || e_index > this->_attr.size()) e_index = this->_attr.size();
  if(s_index<= 0 || s_index > this->_attr.size()) s_index = 0;
  if(s_index+arg.size() > e_index) {return false;}
  if(e_index < arg.size()) return false;
  return this->_attr.substr(e_index-arg.size(),arg.size()) == arg;
}

bool pythString::startswith(string arg,int s_index,int e_index){
  if(e_index<= 0 || e_index > this->_attr.size()) e_index = this->_attr.size();
  if(s_index<= 0 || s_index > this->_attr.size()) s_index = 0;
  if(s_index+arg.size() > e_index) {return false;}
  if(e_index < arg.size()) return false;
  return this->_attr.substr(s_index,arg.size()) == arg;
}

string pythString::expandtabs(int numberspace){
  string aux = this->_attr;
  string aux2 = "";
  for(int i = 0; i < numberspace ;i++){
    aux2 += " ";
  }
  for(int i = aux.size()-1; i >= 0;i--){
    if(aux[i] == '\t') aux.replace(i,1,aux2);
  }
  return aux;
}

int pythString::find(string arg,int s_index,int e_index){
  if(e_index<=0 || e_index > this->_attr.size()) e_index = this->_attr.size();
  if(s_index<=0 || s_index > this->_attr.size()) s_index = 0;
  for(int i = s_index; i < e_index;i++){
    if(i+arg.size() <= e_index )
      if(this->_attr.substr(i,arg.size())==arg)
        return(i);
  }
  return -1;
}

bool pythString::isalnum(){
  for(int i = 0; i < this->_attr.size() ;i++){
    if( !(((int)this->_attr[i]>= 48 && (int)this->_attr[i]<=57) || ((int)this->_attr[i]>=65 && (int)this->_attr[i]<=90) || ((int)this->_attr[i]>=97 && (int)this->_attr[i]<=122)) )
      return false;
  }
  return true;
}

bool pythString::isalpha(){
  for(int i = 0; i < this->_attr.size() ;i++){
    if( !(((int)this->_attr[i]>=65 && (int)this->_attr[i]<=90) || ((int)this->_attr[i]>=97 && (int)this->_attr[i]<=122)) )
      return false;
  }
  return true;
}

bool pythString::isdigit(){
  for(int i = 0; i < this->_attr.size() ;i++){
    if( !((int)this->_attr[i]>= 48 && (int)this->_attr[i]<=57) )
      return false;
  }
  return true;
}

bool pythString::islower(){
  for(int i = 0; i < this->_attr.size() ;i++){
    if( !( ((int)this->_attr[i]>=97 && (int)this->_attr[i]<=122)) )
      return false;
  }
  return true;
}

bool pythString::isupper(){
  for(int i = 0; i < this->_attr.size() ;i++){
    if( !(((int)this->_attr[i]>=65 && (int)this->_attr[i]<=90) ) )
      return false;
  }
  return true;
}

bool pythString::isspace(){
  for(int i = 0; i < this->_attr.size() ;i++){
    if( ((int)this->_attr[i] != 32) )
      return false;
  }
  return true;
}

bool pythString::istitle(){
  vector<string> aux = this->split(" ");
  bool title = true;
  for(int i = 0; i < aux.size(); i++){
    bool good = false;
    for(int j = 0 ; j < aux[i].size() ; j++){
      if((((int)aux[i][j] >= 65 && (int)aux[i][j] <= 90) || ((int)aux[i][j]>=97) && (int)aux[i][j]<=122 )) {
        if((int)aux[i][j]>=65 && (int)aux[i][j]<= 90){
          if(good)
            return false;
          good = true;
        } else{
          if(!good)
            return false;
        }
      }
    }
  }
  return title;
}

string pythString::join(string arg[],int size){
  string aux = "";
  for(int i = 0; i < size-1; i++){
    aux+= arg[i]+this->_attr;
  }
  aux+= arg[size-1];
  return aux;
}
//len
int pythString::size() { return this->_attr.size();}

string pythString::ljust(int size,string arg){
  if(size < this->_attr.size()) { return this->_attr;}
  string aux = this->_attr;
  for(int i = this->_attr.size() ; i < size ;i++){
    aux += arg;
  }
  return aux;
}

string pythString::rjust(int size,string arg){
  if(size < this->_attr.size()) { return this->_attr;}
  string aux = this->_attr;
  for(int i = this->_attr.size() ; i < size ;i++){
    aux = arg+aux;
  }
  return aux;
}

string pythString::lower(){
  string aux = this->_attr;
  for(int i =0 ; i < aux.size() ; i++){
    if((int)aux[i] >= 65 && (int)aux[i]<=90 )
      aux[i] = char( (int)aux[i] + 32 );
  }
  return aux;
}

string pythString::upper(){
  string aux = this->_attr;
  for(int i = 0; i < aux.size() ;i++){
    if((int)aux[i] >= 97 && (int)aux[i]<= 122)
      aux[i] = char( (int)aux[i] - 32);
  }
  return aux;
}

string pythString::switchcase(){
  string aux = this->_attr;
  for(int i = 0; i < aux.size() ; i++){
    if((int)aux[i]>=65 && (int)aux[i]<=90){
      aux[i] = char((int)aux[i] +32);
    } else if((int)aux[i]>= 97 && (int)aux[i]<= 122){
      aux[i] = char((int)aux[i] -32);
    }
  }
  return aux;
}

string pythString::lstrip(string seq){
  string aux = this->_attr;
  int i = 0;
  while( i < aux.size()){
    if(aux.substr(i,1) == seq)
      aux = aux.substr(i+1);
    else return aux;
  }
  return aux;
}

string pythString::rstrip(string seq){
  string aux = this->_attr;
  int i = aux.size()-1;
  while( i >= 0 ){
    if(aux.substr(i,1) == seq){
      aux = aux.substr(0,i);
      i--;
    } else return aux;
  }
  return aux;
}

string pythString::strip(string seq){
  string aux = this->_attr;
  this->_attr = this->lstrip(seq);
  this->_attr = this->rstrip(seq);
  string aux2 = this->_attr;
  this->_attr = aux;
  return aux2;
}


string pythString::to_l33t(string alpha,string transl){
  if(alpha.size() != transl.size()) { return "-1" ;}
  string aux = this->_attr;
  for(int i = 0; i < alpha.size() ; i++)
    if(aux.find(alpha[i]) != string::npos)
      for(int j = 0 ; j < aux.size() ; j++ )
        if(aux[j] == alpha[i])
          aux[j] = transl[i];
  return aux;
}

string pythString::max(){
  int max = (int)this->_attr[0];
  int nmax = 0;
  for(int i = 1; i < this->_attr.size() ; i++){
    if(max < (int)this->_attr[i]){
      max = (int)this->_attr[i];
      nmax = i;
    }
  }
  return this->_attr.substr(nmax,1);
}

string pythString::min(){
  int min = (int)this->_attr[0];
  int nmin = 0;
  for(int i = 0 ; i < this->_attr.size(); i++){
    if( min > (int)this->_attr[i]){
      min = (int)this->_attr[i];
      nmin = i;
    }
  }
  return this->_attr.substr(nmin,1);
}

string pythString::replace(string old,string rep, int nb){
  bool inf = false;
  if(nb == 0 ) inf =true;
  string aux = this->_attr;
  int i = 0;
  for(int j = aux.size() -1 ; j >= 0 ; j--){
    if(!inf)
      if( i > nb ) break;
    if(j+old.size() < aux.size())
      if(aux.substr(j,old.size()) == old)
        aux = aux.substr(0,j)+rep+aux.substr(j+old.size());
        i++;
  }
  return aux;
}

vector<string> pythString::split(string sep,int number){
  int i = 0;
  vector<string> aux;
  string tmp = "";
  for(int j = 0; j < this->_attr.size() ;j++){
    if(this->_attr.substr(j,1) != sep)
      tmp += this->_attr[j];
    else {
      if(number != 0)
        if(i < number){
          i++;
          aux.push_back(tmp);
          tmp = "";
        } else {
          tmp += this->_attr[j];
        }
      else{
        aux.push_back(tmp);
        tmp = "";
      }
    }


  }
  if(!tmp.empty()) aux.push_back(tmp);
  return aux;
}

vector<string> pythString::splitline(int number){
  int i = 0;
  vector<string> aux;
  string sep = "\n";
  string tmp = "";
  for(int j = 0; j < this->_attr.size() ;j++){
    if(this->_attr.substr(j,1) != sep)
      tmp += this->_attr[j];
    else {
      if(number != 0)
        if(i < number){
          i++;
          tmp+="\n";
          aux.push_back(tmp);
          tmp = "";
        } else {
          tmp += this->_attr[j];
        }
      else{
        aux.push_back(tmp);
        tmp = "";
      }
    }


  }
  if(!tmp.empty()) aux.push_back(tmp);
  return aux;

}

string pythString::zfill(int number){
  string aux = this->_attr;
  int size = number - aux.size();
  for(int i = 0 ; i < size ; i++){
    aux = '0'+aux;
  }
  return aux;
}

string pythString::title(){
  vector<string> aux = this->split(" ");
  for(int i = 0; i < aux.size(); i++){
    bool first = true;
    for(int j = 0; j < aux[i].size(); j++){
      if(((int)aux[i][j]>=65 && (int)aux[i][j]<= 90)){
        if(first) first = false;
        else{
          aux[i][j] = char((int)aux[i][j]+32);
        }
      } else if((int)aux[i][j]>= 97 && (int)aux[i][j] <= 122){
        if(first){
          aux[i][j] = char((int)aux[i][j] -32);
          first =false;
        }
      }
    }
  }
  string temp = "";
  for(int i =0; i < aux.size()-1; i++){
    temp+= aux[i]+" ";
  }
  return temp+aux[aux.size()-1];
}

// OPERATOR REDEFINITION
void pythString::operator=(const pythString& equal){
  this->_attr = equal._attr;
}

char& pythString::operator[](int index) {
    if(index < 0 || index > this->_attr.size() ){
      throw out_of_range("Operator[] - Bad index - out_of_range");
    }
    return this->_attr[index];
}

pythString pythString::operator+=(const pythString& sup){
  string aux = this->_attr;
  aux+= sup._attr;
  return aux;
}
