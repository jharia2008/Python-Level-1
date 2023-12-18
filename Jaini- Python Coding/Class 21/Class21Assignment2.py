#create a login page but better than the last one

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
screen= Tk()

a= input("enter your username")
b= input("enter your password")
c=StringVar()
d=StringVar()

def Logins():
    if c.get()== a and d.get()==b:
        messagebox.showinfo("Information", "You have successfully logged in.")
    else:
        messagebox.askretrycancel("Error", "Username or password is incorrect.")

l1= Label(screen, text="Log In")
l1.grid(row=0, column=0)
l1= Label(screen, text="Username")
l1.grid(row=2, column=0)
e1= Entry(screen, width=28, bg="lightGreen", textvariable=c) 
e1.grid(row=3, columnspan= 4, column= 0)
l1= Label(screen, text="Name")
l1.grid(row=4, column=0)
e1= Entry(screen, width=28, bg="lightBlue")
e1.grid(row=5, columnspan= 4, column= 0)
l1= Label(screen, text="Password")
l1.grid(row=6, column=0)
e2= Entry(screen, width=28, bg="lavender", textvariable= d)
e2.grid(row=7, columnspan= 4, column= 0)

i= Image.open("C:/Users/anish/OneDrive/Desktop/Jaini- Python Coding/Class 21/Login-logo.jpg")
n= i.resize((150, 100))
img= ImageTk.PhotoImage(n)
l1= Label(screen, image= img) 
l1.grid(row=7, column=4)

b1= Button(screen, text="Submit", bg= "pink", fg="black", width=8, height=1, command= Logins)
b1.grid(row=8, column= 2)

mainloop()