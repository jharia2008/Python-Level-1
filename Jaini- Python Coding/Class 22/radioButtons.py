from tkinter import *
screen= Tk()

j= StringVar()

def button1():
    i= j.get()
    n= "You have selected", str(i)
    l2= Label(screen, text= n)
    l2.pack()

l1= Label(screen, text="Following are the programming languages")
l1.pack()
r1= Radiobutton(screen, text="HTML", value="HTML", variable= j)
r1.pack()
r2= Radiobutton(screen, text="CSS", value="CSS", variable= j)
r2.pack()
r3= Radiobutton(screen, text="Java", value="Java", variable= j)
r3.pack()
b1= Button(screen, text="Submit", bg="pink", command= button1)
b1.pack()

mainloop()