"""sqlite is a database which can hold data. its an inbuilt database so no installation requires also it is in the form of library, but it can only hold small data and cannot hold large data. that means sqlite is good to make only small softwares/applications, not big ones
Steps to follow for sqlite:
1. import sqlite
2. use connect function to connect with database. If database name mentioned exits it will get connected to that database otherwise a new database ill be created.
3. use cursor function to create cursor object
4. create table using create bale query :
syntax : create table tablename(columname1 datatype, columname2 datatype.......)
use cursor to finally execute at the end of  every query
Note : cusor is import to execute at the end of all queries as it does the final execution
5. Use insert command to insert data. 
syntax : insert into tablename(colunname1, columname2...) values(data values)
use cursor to execute the query.
6. use select and fetch all to fetch data from database
7. Use update query to update data
8. use delete to delete data
9. After this use commit save all data
10. close can also be used to close the connection"""

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
#sql="""insert into employee(staff_Number, first_Name, last_Name, gender, doj) values(10,"Jaini", "Haria", "female", "7/3/23")"""
#crsr.execute(sql)
#in this function, variables have been created in a dictionary, where we are getting the value of all the entry boxes
#and then those variables are  given to the insert query in the value part, so that data can be inserted
def add():
 crsr.execute("INSERT INTO employee VALUES (:Staffno,  :f_name , :l_name , :Gender , :DOJi)",
        {
            'Staffno' : e1.get(),
            'f_name' : e2.get(),
            'l_name' : e3.get(),
            'Gender' : e4.get(),
            'DOJi' : e5.get()
        }
    )
 e1.delete(0,END) #delete function is used to delete anything from the text box and insert is used to insert anything inside the textbox
 e2.delete(0,END)
 e3.delete(0,END)
 e4.delete(0,END)
 e5.delete(0,END)
 connection.commit()

def query():
  #to retreive the data there are 2 steps
  #1 step- you select query to select the whole table data
  #2 step- use fetchall function to get data from database to the screen
  t1= e8.get() #we get the id from e8 to t1
  crsr.execute("select * from employee where oid=" +t1) # * means all ; after where we have given the id through t1 variable, the employee whose id has been selected
  ans=crsr.fetchall() #this fetchs all the data into the variable ans
  #now we will use for loop in ans and move ans to the screen 
  res=""
  for i in ans:
    res+=str(i[0])+" "+i[1]+" "+i[2]+" "+i[3]+" "+i[4]
  l9=Label(screen, text=res)
  l9.grid(row=8, column=0)
  connection.commit()

def edit():
  crsr.execute("""update employee set 
              staff_Number=:s_Number,
              first_Name=:f_Name,
              last_Name=:l_Name,
              gender=:g_Gender,
              doj=:date_Joined
              where oid=:Aid
               """,{
               "s_Number":e11.get(),
               "f_Name":e12.get(),
               "l_Name":e13.get(),
               "g_Gender":e14.get(),
               "date_Joined":e15.get(),
               "Aid":e8.get()
               })
  connection.commit()
  screen2.destroy()


def update():
  global screen2
  screen2=Tk()
  l11= Label(screen2, text="Staff Number")
  l11.grid(row=0, column=0)
  sn1= IntVar()
  global e11
  e11= Entry(screen2, textvariable=sn1)
  e11.grid(row=0, column=1)

  l12= Label(screen2, text="First Name")
  l12.grid(row=1, column=0)
  f1n= StringVar()
  global e12
  e12= Entry(screen2, textvariable=f1n)
  e12.grid(row=1, column=1)

  l13= Label(screen2, text="Last Name")
  l13.grid(row=2, column=0)
  l1n=StringVar()
  global e13
  e13= Entry(screen2, textvariable=l1n)
  e13.grid(row=2, column=1)

  l14= Label(screen2, text="Gender")
  l14.grid(row=3, column=0)
  g1=StringVar()
  global e14
  e14= Entry(screen2, textvariable=g1)
  e14.grid(row=3, column=1)

  l15= Label(screen2, text="Date of Joining")
  l15.grid(row=4, column=0)
  d1=StringVar()
  global e15
  e15= Entry(screen2, textvariable=d1)
  e15.grid(row=4, column=1)

  t1= e8.get() #we get the id from e8 to t1
  crsr.execute("select * from employee where oid=" +t1) # * means all ; after where we have given the id through t1 variable, the employee whose id has been selected
  ans=crsr.fetchall() #this fetchs all the data into the variable ans
  #now we will use for loop in ans and move ans to the screen 
  res=""
  for i in ans:
    e11.insert(0,i[0])
    e12.insert(0,i[1])
    e13.insert(0,i[2])
    e14.insert(0,i[3])
    e15.insert(0,i[4]) #get is used to get the data from the textboxes and insert is used to insert the data in the textboxes and whatever data is coming from the database, we are inserting here on the second page

  connection.commit()
  b11=Button(screen2, text="Submit", command= edit)
  b11.grid(row=5, column=0, columnspan=3)

def delete():
  crsr.execute("delete from employee where oid ="+e8.get())
  connection.commit()



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

enterID= Label(screen, text="Enter the ID")
enterID.grid(row=6, column=0)
global e8 #declare the variables as global when different functions are going to share the same variable
e8=Entry(screen)
e8.grid(row=6, column=1)

b2=Button(screen, text="Query to database", command= query)
b2.grid(row=7, column=0, columnspan=3)

b3=Button(screen, text="Edit", command= update)
b3.grid(row=9, column=0, columnspan=3)

b10=Button(screen, text="Delete", command= delete)
b10.grid(row=10,column=0, columnspan=3)

mainloop()
exit()