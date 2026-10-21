# predefined modules
# 1.math
# import math as m
# print(m.pi)
# print(m.sqrt(9))
# print(m.cbrt(27))
# print(m.ceil(2.3))
# print(m.floor(2.3))
# print(m.factorial(5))
# print(m.pow(5,3))
# a=10
# b=20
# c=a-b
# print(m.fabs(c))

# 2.scipy
# from scipy import constants as c
# print(c.pi)
# print(c.day)
# print(c.week)
# print(c.year)
# print(c.hour)
# print(c.milli)

# Calendar
# import calendar as c
# print(c.calendar(2027))
# print(c.month(2026,10))
# print(c.isleap(2028))
# print(c.weekday(2026,10,14))

# time
# import time as t
# print(t.ctime())
# t.sleep(5)
# print("hello")
# print(t.strftime("%Y-%M-%D %H:%M:%S"))

# datetime
# import datetime as d
# print(d.datetime.now())

# numpy
# import numpy as n
# a=n.array([1,5,8,9,3,2])
# print(n.min(a))
# print(n.max(a))
# print(n.sqrt(a))
# print(n.cbrt(a))
# print(n.mean(a))#[1,2,3,5,8,9]
# print(n.median(a))

# pywhatkit
# import pywhatkit as p
# import pyautogui
# # p.search("ind vs nz")
# p.sendwhatmsg_instantly("+91 9843050604","Hii Karthi...")
# pyautogui.press("Enter")

# webbrowser
# import  webbrowser as w
# w.open("https://www.youtube.com/watch?v=FW_PPcr1sPE")

# import selenium
# from selenium import webdriver
# import time as t
# from selenium.webdriver.common.by import By
# a = webdriver.Chrome()
# a.get("https://www.facebook.com/")
# t.sleep(5)
# a.find_element(By.XPATH, '//*[@id="_R_c9l6neappb6amH1_"]').send_keys("kokila")
# t.sleep(5)

# import socket as s
# print(s.gethostname())

# import sys
# print(sys.path)
# print(sys.version)
# sys.stdout.write("Helllo")
# sys.stderr.write("dsfghjk")

# import random as r
# print(r.random())
# print(r.randint(1000,9999))
# print(r.randrange(1000,9999,5))
# a=["Java","Python","C","C++"]
# r.shuffle(a)
# print(a)
# print(r.choice(a))

import pandas as p
data={"Name":["Kokila","Jana","Mano","Priya"],"Age":[27,25,22,18],
      "Mark":[85,96,99,100]}
a=p.DataFrame(data)
print(a)
print(a["Mark"].mean())
