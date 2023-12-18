from tkinter import *
import tkinter.font as tkfont
import datetime
import customtkinter
from tkinter import messagebox
from reportlab.pdfgen import canvas

screen=Tk()
screen.configure(bg="cadetblue")

a= IntVar()
j= StringVar()
q= StringVar()
p= StringVar()
w= StringVar()
t= StringVar()
y= StringVar()
dt=StringVar()
hg=StringVar()
om=StringVar()
fy=StringVar()
bl=StringVar()

def submit():
    u= a.get()
    h= j.get()
    v= q.get() 
    z= p.get()
    ng= w.get()
    hd= t.get()
    vd= y.get() 
    ut= hg.get()
    hy= om.get()
    vu= fy.get() 
    zj= bl.get()
    
    if u=="" or h=="" or v=="" or z=="" or ng=="" or hd=="" or vd=="" or ut=="" or hy=="" or vu=="" or zj=="":
        messagebox.showinfo("Error", "Enter all the Things")
    else:
        pdfFile=hd+".pdf"
        c=canvas.Canvas(pdfFile)
        c.drawString(100, 700, "Customer Name:     " , hd)
        c.drawString(100, 650, "Invoice Number:      ", ng)
        c.drawString(100, 600, "Date&Time:      ", f)
        c.drawString(100, 550, "Email:      ",vd)
        c.drawString(100, 500, "Phone Number:      ",ut)
        c.drawString(100, 450, "Movie:      ",hy)
        c.drawString(100, 400, "Tickets:      ", u)
        c.drawString(100, 350, "Food:      ", h, v ,z)
        c.drawString(100, 300, "Price:      ",vu)
        c.drawString(100, 250, "Tax:      ",zj)
        
        messagebox.showinfo("Success", "It's been downloaded")
        c.save()


l1= Label(screen, text="Cinema App", font=("Times", 40), bg="cadetblue")
l1.grid(row=0, column=4)

l4= Label(screen, text="Invoice Number", font=("Arial", 15), bg="cadetblue")
l4.grid(row=1, column=0)
e4= Entry(screen, textvariable=w)
e4.configure(bg="powderblue", width=50)
e4.grid(row=1, columnspan=3, column=1, pady=12)

dt= datetime.datetime.now()
f=dt.strftime("%H:%M:%S")
l5= Label(screen, text="Date & Time", font=("Arial", 15),  bg="cadetblue")
l5.grid(row=2, column=0)
e5= Entry(screen)
e5.insert(END, f)
e5.configure(bg="powderblue", width=50)
e5.grid(row=2, columnspan=3, column=1, pady=12)

l2= Label(screen, text="Name", font=("Arial", 15),  bg="cadetblue")
l2.grid(row=3, column=0)
e1= Entry(screen, textvariable=t)
e1.configure(bg="powderblue", width=50)
e1.grid(row=3, columnspan=3, column=1, pady=12)

l2= Label(screen, text="Email", font=("Arial", 15),  bg="cadetblue")
l2.grid(row=4, column=0)
e1= Entry(screen, textvariable=y)
e1.configure(bg="powderblue", width=50)
e1.grid(row=4, columnspan=3, column=1, pady=12)

l2= Label(screen, text="Phone Number", font=("Arial", 15),  bg="cadetblue")
l2.grid(row=5, column=0)
e1= Entry(screen, textvariable= hg)
e1.configure(bg="powderblue", width=50)
e1.grid(row=5, columnspan=3, column=1, pady=12)

l4=Label(screen,  text="Movie Choices", bg="cadetblue", font=("Arial", 15),)
l4.grid(row=6, column= 0)
options=["Barbie", "Top Gun", "Spy Kids", "Mission Impossible 7"]
om= StringVar()
om.set("Barbie")
d= OptionMenu(screen, om, *options)
d.configure(bg= "thistle", width=20)
d.grid(row=6, column=1, pady=12)

l3= Label(screen, text="Tickets", font=("Arial", 15),  bg="cadetblue")
l3.grid(row=7, column=0)
s1=Scale(screen, from_= 1, to= 10, orient= 'horizontal', variable= a, bg="thistle")
s1.grid(row=7, column= 1)

l1= Label(screen, text="Food Items", font=("Arial", 15),  bg="cadetblue")
l1.grid(row=8, rowspan=4, column=0)
c1= Checkbutton(screen, text="Popcorn", onvalue="1", offvalue="0", variable= j, font=("Arial", 15),  bg="cadetblue")
c1.grid(row=9, column=1)
c2= Checkbutton(screen, text="Candy", onvalue="1", offvalue="0", variable= q, font=("Arial", 15),  bg="cadetblue")
c2.grid(row=10, column=1)
c3= Checkbutton(screen, text="Soda", onvalue="1", offvalue="0", variable= p, font=("Arial", 15),  bg="cadetblue")
c3.grid(row=11, column=1)

l7=Label(screen, text="Price", font=("Arial", 15), bg="cadetblue")
l7.grid(row=12, column=0)
e7= Entry(screen, textvariable=fy)
e7.configure(bg="powderblue", width=50)
e7.grid(row=12, columnspan=3, column=1, pady=12)

l8=Label(screen, text="Tax", font=("Arial", 15), bg="cadetblue")
l8.grid(row=13, column=0)
e8= Entry(screen, textvariable=bl)
e8.configure(bg="powderblue", width=50)
e8.grid(row=13, columnspan=3, column=1, pady=12)

b1= Button(screen, text="Confirm", font=("Arial", 12), bg="purple", fg="white", command=submit)
b1.grid(row=14, columnspan=4, column=0)



mainloop()