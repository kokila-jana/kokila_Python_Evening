import tkinter as t
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
a=t.Tk()
a.geometry("1500x900")
a.title("Login Page")
# a.config(background="Orchid")
i=Image.open("C:\\Users\\manojana\\OneDrive\\Pictures\\dhoni wallpaper.png")
j=ImageTk.PhotoImage(i)
Back=Label(a,image=j)
Back.place(relwidth=2,relheight=1)
#
l=Label(a,text="Login Page",font=("Bodoni MT Black",30),foreground="Navy")
l.place(x=200,y=100)
# l.pack()
#
l1=Label(a,text="UserName",font=("Bodoni MT Black",30),foreground="Navy")
l1.place(x=100,y=200)
#
t=Entry(a,font=("Bodoni MT Black",30),foreground="Navy",width=10)
t.place(x=330,y=200)
#
l2=Label(a,text="Password",font=("Bodoni MT Black",30),foreground="Navy")
l2.place(x=100,y=300)
#
t1=Entry(a,font=("Bodoni MT Black",30),foreground="Navy",width=10,show="*")
t1.place(x=330,y=300)

def demo():
    s=t.get()
    s1=t1.get()
    if s=="" or s1=="":
        messagebox.showerror("Error","Please Enter UserName and Password")
    elif s=="Python" and s1=="12345":
        messagebox.showinfo("Message","Login Success")
    else:
        messagebox.showerror("Error","Invalid UserName and Password")

b=Button(a,text="Login",font=("Bodoni MT Black",30),foreground="Navy",activebackground="pink",activeforeground="green",command=demo)
b.place(x=200,y=400)
#
a.mainloop()

