#include<iostream>
#include<string.h>
using namespace std;
int main() {
   char m[25] = "My name is Gaurav";
   string str;
   int i;
   for(i=0;i<sizeof(m);i++) {
      str[i] = m[i];
      cout<<str[i];
   }
   return 0;
}