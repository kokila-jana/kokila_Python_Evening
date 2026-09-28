'''print('Hello')
a=10
a=20
#print(a)
a154485=100
jhbv=78
i=74
max_num=1000'''
'''a1=78
print(a1)'''
'''a=10
b=12.36
c=True
d="hello"
print(type(a))
print(type(b))
print(type(c))
print(type(d))'''

'''a=int(input("Enter"))
b=int(input("enter"))
c=a+b
print(c)'''

'''a=float(input("Enter"))
b=float(input("enter"))
c=a+b
print(c)'''
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
'''a=int(input("Enter the number"))
count=0
for i in range(1,a+1):
    if a%i==0:
       count+=1
print(count)

if count==2:
    print("Prime number")
else:
    print("not prime number")
'''


'''
while loop sytax
initialization-->start
while  condition:-->stop
        #block
        inc/dec-->step
'''
#while loop using increment
'''a=1
while a<11:
    print(a)
    a+=1
'''

#while loop using decrement
'''a=10
while a>0:
    print(a)
    a-=1
'''

#while loop using inifinity
'''a=1
while True:
    print(a)
    a-=1'''
'''
a=1    a=a-1=>1-1=>0
a=0    a=0-1'''

#while loop using inifinity
'''a=1
while a<=10:
    print(a)'''
'''
a=1   1<=10   1
a=1   1<=10   1
'''
'''a=1
while a<11:
    print(a)
    a+=1'''
'''
a=1   1<11   1    a=1+1=>2
a=2   2<11   2    a=2+1=>3
.
.
.
a=10  10<11    10   10+1=11
a=11  11<11(False)
'''
#Factorial using while loop
'''5-->5*4*3*2*1-->120'''
'''a=int(input("Enter the number"))
fact=1
i=1
while i<=a:
    fact*=i
    i+=1
print(fact)'''

#To reverse a number...
'''
123-->321
'''
'''a=121
b=0
while a>0:
    c=a%10
    b=b*10+c
    a=a//10
print(b)'''
'''
a=123
b=0

1)123>0
c=123%10-->c=3
b=0*10+3-->b=3
a=123//10-->a=12

2) 12>0
c=12%10-->c=2
b=3*10+2-->b=32
a=12//10-->a=1

3)1>0
c=1%10-->c=1
b=32*10+1-->b=321
a=1//10-->a=0

4)0>0(False)

'''
#Palindrome
'''a=int(input("Enter the number"))
x=a
b=0
while a>0:
    c=a%10
    b=b*10+c
    a=a//10
print(b)
if b==x:
    print("Palindrome ")
else:
    print("not Palindrome")
'''
#Armstrong number
'''153 -->3
3^3+  5^3+  1^3-->27+125+1-->153'''
#to count the digits
'''a=int(input("Enter"))
x=a
y=a
count=0
while a>0:
    count+=1
    a=a//10
print(count)

res=0
while x>0:
    c=x%10
    res=res+c**count
    x=x//10
print(res)
if res==y:
    print("Armstrong number")
else:
    print("not Armstrong number")'''
'''
res=0
x=153
1)153>0
 c=153%10-->c=3
 res=0+3**3-->res=27
 x=153//10-->x=15
2)15>0
  c=15%10-->c=5
  res=27+5**3-->res=152
  x=15//10-->x=1
3)1>0
   c=1%10-->c=1
   res=152+1**3-->res=153
   x=1//10-->x=0
'''
'''
a=153
count=0
1)153>0
   count=0+1-->count=1
   a=153//10-->a=15
2)15>0
  count=1+1=2
  a=15//10-->a=1
3)1>0
   count=3
   a=1//10-->a=0
'''
#Jumping/transfer statements
'''
1.break
2.continue
3.pass
'''
'''for i in range(1,11):
    print(i)
    if i==5:
        break'''
'''for i in range(1,11):
    if i==5:
        continue
    print(i)'''

'''for i in range(1,11):
    if i%2==0:
        print("hello")
        continue
    print(i)
'''
'''for i in range(1,31):
    if i%3==0 and i%5==0:
        print("hi hello")       
        continue
    elif i%5==0:
        print("hello")
        continue
    elif i%3==0 :
         print("hii")
         continue
    print(i)
'''
'''a=int(input("Enter"))
if a>=18:
    print("Eligible")
else:
    pass
    print("not eligible")'''

'''a="Hello Java"
print(a[2])
print(a[9])
print(a[-1])
print(a[-5])
print(a[0:5])
print(a[6:])
print(a[:4])
print(a[-8:-4])
print(a[::-1]) #reverse a string
'''
'''
H  e   l   l   o       J  a  v  a
0   1  2  3  4  5  6  7  8  9
-->forward indexing

-10   -9  -8  -7  -6  -5  -4  -3   -2   -1
H      e     l    l    o         J     a    v    a
<--backward indexing

a.length=10
index=length-1
index=9
'''
'''a="hello"
print(a)
print(a.capitalize())
print(a.center(10))
print(a.count('l'))
print(a.endswith('lo'))
print(a.find('l'))
print(a.index('o'))
b="java"
c="123"
print(c.isalnum())
print(b.isalpha())
print(c.isdecimal())
print(c.isdigit())
print(c.isnumeric())
print(b.isascii())
d='1'
print(d.isidentifier())
print(a.islower())
e=" "
print(e.isspace())
f="Hii I am Fullstack Developer"
print(f.istitle())
g="JAVA"
print(g.isupper())
print(g.lower())
print(g.replace('A','E'))
print(a.rfind('l'))
print(a.rindex('l'))
'''
'''h  e  l   l  o
0  1  2  3  4'''
'''
print(f.split(" "))
x=f.split(" ")
for i in x:
    print(i)
h="Hello\nPython\nJava\ncpp"
print(h.splitlines())
print(a.startswith('h'))
i="           Java        "
print(i.strip())
print(i.lstrip())
print(i.rstrip())
j="HEllo"
print(j.swapcase())
k="hi i am python developer"
print(k.title())
print(a.upper())
print(a.zfill(10))
print("@".join(a))
'''
'''a=input("Enter the string")
b=""
for i in a:
    b=i+b
print(b)
if a==b:
    print("Palindrome")
else:
    print("Not Palindrome")'''
'''
1)b=J+""-->b=J
2)b=a+J-->b=aJ
3)b=v+aJ-->b=vaJ
4)b=a+vaJ-->b=avaJ
'''








