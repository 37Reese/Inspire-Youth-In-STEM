#!/usr/bin/env python3
# This is a single line comment
# Using setters and getters
# Name : Cyril Newman
# Email : reesedugg24@gmail.com
# Date : 27th Feb 2023
# File : cars.py


class car:
    def _init_(self,model,make,year_of_manufacture,engine_capacity):
       self.model = model
       self.make = make
       self.year_of_manufacture = year_of_manufacture
       self.engine_capacity = engine_capacity

    
    def get_model(self):
        return self.model
    
    def get_make(self):
        return self.make
    
    def get_year(self):
        return self.year_of_manufacture
    
    def get_engine_capacity(self):
        return self.engine_capacity
    
    #setters : set the attributes
def set_model(self,model):
    set.model = model

def set_make(self,make):
    set.make = make

def set_year(self,year):
    set.year = year

def set_engine_capacity(self,engine_capacity):
    set.engine.capacity = engine_capacity

    

Car1 = car("supra","toyota",1997,30000)
Car2 = car("skyline","nissan",2006,25000)
Car3 = car("GTR","nissan",2002,27000)

Car3.set_year(2045)
Car2.set_model("Chiron")
print(Car1.get_model())
print(Car1.get_year())

print(Car2.get_model())
print(Car3.get_year())    
    

