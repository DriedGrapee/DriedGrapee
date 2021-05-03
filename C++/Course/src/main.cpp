#include <iostream>
#include "Log.h"

int main()
{
    int x = 5;
    if(x==5)
    {
       log("Home");     
    }
    log("Hello World!");
    std::cin.get();
    return 0;
}