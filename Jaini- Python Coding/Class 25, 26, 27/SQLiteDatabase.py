from tkinter import *
import sqlite3
screen= Tk()
#first step - to connect with the SQLite database and create the database at the same time
connection=sqlite3.connect("mydb.db") #you can mention any name of the database
#second step - use a cursor function that will help execute all your queries
crsr=connection.cursor()
#data in the database is ALWAYS stored in the form of a table
#third step - create a table
#syntax to create table - """create table name of the table (columnName1, columnName2, columnName3...)""""
#along with the column name, you need to mention the datatype like text, varchar, int, decimal
#primary key means a column which is unique and no data inside it will be duplicated
#ALWAYS AT LEAST ONE COLUMN HAS TO BE PRIMARY KEY
#sql = """create table employee(
#staff_Number integer primary key autoincrement,
#first_Name varchar(70),
#last_Name varchar(70),
#gender varchar(20),
#doj varchar(50)
#)"""
#step four - cursor will execute the sql query
#crsr.execute(sql)

# -----insert data-----
#manual insertation through coding
sql="""insert into employee(staff_Number, first_Name, last_Name, gender, doj) values(1,"Jaini", "Haria", "female", "7/3/23")"""
crsr.execute(sql)

def add():
  sql = "insert into employee(first_Name, last_Name, gender, doj) values(:fname, :lname, :gender, :doj)"
  crsr.execute(sql, {"fname": fn.get(), "lname":ln.get(),"gender": g.get(), "doj": d.get()})

def query():
  #to retreive the data there are 2 steps
  #1 step- you select query to select the whole table data
  #2 step- use fetchall function to get data from database to the screen
  sql= "select*,oid from employee" # * means all
  crsr.execute(sql)
  ans=crsr.fetchall() #this fetchs all the data into the variable ans
  #now we will use for loop in ans and move ans to the screen 


l1= Label(screen, text="Staff Number")
l1.grid(row=0, column=0)
sn= IntVar()
e1= Entry(screen, textvariable=sn)
e1.grid(row=0, column=1)

l2= Label(screen, text="First Name")
l2.grid(row=1, column=0)
fn= StringVar()
e2= Entry(screen, textvariable=fn)
e2.grid(row=1, column=1)

l3= Label(screen, text="Last Name")
l3.grid(row=2, column=0)
ln=StringVar()
e3= Entry(screen, textvariable=ln)
e3.grid(row=2, column=1)

l4= Label(screen, text="Gender")
l4.grid(row=3, column=0)
g=StringVar()
e4= Entry(screen, textvariable=g)
e4.grid(row=3, column=1)

l5= Label(screen, text="Date of Joining")
l5.grid(row=4, column=0)
d=StringVar()
e5= Entry(screen, textvariable=d)
e5.grid(row=4, column=1)

b1=Button(screen, text="Add record to database", command= add)
b1.grid(row=5, column=0, columnspan=3)

b2=Button(screen, text="Query to database")
b2.grid(row=6, column=0, columnspan=3)

mainloop()