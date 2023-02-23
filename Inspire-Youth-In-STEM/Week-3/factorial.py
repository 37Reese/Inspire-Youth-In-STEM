#Write a program to print the factorial of a number using 
#Wrire a program to calculate simple interest
def factorial(n):
    for i in range(0,n):
        fact_n = n * (n-i)
        return fact_n

print(factorial(5))