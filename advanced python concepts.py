
'''abc-->abstract base class
   ABC-->Abstract class'''
# from abc import ABC,abstractmethod
# class Java(ABC):
#     @abstractmethod
#     def program(self):
#        pass
# class Python(Java):
#     def program(self):
#         print("Hello Python")
# a=Python()
# a.program()


# class Java:
#     __name="James Gosling"
#     def __program(self):
#         print("Hello java")
#     def demo(self):
#         print(self.__name)
#         self.__program()
# b=Java()
# b.demo()





# print(__doc__)

# def demo():
#     '''Hello Python....'''
# print(demo.__doc__)

# a=[1,2,5,85,9,96]
# b=a.copy()
# print(b)


# def demo(a):
#     print("Hello Java")
#     def fun():
#         print("Welcome ...",a)
#     fun()
# demo("Kokila")

# def demo():
#     n=5
#     for i in range(1,6):
#         n*=i
#         yield n
# a=demo()
# for i in a:
#     print(i)


# def  java(demo):
#     def fun():
#         print("Hello Java")
#         demo()
#         print("Welcome...")
#         return fun()
# @java
# def demo():
#     print("hiii")
# demo()

# def add(a,b):
#     return a+b
# a=[1,2,3,4,5]
# b=[9,8,7,6,5]
# x=map(add,a,b)
# print(x)
# for i in x:
#     print(i)

# voewl=['a','e','i','o','u']
# def demo(a):
#     for i in a:
#         if i in voewl:
#             return i
# x=filter(demo,['r','a','i','t','i','r','n','c','h','o','s'])
# for i in x:
#     print(i)

a=["C","C++","Python","Java","Selenium"]
b=iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))


# for i in a:
#     print(i)
