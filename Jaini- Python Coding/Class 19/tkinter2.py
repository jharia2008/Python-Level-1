from tkinter import *
screen1= Tk()
#syntax to set the screen size
screen1.geometry("400x400")
#syntax to give the screen background color
screen1.configure(bg="turquoise")
k1= Button(screen1, text="Button1", bg= "blue", fg="yellow", relief= GROOVE, bd= 6, activebackground= "orange")
k2= Button(screen1, text="Button2", bg= "pink", fg="green", relief= SUNKEN, padx= -5, pady= 5, activeforeground= "purple")
k1.grid(row=0, column=0)
k2.grid(row=1, column=1)
#bg= background color, fg= text color, font= text font, image= image on button, height= height of button
#width= width of button, active background= changing background color when button is under curser/being hovered
#active forground= changing color of text when being hovered, bd= border in pixels by defult it is 2 pixels
#padx= padding left and right inside button, pady= padding top and bottom inside button
#command= used to call function, relief= change border style, underline= underline text by default it is -1
#state= disable button, active state= when the mouse is over it, normal= when you want to enable the state
#justify= used to set position left, right, or center

mainloop()