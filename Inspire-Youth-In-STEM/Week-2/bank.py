#write a program that calculates 16% tax on income 
#ranging btwn 100k - 150k

#19% tax income is btwn 150k- 300k
#30% tax income is above 300k
#5% tax if income is less than 100k

# print gross income and net income
income = input("Enter your net income:")

Gross_income = int(input("What is your gross income:"))
Tax_group_1 = (Gross_income * 0.05 )
Tax_group_2 = (Gross_income * 0.16)
Tax_group_3 = (Gross_income * 0.19)
Tax_group_4 = (Gross_income * 0.3)

if Gross_income <= 100000:
    print("Gross_income:", Gross_income)
    print("Net income:",Gross_income - Tax_group_1)
elif Gross_income >= 100001 & (Gross_income < 150000):
    print("Gross_income:", Gross_income)
    print("Net income:", Gross_income - Tax_group_2)
elif(Gross_income <=150001) & (Gross_income <= 300000):
    print("Gross_income:", Gross_income)
    print("Net income:",Gross_income - Tax_group_3)
elif Gross_income > 300000:
    print("Gross_income:", Gross_income)
    print("Net income:", Gross_income - Tax_group_4)