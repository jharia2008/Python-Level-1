from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
screen= Tk()

def open():
    global myimage
    screen2=Tk()
    screen.destroy()
    g=ImageTk.PhotoImage(Image.open("C:/Users/anish/OneDrive/Desktop/Jaini- Python Coding/Class 20/apple.png"))
    l1=Label(screen2, image=g)
    l1.pack()

b1= Button(screen, text="Submit", command= open)
b1.pack()

mainloop()