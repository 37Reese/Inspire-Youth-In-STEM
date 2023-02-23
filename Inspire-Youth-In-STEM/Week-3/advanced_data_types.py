#!/usr/bin/env python3
# This is a single line comment
# Dta types
# Name : Cyril Newman
# Email : reesedugg24@gmail.com
# Date : 22nd Feb 2023
# File : advanced data types

# Mutable vs immutable

#Mutable are data types that can change / edited during the program life cycle
# add / remove elements

#Immutable --> Data types that cannot be edited during program life cycle

# 1) List (mutable)

friends = ["Reese","Neema","Keke","Masese"]
#        or [ ] for empty list
# add ---> append() or extend()

students = ["Prince","Cyril","Sammy"]
friends.extend(students)
friends.append("Rubadiri")
friends.sort()
friends.pop(2)
print(friends)

# 2) Tuples (immutables)
stationeries = ("Pens","pencils","rubber","stapler","ink")

# Repalce the whole tuple
stationeries = ("ruler","clip board","eraser")
for stationery in stationeries:
    print(stationery)

# 3) Dictionaries

# Use key and value pair

student = {"Name" : "Reese", "age" : 24 , "Gender":"Male", "is tall":"true"}
print(student["Gender"])
print(student["age"])
print(student["Name"])
print(student["is tall"])
# "Name" : "Reese" --> Name(key) , Reese(Value)
# Create a dictionary
# Name it friend

friend = {"fav colour" : "Royal blue", "Hobby":"Listening to music","course":"Computer science","weight":67 ,"height": 171}
print(friend["fav colour"])
print(friend["Hobby"])
print(friend["course"])
print(friend["weight"])
print(friend["height"])

print(friend.values())
print(friend.keys())

# 4) Sets
#_____________________________________
# # a) Ordered--> similar data types
#_____________________________________

# b) Non ordered--> Different data types
#-------------------------------------

#uses curly brackets( {} )
my_fruits = {"banana","cherry","apple","orange"}
for fruit in my_fruits:
    print(type(fruit))