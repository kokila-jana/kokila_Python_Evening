
'''
Types of functions
5 types
1.predefined functions
purple color-->
2.user defined functions
syntax:
def functionName():#function definition
        #block
functionName() #function call

2 types
1.without argument
2.with argument
    4 types
    1.Positional argument
    2.Default argument
    3.variable argument
    4.keyword argument

3.return functions
4.recursive functions
5.lambda function
'''
#without argument
'''def add():
    a=int(input("Enter the number"))
    b=int(input("Enter the number"))
    c=a+b
    print(c)
add()
add()
add()'''

#With argument
#Positional argument
'''def add(a,b):
    c=a+b
    print(c)
add(12,45,47)
add(78,12)'''

'''def withdraw(amount):
    balance=5000
    if amount>balance:
        print("invalid amount")
    else:
        rem_balance=balance-amount
        print(amount,"amount debited.. balance is",rem_balance)
a=int(input("enter amount you want debit"))
withdraw(a)
'''
#default argument
'''def add(a,b=20):
    c=a+b
    print(c)
add(45)
add(10,30)'''

#variable argument
'''def demo(*r):
    print(r)
    for i in r:
        print(i)
demo(12,9.3,956,3+6j,"Hello",False,78,89)
'''

#keyword argument
def demo(**r):
    print(r)
    for i,j in r.items():
        print(i," =",j)
demo(name="Java",year=1995,age=31,author="James Gosling")
