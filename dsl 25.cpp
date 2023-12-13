#include<iostream>
#include<stack>
#include<cctype>

using namespace std;

void printReverse(string str) {
    stack<char> Stack;

    for (int i =0; i<str.length(); i++) {
        Stack.push(str[i]);
    }

    for (int i =0; i<str.length(); i++) {
        cout << Stack.top();
        Stack.pop();
    }
}

bool isPalindrome(string str) {
    int start =0;
    int end =str.length() -1;

    while (start < end) {
        if (tolower(str[start]) !=tolower(str[end])) {
            return false;
        }
        start++;
        end--;
    }
    return true;
}

int main() {
    string str ="Poor Dan is in a droop";
    cout <<"Original string: "<< str << endl;
    printReverse(str);
    cout <<"Entered string is "<< (isPalindrome(str) ?"a palindrome":"not a palindrome") << endl;
    return 0;
}