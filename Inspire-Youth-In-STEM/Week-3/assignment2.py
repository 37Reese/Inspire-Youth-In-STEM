#!/usr/bin/env python3
# This is a single line comment
# assignment
# Name : Cyril Newman
# Email : reesedugg24@gmail.com
# Date : 21st Feb 2023
# File : assignment.py


#Write a problem that solves quadratic equation
# Using for loop draw a diamond 
# Draw a triangle


# y = 6x^2 + 3x + 9
'''
for x in range(0,10):
    print("(x) :" +str(x)+ "6x^2 + 3x + 9 =",str(6*(x**2) + (3*x) + 9)  )
'''
h = eval(input("Enter diamond's height: "))
for x in range(h):
    print(" " * (h - x), "*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2*x + 1))