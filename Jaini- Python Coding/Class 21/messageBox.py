from tkinter import *
from tkinter import messagebox
screen=Tk()

def submit():
    global expression
    messagebox.showinfo("Information", "Button has been clicked")
    f= messagebox.askquestion("Question", "Are you sure")
    if f=="yes":
        l1=Label(screen, text="You have selected yes")
        l1.pack()
    else:
        l2=Label(screen, text="You have selected No")
        l2.pack()

#messagebox.showinfo("Information", "My name is Jaini.")
#messagebox.showwarning("Warning", "This is scary.")
#messagebox.showerror("Error", "The username is incorrect.")
#messagebox.askquestion("Are you sure?", "Is ths the answer you want to put for the quiz?")
#messagebox.askyesno("Find the value?", "Is the answer yes or no?")
#messagebox.askretrycancel("Try Again?", "Do you want to try again?")
#messagebox.askokcancel("Cancel?", "do you want to cancel?")

b1= Button(screen, text="Submit", command=submit)
b1.pack()

mainloop()