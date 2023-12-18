from tkinter import *
from PIL import Image, ImageTk 
screen=Tk()
screen.iconbitmap("C:/Users/anish/OneDrive/Desktop/Jaini- Python Coding/Class 20/flower.ico")
#if png image needs to be used for the icon then use iconphoto()
#PhotoImage function is used to store the image in a variable
# img1=PhotoImage(file= "C:/Users/anish/OneDrive/Desktop/Jaini- Python Coding/Class 20/dog.png")
# screen.iconphoto(False, img1)

#steps to give image on the screen-
#step 1: first import Image, ImageTk from PIL library
#step 2: use Image.open to give the name of the image
#step 3: resize function to change the size of the picture
#step 4: ImageTk.PhotoImage to load up the image
#step 5: use Label to set it on the screen 
i= Image.open("C:/Users/anish/OneDrive/Desktop/Jaini- Python Coding/Class 20/dog.png")
d= i.resize((100, 100))
img= ImageTk.PhotoImage(d)
l1= Label(screen, image= img, pady= -30) #padx and pady are used to give space from left(padx), right(padx), up(pady-), and down(pady+) by giving negative and positive values
l1.pack()

mainloop()