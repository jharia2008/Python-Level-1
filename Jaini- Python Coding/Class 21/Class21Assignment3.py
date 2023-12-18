#do login page using screenshot
#assignment on codevidhya
    #if onvalue=0 label this else label that

from tkinter import *
screen= Tk()

a= StringVar()
b= StringVar()
c= StringVar()
d= StringVar()

def answers():
    k= a.get(), b.get(), c.get(), d.get()
    m= "You have ordered" + str(k)
    l3= Label(screen, text=m)
    l3.pack()

l1= Label(screen, text="What toppings do you want.")
l1.pack()
c1= Checkbutton(screen, text="Pepperoni", onvalue="Pepperoni", offvalue="", variable=a)
c1.pack()
c2= Checkbutton(screen, text="Olives", onvalue="Olives", offvalue="", variable=b)
c2.pack()
c3= Checkbutton(screen, text="Mushrooms", onvalue="Mushrooms", offvalue="", variable=c)
c3.pack()
c4= Checkbutton(screen, text="Green Peppers", onvalue="Green Peppers", offvalue="", variable=d)
c4.pack()
b1= Button(screen, text="Submit", bg="pink", command= answers)
b1.pack()



mainloop()