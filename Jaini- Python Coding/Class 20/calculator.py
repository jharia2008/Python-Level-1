from tkinter import *
screen= Tk()
#always create the functions before the widgets and before you call them
#tkinter variables are like normal variables used to store the things, they store the input values taken from the user through widgets like input, radio buttons, check buttons, scale, etc.
#syntax to create a tkinter variable
a=StringVar() #inside the variable give the function according to what you are going to store IntVar(), StringVar(), BoolVar(), DoubleVar()
#after creating a tkinter variable, connect that variable to the widget where the input is coming
expression=""
def pressButton(num):
    global expression #when you create a variable and change that variable value inside the function and when you come out of it the value of the variable will not be the changed value
    #this is because changes done inside the funtion will not work when you come outside the function
    #but if you want the changes inside to work outside also 
    expression=expression+str(num) #num is a temporary variable which will be replaced by the actual value when you call it
    a.set(expression) #set means updating the tkinter variable a with number and later on this tkinter variable updates the entry box because they both have connected
def equals():
    global expression
    try: 
        total=str(eval(expression))#eval function is the inbuilt function which means evaluating the expression, its work is to perform the addition, subtraction, multiplication, division based on the sign given
        a.set(total)#setting the answer again back to the tkinter variable a
        expression=""
    except:
        a.set("error")
        expression=""

def clear1():
    global expression
    a.set("")
    expression=""

def positive():
    global expression
    expression=-expression
    a.set(expression)
    expression=""

l1= Label(screen, text="Calculator")
l1.grid(row=0, column=0)
#input box is used 
e1= Entry(screen, width=28, textvariable=a)
e1.grid(columnspan= 4, ipadx= 50)
b1= Button(screen, text="AC", bg= "gray", fg="black", width=7, height=1, command=clear1)
b1.grid(row=2, column= 0)
b2= Button(screen, text="+/-", bg= "gray", fg="black", width=7, height=1, command=positive)
b2.grid(row= 2, column= 1)
b3= Button(screen, text="%", bg= "gray", fg="black", width=7, height=1, command=lambda:pressButton("%"))#when you call a function which has a variable inside the () then lambda key word is used to call the function
#but if you have a function without any variable then () command = name of function 
b3.grid(row=2,column=2)
b4= Button(screen, text="/", bg= "orange", fg="white", width=7, height=1, command=lambda:pressButton("/"))
b4.grid(row=2, column=3)
b5= Button(screen, text="7", bg="gray", fg= "white", width=7, height=1, command=lambda:pressButton(7))
b5.grid(row=3, column=0)
b6= Button(screen, text="8", bg="gray", fg= "white", width=7, height=1, command=lambda:pressButton(8))
b6.grid(row=3, column=1)
b7= Button(screen, text="9", bg="gray", fg= "white", width=7, height=1, command=lambda:pressButton(9))
b7.grid(row=3, column=2)
b8= Button(screen, text="*", bg="orange", fg= "white", width=7, height=1, command=lambda:pressButton("*"))
b8.grid(row=3, column=3)
b9= Button(screen, text="4", bg="gray", fg= "white", width=7, height=1, command=lambda:pressButton(4))
b9.grid(row=4, column=0)
b10= Button(screen, text="5", bg="gray", fg= "white", width=7, height=1, command=lambda:pressButton(5))
b10.grid(row=4, column=1)
b11= Button(screen, text="6", bg="gray", fg= "white", width=7, height=1, command=lambda:pressButton(6))
b11.grid(row=4, column=2)
b12= Button(screen, text="-", bg="orange", fg= "white", width=7, height=1, command=lambda:pressButton("-"))
b12.grid(row=4, column=3)
b13= Button(screen, text="1", bg="gray", fg= "white", width=7, height=1, command=lambda:pressButton(1))
b13.grid(row=5, column=0)
b14= Button(screen, text="2", bg="gray", fg= "white", width=7, height=1, command=lambda:pressButton(2))
b14.grid(row=5, column=1)
b15= Button(screen, text="3", bg="gray", fg= "white", width=7, height=1, command=lambda:pressButton(3))
b15.grid(row=5, column=2)
b16= Button(screen, text="+", bg="orange", fg= "white", width=7, height=1, command=lambda:pressButton("+"))
b16.grid(row=5, column=3)
b17= Button(screen, text="0", bg="gray", fg= "white", width=7, height=1, command=lambda:pressButton(0))
b17.grid(row=6, column=1)
b18= Button(screen, text=".", bg="gray", fg= "white", width=7, height=1, command=lambda:pressButton("."))
b18.grid(row=6, column=2)
b19= Button(screen, text="=", bg="orange", fg= "white", width=7, height=1, command=equals)
b19.grid(row=6, column=3)

mainloop()