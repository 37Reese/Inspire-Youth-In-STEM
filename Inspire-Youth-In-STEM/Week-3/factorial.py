#Write a program to print the factorial of a number using def factorial
#Wrire a program to calculate simple interest

def factorial(n):
    for i in range(0,n):
        fact_n = n * (n-i)
        return fact_n

print(factorial(5))


def simple_interest(p,t,r):
    print("The principle is:",p)
    print("The time is:",t)
    print("The rate of interest is:",r)

    simp_int = (p * t* r)/100

    print("The simple interest")

    return simp_int

#Driver code
simple_interest(80000,60000,800000)

