#create an app with studentId, bookId, studentName, bookName, date of issue, date of return, with add button, query button, entry box for id, edit button
#do all database coding

from tkinter import *
import sqlite3
screen= Tk()

connection=sqlite3.connect("mydb.db")
crsr=connection.cursor()

#sql = """create table library(
#studentID integer primary key autoincrement,
#bookID varchar(70),
#student_Name varchar(70),
#book_Name varchar(70),
#doi varchar(20),
#dar varchar(50)
#)"""
#crsr.execute(sql)

def add():
 crsr.execute("INSERT INTO library VALUES (:studentID,  :bookID, :s_name , :b_name , :doi , :dor)",
        {
            'studentID' : e1.get(),
            'bookID' : e2.get(),
            's_name' : e3.get(),
            'b_name' : e4.get(),
            'doi' : e5.get(),
            'dor' : e6.get()
        }
    )
 e1.delete(0,END)
 e2.delete(0,END)
 e3.delete(0,END)
 e4.delete(0,END)
 e5.delete(0,END)
 e6.delete(0,END)
 connection.commit()

def query():
  t1= e8.get()
  crsr.execute("select * from library where oid=" +t1) 
  ans=crsr.fetchall() 
  
  res=""
  for i in ans:
    res+=str(i[0])+" "+i[1]+" "+i[2]+" "+i[3]+" "+i[4]+" "+i[5]
  l9=Label(screen, text=res)
  l9.grid(row=8, column=0, columnspan=4)
  connection.commit()
  

def edit():
  crsr.execute("""update library set 
              studentID=:sID,
              bookID=:bID,
              s_name=:sname,
              b_name=:bname,
              doi=:date_Issued,
              dor=:date_Returned
              where oid=:Aid
               """,{
               "sID":e11.get(),
               "bID":e12.get(),
               "sname":e13.get(),
               "bname":e14.get(),
               "date_Issued":e15.get(),
               "date_Returned":e16.get(),
               "Aid":e8.get()
               })
  connection.commit()
  screen2.destroy()

def update():
  global screen2
  screen2=Tk()
  l11= Label(screen2, text="Student ID")
  l11.grid(row=0, column=0)
  sn1= IntVar()
  global e11
  e11= Entry(screen2, textvariable=sn1)
  e11.grid(row=0, column=1)

  l12= Label(screen2, text="Book ID")
  l12.grid(row=1, column=0)
  f1n= StringVar()
  global e12
  e12= Entry(screen2, textvariable=f1n)
  e12.grid(row=1, column=1)

  l13= Label(screen2, text="Student Name")
  l13.grid(row=2, column=0)
  l1n=StringVar()
  global e13
  e13= Entry(screen2, textvariable=l1n)
  e13.grid(row=2, column=1)

  l14= Label(screen2, text="Book Name")
  l14.grid(row=3, column=0)
  g1=StringVar()
  global e14
  e14= Entry(screen2, textvariable=g1)
  e14.grid(row=3, column=1)

  l15= Label(screen2, text="Date of Issue")
  l15.grid(row=4, column=0)
  d1=StringVar()
  global e15
  e15= Entry(screen2, textvariable=d1)
  e15.grid(row=4, column=1)

  l16= Label(screen2, text="Date of Return")
  l16.grid(row=5, column=0)
  d1=StringVar()
  global e16
  e16= Entry(screen2, textvariable=d1)
  e16.grid(row=5, column=1)

  t1= e8.get()
  crsr.execute("select * from library where oid=" +t1) 
  ans=crsr.fetchall() 

  res=""
  for i in ans:
    e11.insert(0,i[0])
    e12.insert(0,i[1])
    e13.insert(0,i[2])
    e14.insert(0,i[3])
    e15.insert(0,i[4]) 
    e16.insert(0,i[5]) 

  connection.commit()
  b11=Button(screen2, text="Update database", command= edit)
  b11.grid(row=6, column=0, columnspan=3)






l1= Label(screen, text="Student ID")
l1.grid(row=0, column=0)
sn= IntVar()
e1= Entry(screen, textvariable=sn)
e1.grid(row=0, column=1)

l2= Label(screen, text="Book ID")
l2.grid(row=1, column=0)
fn= StringVar()
e2= Entry(screen, textvariable=fn)
e2.grid(row=1, column=1)

l3= Label(screen, text="Student Name")
l3.grid(row=2, column=0)
ln=StringVar()
e3= Entry(screen, textvariable=ln)
e3.grid(row=2, column=1)

l4= Label(screen, text="Book Name")
l4.grid(row=3, column=0)
g=StringVar()
e4= Entry(screen, textvariable=g)
e4.grid(row=3, column=1)

l5= Label(screen, text="Date of Issue")
l5.grid(row=4, column=0)
d=StringVar()
e5= Entry(screen, textvariable=d)
e5.grid(row=4, column=1)

l6= Label(screen, text="Date of Return")
l6.grid(row=5, column=0)
d=StringVar()
e6= Entry(screen, textvariable=d)
e6.grid(row=5, column=1)

b1=Button(screen, text="Add record to database", command= add)
b1.grid(row=6, column=0, columnspan=3)

enterID= Label(screen, text="Enter your Student ID")
enterID.grid(row=7, column=0)
global e8 
e8=Entry(screen)
e8.grid(row=7, column=1)

b2=Button(screen, text="Query to database", command= query)
b2.grid(row=9, column=0, columnspan=3)

b3=Button(screen, text="Edit", command= update)
b3.grid(row=10, column=0, columnspan=3)

mainloop()