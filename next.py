import tkinter as t
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
a=t.Tk()
a.geometry("1500x900")
a.title("Login Page")
a.config(background="Orchid")

l=Label(a,text="Welcome to my page....",font=("Bodoni MT Black",30),foreground="black",background="Orchid")
l.place(x=100,y=50)

l1=Label(a,text="Gender",font=("Bodoni MT Black",30),foreground="black",background="Orchid")
l1.place(x=100,y=150)

rb=Radiobutton(a,text="Male",font=("Bodoni MT Black",30),foreground="black",background="Orchid",value=1)
rb.place(x=300,y=150)

rb1=Radiobutton(a,text="Female",font=("Bodoni MT Black",30),foreground="black",background="Orchid",value=2)
rb1.place(x=500,y=150)

ck=Checkbutton(a,text="I agree to the terms and conditions",font=("Bodoni MT Black",30),foreground="black",background="Orchid")
ck.place(x=100,y=250)

b=["Select","CSE","ECE","EEE","MECH","CIVIL"]
cb=Combobox(a,font=("Bodoni MT Black",30),foreground="black",background="Orchid",width=10)
cb['values']=b
cb.current(0)
cb.place(x=100,y=350)

age=Spinbox(a,from_=22,to=35,font=("Bodoni MT Black",30),foreground="black",background="Orchid",width=5)
age.place(x=100,y=450)

sct=scrolledtext.ScrolledText(a, width=20, height=10, font=("Bodoni MT Black",30), foreground="black", background="Orchid")
sct.place(x=750,y=50)
a.mainloop()