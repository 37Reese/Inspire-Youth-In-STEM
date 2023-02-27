#!/usr/bin/env python3
# This is a single line comment
# Python program to illustrate operators
# Name : Cyril Newman
# Email : reesedugg24@gmail.com
# Date : 27th Feb 2023
# File : Files.py

#exception handling

filename = 'C:\\Users\\user\\Documents\\Inspire-Youth-In-STEM\\Week-4\\test.txt','r+w'
f = open(filename,'r+w',encoding=None)
print(f.readlines())
try:
    for file in filename:
        with open(filename , 'r+w',encoding = None) as f_obj:
             contents = f_obj.read()
             print(contents)
except FileNotFoundError:
    msg = "Sorry, the file" + filename + "does not exist"
print(msg)

filename = ("C:\\Users\\user\\Documents\\Inspire-Youth-In-STEM\\Week-4\\test.txt','r+w+a'")
f = open(filename,'r+w')
print(f.readlines())
