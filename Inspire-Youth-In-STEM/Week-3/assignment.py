#!/usr/bin/env python3
# This is a single line comment
# Create an empty list of favourite musicians
# Using for loop add 5 new musicians
# copy the list ta new list called celebs
# sort the list
# pop out two celebs from the list
# Count the remaining celebs in the list
# Name : Cyril Newman
# Email : reesedugg24@gmail.com
# Date : 20th Feb 2023
# File : assignment.py

favouriteArtists = []
r = int(input("Enter the number of your favouriteArtists:"))
for i in range(0,r):
    elem= input("Enter the names of the favouriteArtists:")
    favouriteArtists.append(elem)
print("The names of the favouriteArtists",favouriteArtists)
celebs = favouriteArtists.copy()
print(celebs)
celebs.sort()
print(celebs)
celebs.pop(3)
print(celebs)
celebs.pop(0)
print(celebs)
print(len(celebs))