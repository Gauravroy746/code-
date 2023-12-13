#include<iostream>
#include<string.h>
#include<stdlib.h>
using namespace std;
class stack
{
 char stk[10]; 
 int top;
 int flag;
 public:
  stack()
 {
   top=-1;
   flag=0;
 }

 int push(char x)
 {
  top=top+1;
   stk[top]=x;
   cout<<"Inserted "<<x<<"\n";
 }

 int pop(char x)
 {
  if(x=='}')
  {
   if(stk[top]=='{')
    {
     cout<<"Deleted '{'\n";
     top=top-1;
    }
    else
    {
     flag=1;
    }
  }  
  if(x==')')
  {
   if(stk[top]=='(')
    {
     cout<<"Deleted '('\n";
     top=top-1;
    }
    else
    {
     flag=1;
    }
  }  
  if(x==']')
  {
   if(stk[top]=='[')
    {
     cout<<"Deleted '['\n";
     top=top-1;
    }
    else
    {
     flag=1;
    }
  }  
 }

 void display()
 {
   if( top!=-1 || flag==1 )
   {
    cout<<"\nThe Expression is not Well Parantesis\n";
   }
   else
   {
   cout<<"\nThe Expression is Well Parantesis\n";
   }
 }
};

int main()
{
 stack st;
 int j;
 char str[20];
 cout<<"Enter the Characters you want to enter\n";
 cin>>str;
 int len=strlen(str);
 for(int m=0;m<len;m++)
 {
  if(str[m]=='{'|| str[m]=='(' || str[m]=='[')
  {
   char x;
   x=str[m];
   st.push(x);
  }  
  if(str[m]=='}'|| str[m]==')' || str[m]==']')
  {
   char x;
   x=str[m];
   st.pop(x);    
  }  
 }
  st.display();
}