from tkinter import *
screen =Tk()
#frame is like a box where you place the things togetherand do styling. youcan create many
#frames in one screen.for example : listbox and scrollbar put together. or if you want to 
#place two button together and give background color only to them not whole page
my_frame=Frame(screen)

l2=Label(screen)
def delete():
    l2.delete(ANCHOR)
    l2.config(text="")
def select():
    l2.config(text=l1)

s= Scrollbar(my_frame, orient="vertical")

#If you want to put anything inside frame you write name of the frame in taht widget instead of screen name
l1= Listbox(my_frame, width= 50, height= 10, yscrollcommand= s.set, selectmode=MULTIPLE) 
#1st method add item to the listbox 
l1.insert(END, "One")
l1.insert(END, "Two")
l1.pack()
my_frame.pack()

#2nd method to insert data inside the listbox using for loop
list1=["Jaini", "Sakshi", "Carli", "Cate", "Shauna"]
#here we insert function is used again and again on all the data which is inside the list
for i in list1:
    l1.insert(END, i)

#connect your listbox with the scrollbar
#When you want to attach scrollbar to any other thing like here in this vcase ist listbox 
#so use yscrollcommand in listbox and yview in scrollbar so it knows atht vertical 
#scrollbar needs to be attached to listbox
#yview changes the vertical position of the widget according to the window
#if it is horizontal scroll bar xcrollcommand and xview
s.config(command=l1.yview) 
s.pack(side=RIGHT, fill= Y)

b1= Button(screen, text="Select", bg="turquoise")
b1.pack()
b2=Button(screen, text="Delete", bg="pink")
b2.pack()
b3= Button(screen, text="Delete Multiple", bg="lavender")
b3.pack()


mainloop()