#pragma once
#include <iostream>

void log(const char* message)
{
    std::cout << message << '\n'; 
}

void InitLog()
{
    log("Initializing Log:");
}
