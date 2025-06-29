# 1. In-Build Function

int()
str()
bool()

# 2. Module Function
# Module : it refers a file where related functions and variable are stored 
import math # here math is a module 
print(dir(math))  # '__doc__', '__loader__', these all are math module func

from math import sqrt
print(sqrt(16))  # sqrt is a Module Function

# from math import *  // here * means all functions 

# 3. User Defined Function
# def function_name(parameters):
#      do something

def print_sum(a,b):
    print(int(a)+int(b)) # as take input as string so we convert it to integer

first = input("Enter first num: ")
second = input("Enter 2nd num: ")

print_sum(first,second)
