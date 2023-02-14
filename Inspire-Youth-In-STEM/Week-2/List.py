names=["Reese","Dugg","Your","Neema","Jeff"]
#Accessing items in a list
print(names)
print(names[0])
print(names[-1])
print(names[2])
print(names[0:3])
Fruits=["mango","apples","peaches","watermelon","pomegranade","banana","guava"]
print(Fruits[0:-1])
print(Fruits[3])
print("my favourite fruit is:",Fruits[2])
print("my favourite fruit is:",Fruits[3].upper())

# Adding two lists
vegetables=["Kales","cabbage","managu","carrots","tulips","brocolli"]
stationery=["pens","ink","paper","sciccors","stapler","ruler"]
shoppings=vegetables + stationery
print(shoppings)
print(shoppings[5])
for vegetable in vegetables:
    print(vegetable)
for shopping in shoppings:
    print(shopping)
    print("my name is " + names[0]+ " and my favourite fruit is " +Fruits[2])