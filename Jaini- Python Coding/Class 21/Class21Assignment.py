from tkinter import *
screen= Tk()
screen.geometry("100x100")

def open2():
    global myimage
    global screen3
    screen3=Tk()
    l2=Label(screen3, text="This is topLevel2 window")
    l2.pack()
    b4= Button(screen3, text="open topLevel3")
    b4.pack()
    b5= Button(screen3, text="exit", command=exit2)
    b5.pack()
    
def open():
    global myimage
    global screen2
    screen2=Tk()
    l1=Label(screen2, text="This is topLevel1 window")
    l1.pack()
    b2= Button(screen2, text="open topLevel1", command= open2)
    b2.pack()
    b3= Button(screen2, text="exit", command=exit)
    b3.pack()

def exit():
    screen2.destroy()   

def exit2():
    screen3.destroy()

b1= Button(screen, text="open topLevel1", command= open)
b1.pack()


mainloop()