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
#Searching a element in list
'''a=[]
n=5
for i in range(0,n):
    b=int(input("Enter list values"))
    a.append(b)
print(a)
key=int(input("Enter element you want search.."))
for i in a:
    if i==key:
        print("Element found")
'''
#Sorting list
'''for i in range(0,n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)'''


#Tuple ()
'''a=(12,3.6,2+6j,"hello",False,3.6)
print(a)
print(a.count(12))
print(a.index(3.6))
b=(45,)
print(type(b))'''
'''print(a[3])
print(a[-3])
b=(12,6,6,(45,96,9),45,89)
print(b[3][2])'''

#set {}
'''a={1,2,3,6,5,6}
b={2,3,7,8,9}
a.add(4)
print(a)
print(a.difference(b))
#a.difference_update(b)
print(a.intersection(b))
#a.intersection_update(b)
print(a.symmetric_difference(b))
#a.symmetric_difference_update(b)
print(a.union(b))
c={1,2,3,4,5}
d={1,2,3}
print(c.issuperset(d))
print(d.issubset(c))
d=a.copy()
print(d)
a.discard(5)
print(a)
a.remove(6)
print(a)
a.pop()
print(a)
a.update(b)
print(a)
e={12,36,89}
print(a.isdisjoint(e))
a.clear()
print(a)'''

'''a=[1,2,3,1,2,5,6]
b=set(a)
c=list(b)
print(c)'''

''''a={}
print(type(a))'''

'''a={"Name":"Python","author":"Guido Van Rossum","year":1991,"age":36}
print(a)
print(a.get("Name"))
print(a.keys())
print(a.values())
print(a.items())
print(a.pop("age"))
print(a.popitem())
print(a.setdefault("Basic","for AI"))
print(a.update({"Year":1991}))
b=a.copy()
print(b)
#a.clear()
print(a)'''

a={1,2,3}
b={"Hello"}
c="Java"
print(dict.fromkeys(a,b))
print(dict.fromkeys(b,a))
print(dict.fromkeys(c,a))
