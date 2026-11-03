# def add():
#     a=10
#     b=20
#     print(a+b)
#
# def reverse(a):
#     b=0
#     while a>0:
#         c=a%10
#         b=b*10+c
#         a=a//10
#     print(b)
#
# def isVowel(a):
#     s=['a','e','i','o','u']
#     for i in s:
#         if i==a:
#             return "Vowel"
#     return "constant"


# class Car:  # parent class
#     brand = "Audi"
#
#     def drive(self):
#         print("I have ", self.brand, " Car...")
#
#
# class Bike(Car):  # child class for Car
#     model = "Royal Enfield"
#
#     def ride(self):
#         print("I have ", self.model, " bike")
#
# class Bus(Bike):
#     route="salem"
#     def travel(self):
#         print("We going to ",self.route)
#
# b = Bus()
# b.ride()
# b.drive()
# b.travel()


# class Mobile:#parent
#     brand = "Oppo"
#
#     def play(self):
#         print("I have ", self.brand, "phone")
#
# class Tab:
#     os="Mac"
#     def study(self):
#         print("I am studying with",self.os," os tab")
#
# class Laptop(Mobile,Tab):
#     pc="acer"
#     def coding(self):
#         print("I am doing python coding with",self.pc," laptop")
#
# c=Laptop()
# c.play()
# c.study()
# c.coding()

# b=Tab()
# b.study()
# b.play()


class Java:
    def __init__(self):#constructor
        print("High level Programming")
    def demo(self):#function
        print("Hello Java")
    def __del__(self):
        print("object deleted...")

a=Java()#constructor call
a.demo()#function call
del a
a.demo()
