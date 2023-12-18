from tkinter import *
screen= Tk()
screen.geometry("400x400")
screen.configure(bg="pink")
k1= Button(screen, text="Button1", bg= "aquamarine", fg="blue", activebackground= "purple")
k2= Button(screen, text="Button2", bg= "lime", fg="green", activebackground= "yellow")
k1.grid(row=1, column=3)
k2.grid(row=5, column=1)

mainloop()