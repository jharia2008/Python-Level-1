#HOMEWORK: NOW MAKE LOGIN PAGE WORK BY USING TKINTER VARIABLE THAT HAVE TO == NORMAL VARIABLES
#OR ELSE THE SCREEN SHOULD PRINT "USERNAME OR PASSWORD IS WRONG"
#ALSO DO WEEK 17 QUIZ


#create a log in page and do the designing of it
from tkinter import *
screen= Tk()

a=StringVar()
b=StringVar()
def Logins():
    c= "jharia02"
    d= "mc90006!"
    if a.get()==c and b.get()==d: #whenever you are getting input from an input variable, use .get()
        l2= Label(screen, text="Your Username and Password are Correct!")
        l2.grid(row=9, column= 0)
    else:
        l2= Label(screen, text="Your Username or Password are Incorrect")
        l2.grid(row=9, column=0)

l1= Label(screen, text="Log In")
l1.grid(row=0, column=0)
l1= Label(screen, text="Username")
l1.grid(row=2, column=0)
e1= Entry(screen, width=28, bg="lightGreen", textvariable= a) 
#whenever there is a string to store in tkinter variable then we use textvariable= to connect in the widget otherwise we use variable=
e1.grid(row=3, columnspan= 4, column= 0)
l1= Label(screen, text="Name")
l1.grid(row=4, column=0)
e1= Entry(screen, width=28, bg="lightBlue")
e1.grid(row=5, columnspan= 4, column= 0)
l1= Label(screen, text="Password")
l1.grid(row=6, column=0)
e1= Entry(screen, width=28, bg="lavender", textvariable= b)
e1.grid(row=7, columnspan= 4, column= 0)
b1= Button(screen, text="Submit", bg= "pink", fg="black", width=8, height=1, command= Logins)
b1.grid(row=8, column= 0)

if Logins== e1:
    print("You can log in!")
else:
    print("Username or Password is incorrect.")

mainloop()