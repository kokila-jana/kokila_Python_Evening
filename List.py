
'''a=10
a=45
a="hello"
a=3.14
print(a)

b=[10,45,"hello",3.14]
print(b)'''
'''[]-->list
()-->tuple
{}-->set
{key:value}-->dict'''

'''a=[12,3.14,"hello",False,12+3j,3.14]
b=45
print(type(a))
print(a)
print(a[3])
print(a[-2])
c=[123,6,9,[45,9,8,6],48]
print(c)
print(c[-2][-2])
print(c[3][2])'''

'''a=[12,3.14,"hello",False,12+3j,3.14]
print(a)
a.append(85)
print(a)
b=a.copy()
print(b)
print(a.count(3.14))
print(a.index(3.14))
a.insert(2,'k')
print(a)
a.pop()
print(a)
a.remove(3.14)
print(a)
a.reverse()
print(a)
c=[1,2,3,6]
a.extend(c)
print(a)
a.clear()
print(a)
d=[4,5,93,1,3,6]
d.sort()
print(d)
'''
'''a=[12,3,9,9,6,3,8,3]
count=0
for  i in a:
    if i==9:
        count+=1
print(count)'''

'''a=[]
n=5
for i in range(0,n):
    b=int(input("Enter list values"))
    a.append(b)
print(a)'''
'''
n=5
1)i=0
   b=132
   a.append(132)-->a[132]
2)i=1
   b=3
   a.append(3)-->a[132,3]
'''
a=[]
n=5
for i in range(0,n):
    b=int(input("Enter list values"))
    a.append(b)
print(a)

for i in range(0,n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)
