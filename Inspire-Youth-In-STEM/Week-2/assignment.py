#Write a programme to list all the odd numbers from 1-100
#Write all the even numbers from 1-100
#Write all the prime numbers from 1-97
#Write a programme to calculate arithmetic proression of numbers 1-100

def listAddNumbers(minValue=0, maxValue=100):
    for x in range(minValue,maxValue):
        if(x %2 != 0): print(x)
