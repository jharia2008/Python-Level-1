from tkinter import *
screen=Tk()

global l2
l2= Label(screen, text="CodeVidhya", font=("Times", 27))
l2.grid(row=0, columnspan=4, column=0)

my_frame=Frame(screen)
s= Scrollbar(my_frame, orient="vertical")
l1= Listbox(my_frame, width= 50, yscrollcommand= s.set, selectmode=MULTIPLE)
l1.grid(row=2,rowspan=7, column=0) 
my_frame.grid(row=2,rowspan=7, columnspan=4, column=0)

list1=["user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8", "user9", "user10", "user11", "user12", "user13", "user14", "user15", "user16", "user17", "user18", "user19"]
for i in list1:
    l1.insert(END, i)

s.config(command=l1.yview) 
s.grid(row=2, column=5, ipady=50)

def delete():
    l1.delete(ANCHOR)
    l2.config(text="")

def select():
    l2.config(text=l1.get(ANCHOR))

def deleteAll():
    l1.delete(0, END)

def selectAll():
    result=""
    for i in l1.curselection():
        result=result+str(l1.get(i))+"\n"
    l2.config(text=result)

def deleteMultiple():
    for i in reversed(l1.curselection()):
        l1.delete(i)
        l2.config(text="")


b1=Button(screen, text="Delete", command=delete)
b1.grid(row=9, column=0)
b2=Button(screen, text="Delete Multiple", command=deleteMultiple)
b2.grid(row=9, column=1)
b2=Button(screen, text="Delete All", command=deleteAll)
b2.grid(row=9, column=2)
b3=Button(screen, text="Select", command=select)
b3.grid(row=9, column=3)
b4=Button(screen, text="Select All", command=selectAll)
b4.grid(row=9, column=4)

mainloop()