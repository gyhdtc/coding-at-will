#ifndef STRING_H_
#define STRING_H_
#include <iostream>
using std::ostream;
using std::istream;
class String
{
private:
    char * str;
    int len;
    static int num_strings;
public:
    static const int CINLIM = 80;
    // constructors and other methods
    String(const char * s);
    String(const String &);
    String();
    ~String();
    int length() const { return len; }
    // overload operator metheds
    String & operator= (const String &);
    String & operator= (const char *);
    char & operator[] (int i);
    const char & operator[] (int i) const;
    // overload operator friends
    friend ostream & operator<< (ostream & os, const String & st);
    friend istream & operator>> (istream & is, const String & st);
    friend bool operator< (const String &st1, const String &st2);
    friend bool operator> (const String &st1, const String &st2);
    friend bool operator== (const String &st1, const String &st2);
    // static function
    static int HowMany();
};
#endif