from tkinter import *
screen= Tk()

a= StringVar()
b= StringVar()
c= StringVar()
d= StringVar()

def answers():
    k= a.get(), b.get(), c.get(), d.get()
    l1= Label(screen, text=k)
    l1.pack()

l1= Label(screen, text="What is my favorite color?")
l1.pack()
c1= Checkbutton(screen, text="blue", onvalue="blue", offvalue="", variable=a)
c1.pack()
c2= Checkbutton(screen, text="pink", onvalue="pink", offvalue="", variable=b)
c2.pack()
c3= Checkbutton(screen, text="purple", onvalue="purple", offvalue="", variable=c)
c3.pack()
c4= Checkbutton(screen, text="orange", onvalue="orange", offvalue="", variable=d)
c4.pack()
b1= Button(screen, text="Submit", bg="pink", command= answers)
b1.pack()

mainloop()