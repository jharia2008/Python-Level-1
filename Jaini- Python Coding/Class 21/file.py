from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
screen= Tk()

def open_file():
    fileName= filedialog.askopenfilename(initialdir="C:/Users/anish/OneDrive/Desktop/Jaini- Python Coding/Class 21", title="open image file", filetypes=(("PNG File", "*.png"), ("JPG File", "*.jpg"), ("ALL Files", "*.txt"))) 
    #this function helps you open any file. it can open all files
    #inside this we give a link path that will open, it can be c drive, d drive, downloads, anything
    #we also give the extensions of any file
    global img
    img= ImageTk.PhotoImage(Image.open(fileName))
    l1= Label(screen, image=img)
    l1.pack()

def safeFile():
    files=[("ALL Files", "*.*"), ("Python Files", "*.py"), ("Text Document", "*.txt")]
    file= filedialog.asksaveasfile(filetypes=files, defaultextension=files)

b1=Button(screen, text="Open File", command= open_file)
b1.pack()

b2= Button(screen, text="Save File", command= safeFile)
b2.pack()
mainloop()