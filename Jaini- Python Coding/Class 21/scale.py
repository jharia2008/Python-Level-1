from tkinter import *
screen= Tk()

a= DoubleVar()
def show():
    w= "horizontal value", a.get()
    l1= Label(screen, text=w)
    l1.pack()

s1=Scale(screen, from_= 1, to= 100, orient= 'horizontal', variable= a)
s1.pack()
b1= Button(screen, text="Submit", command=show, bg="pink")
b1.pack()


mainloop()