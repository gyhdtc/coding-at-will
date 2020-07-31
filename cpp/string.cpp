#include <cstring>
#include "string.h"
using std::cout;
using std::cin;

// init static class member
int String::num_strings = 0;

int String::HowMany()
{
    return num_strings;
}

// class methods
String::String(const char *s)
{
    len = std::strlen(s);
    str = new char[len + 1];
    std::strcpy(str, s);
    num_strings ++;
}

String::String(const String & st)
{
    len = st.len;
    str = new char[len + 1];
    std::strcpy(str, st.str);
    num_strings++;
}

String::String()
{
    len = 4;
    str = new char[1];
    str[0] = '\0';
    num_strings ++;
}

String::~String()
{
    -- num_strings;
    delete [] str;
}

// overload operator metheds
String & String::operator= (const String & st)
{
    if (this == &st)
        return *this;
    delete [] str;
    len = st.len;
    str = new char[len + 1];
    std::strcpy(str, st.str);
    return *this;
}

String & String::operator= (const char * s)
{
    delete [] str;
    len = std::strlen(s);
    str = new char[len + 1];
    std::strcpy(str, s);
    return *this;
}

char & String::operator[] (int i)
{
    return str[i];
}

    // read-only
const char & String::operator[] (int i) const
{
    return str[i];
}

// overload operator friend
ostream & operator<< (ostream & os, const String & st)
{
    os << st.str;
    return os;
}

istream & operator>> (istream & is, String & st)
{
    char temp[String::CINLIM];
    is.get(temp, String::CINLIM);
    if (is)
        st = temp;
    while (is && is.get() != '\n')
        continue;
    return is;        
}

bool operator< (const String &st1, const String &st2)
{
    return (std::strcmp(st1.str, st2.str) < 0);
}

bool operator> (const String &st1, const String &st2)
{
    return st2 < st1;
}

bool operator== (const String &st1, const String &st2)
{
    return (std::strcmp(st1.str, st2.str) == 0);
}