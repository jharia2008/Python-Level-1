#create a new quiz where there are 5 labels to give questions, 5 entry boxes where answers will be given
#at the end a submit button that when clicked shows a score of how many answers are correct
#5 tk variables for the answers, in the functions more variables with actual answers which get == to other answer
#if correct then score goes up 1 in another variable

from tkinter import *
from tkinter import messagebox
screen= Tk()

r= StringVar()
o= StringVar()
s= StringVar()
c= StringVar()
p= StringVar()

def button1():
    r10=r.get()
    o10=o.get()
    s10=s.get()
    c10=c.get()
    p10=p.get()

    q1a="7"
    q2a="Pacific"
    q3a="8"
    q4a="100"
    q5a="Jupiter"

    score=0

    if(r10==q1a):
        score= score +1
    else:
        score=score
    
    if(o10==q2a):
        score= score +1
    else:
        score=score

    if(s10==q3a):
        score= score +1
    else:
        score=score

    if(c10==q4a):
        score=score +1
    else:
        score=score

    if(p10==q5a):
        score= score +1
    else:
        score=score
    
    SCORE= Label(screen, text= "Your score is " + str(score))
    SCORE.grid(row=21, columnspan=3, column=0)


l1= Label(screen, text="Question 1: How many colors are in the rainbow?")
l1.grid(row=0, columnspan=4, column=0)
r1= Radiobutton(screen, text="3", value="3", variable= r)
r1.grid(row=1, column=0)
r2= Radiobutton(screen, text="9", value="9", variable= r)
r2.grid(row=2, column=0)
r3= Radiobutton(screen, text="7", value="7", variable= r)
r3.grid(row=3, column=0)



l2= Label(screen, text="Question 2: Which is the world's largest ocean?")
l2.grid(row=4, columnspan=4, column=0)
r1= Radiobutton(screen, text="Pacific", value="Pacific", variable= o)
r1.grid(row=5, column=0)
r2= Radiobutton(screen, text="Atlantic", value="Atlantic", variable= o)
r2.grid(row=6, column=0)
r3= Radiobutton(screen, text="Artic", value="Artic", variable= o)
r3.grid(row=7, column=0)




l3= Label(screen, text="Question 3: How many legs does a spider have?")
l3.grid(row=8, columnspan=4, column=0)
r1= Radiobutton(screen, text="6", value="6", variable= s)
r1.grid(row=9, column=0)
r2= Radiobutton(screen, text="10", value="10", variable= s)
r2.grid(row=10, column=0)
r3= Radiobutton(screen, text="8", value="8", variable= s)
r3.grid(row=11, column=0)



l4= Label(screen, text="Question 4: How many years are in a century?")
l4.grid(row=12, columnspan=4, column=0)
r1= Radiobutton(screen, text="1000", value="1000", variable= c)
r1.grid(row=13, column=0)
r2= Radiobutton(screen, text="10", value="10", variable= c)
r2.grid(row=14, column=0)
r3= Radiobutton(screen, text="100", value="100", variable= c)
r3.grid(row=15, column=0)



l5= Label(screen, text="Question 5: What is the largest planet in the solar system?")
l5.grid(row=16, columnspan=4, column=0)
r1= Radiobutton(screen, text="Saturn", value="Saturn", variable= p)
r1.grid(row=17, column=0)
r2= Radiobutton(screen, text="Jupiter", value="Jupiter", variable= p)
r2.grid(row=18, column=0)
r3= Radiobutton(screen, text="Sun", value="Sun", variable= p)
r3.grid(row=19, column=0)

b1= Button(screen, text="Submit", bg="pink", command= button1)
b1.grid(row=20, columnspan=3, column=0)

mainloop()