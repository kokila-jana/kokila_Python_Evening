'''
control statements
 to control the flow of the program
 4 types
 1.Sequential statements-->to execute the program line by line
 2.Selectional/conditional statements
     4 types
     1.if  syntax
     if  condition:
         #block of code
     
     2.if-else
     if condition:
         #block
     else:
         #block
     3.if elif else
     4.nested if
 3.Loop/Iterative statements
 4.Jumping/Transfer statements
 '''
'''a=int(input("Enter the number..."))
b=int(input("Enter the number..."))
if a>b:
    print("a is big...")'''

'''a=int(input("Enter the number..."))
if a==1234:
    print("valid PIN")
else:
    print("invalid PIN")'''

#Buzz number...
'''a=int(input("Enter the number..."))
if a%10==7  or  a%7==0:
    print("Buzz number")
else:
    print("not Buzz number")
'''

'''
Types of loop
Entry checked loop
  2 types
  1.for  loop-->Countable loop
  2.while loop-->inifinity loop
Exit checked loop
do-while-->not support in python

for loop syntax
for variable in range(start,stop,step):
        #block
1.start
2.stop-->condition
3.block
4.step

1.for loop using increment-->stop-1
2.decrement-->stop+1
'''
'''for i in range(1,11,1):
    print(i)'''

'''
   1         2          3          4
   i=1   1<11      1         1+1=2
   i=2   2<11      2         2+1=3
   .
   .
   .
   i=10  10<11   10       10+1=11
   i=11   11<11(False)'''

'''for i in range(10,0,-1):
    print(i)'''

'''for i in range(1,11):
    print(i)'''

'''for i in range(11):
    print(i)'''

'''for i in "Python":
    print(i)
'''

# to sum of first 10 numbers
'''add=0
for i in range(1,11):
    add+=i
print(add)'''

#to multiple first 5 numbers
'''mul=1
for i in range(1,6):
    mul*=i
    print(mul)
'''

#to find Factorial of the given number
'''a=int(input("enter the number"))
mul=1
for i in range(1,a+1):
    mul*=i
print(mul)'''

#to find the divisors of given number
'''a=int(input("Enter the number"))
for i in range(1,a+1):
    if a%i==0:
        print(i)'''

#count the divisors
'''a=int(input("Enter the number"))
count=0
for i in range(1,a+1):
    if a%i==0:
       count+=1
print(count)
'''

#to find the sum of the divisors
'''a=int(input("Enter the number"))
add=0
for i in range(1,a+1):
    if a%i==0:
       add+=i
print(add)'''

#Prime number or not
a=int(input("Enter the number"))
count=0
for i in range(1,a+1):
    if a%i==0:
       count+=1
print(count)

if count==2:
    print("Prime number")
else:
    print("not prime number")
