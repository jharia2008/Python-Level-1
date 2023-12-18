#syntax to import different libraries or modules
#1 from libraryName import * or import libraryName or import libraryName as variableName
from tkinter import *
#creating screen by using Tk
screen= Tk()
#to give the text label widget is used
l1= Label(screen, text="Colors")
l1.pack() 
#once the label is created in the next line you need to mention how you want to display that means position on the screen
#three ways to set the position: pack(), grid(), place()
#pack(): it is used to set the things one after another in vertical order or sometimes maybe in a horizontal order
#grid(): it is used to set the things in rows or columns order 
#place():it is used to set the position using x-axis and y-axis y at the top is negative and y at the bottom is positive
#you cannot use two of the position functions together in one program 
#ex. if you started your program with pack, you cannot use grid or place visa versa if you start if place or grid, you cant use pack
b1= Button(screen, text="Submit")
b1.pack()

#syntax to use mainloop- name of the screen.mainloop(), or mainloop()
screen.mainloop()