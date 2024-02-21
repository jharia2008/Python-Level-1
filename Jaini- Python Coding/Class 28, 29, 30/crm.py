from tkinter import *
import mysql.connector #after installing mysql database, mysql.connector needs to be installed via command prompt : pip install mysql-connector-python
screen = Tk()
#to connect with mysql, mysql.connector.connect is used along with the username and password and the host which was given when installing mysql
#the rest of the coding of create table, insert, update, delete is going to be the same as sqlite
mydb=mysql.connector.connect(host="localhost", user="root", password="Mahaviris24!", database= "custom") #mention the database you want to use here
print(mydb) #execute til here to check if the connection is established or not
crsr=mydb.cursor()
#how to create a database
#crsr.execute("CREATE DATABASE custom")
#to check all the databases, show databases will show all the inbuilt databases and databases created by the user
crsr.execute("SHOW DATABASES")
#use for loop to get the names and print
for i in crsr:
    print(i)
#crsr.execute('CREATE TABLE customer2 (id INT  PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), address1 VARCHAR(255),address2 VARCHAR(255),city VARCHAR(255), state VARCHAR(255), country VARCHAR(255), zip VARCHAR(5), phone VARCHAR(255), email VARCHAR(255), payment VARCHAR(255), discount VARCHAR(255), price VARCHAR(255))')

"""def add():
 crsr.execute("INSERT INTO customer2 VALUES (:id, :first_name,  :last_name , :address1 , :address2 , :city, :state, :zip, :country, :phone, :email, :payment, :discount, :price)",
        {
            'id' : e1.get(),
            'first_name' : e2.get(),
            'last_name' : e3.get(),
            'address1' : e4.get(),
            'address2' : e5.get(),
            'city' : e6.get(),
            'state' : e7.get(),
            'zip' : e8.get(),
            'country' : e9.get(),
            'phone' : e10.get(),
            'email' : e11.get(),
            'payment' : e12.get(),
            'discount' : e13.get(),
            'price' : e14.get()
        }
    )
 e1.delete(0,END)
 e2.delete(0,END)
 e3.delete(0,END)
 e4.delete(0,END)
 e5.delete(0,END)
 e6.delete(0,END)
 e7.delete(0,END)
 e8.delete(0,END)
 e9.delete(0,END)
 e10.delete(0,END)
 e12.delete(0,END)
 e13.delete(0,END)
 e14.delete(0,END)
 mydb.commit()
"""

def add():
   sql="insert into customer2(id, first_name, last_name, address1, address2, city, state, zip, country, phone, email, payment, discount, price) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
   values=(e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get(), e8.get(), e9.get(), e10.get(), e11.get(), e12.get(), e13.get(), e14.get())
   crsr.execute(sql, values)

   e1.delete(0,END)
   e2.delete(0,END)
   e3.delete(0,END)
   e4.delete(0,END)
   e5.delete(0,END)
   e6.delete(0,END)
   e7.delete(0,END)
   e8.delete(0,END)
   e9.delete(0,END)
   e10.delete(0,END)
   e12.delete(0,END)
   e13.delete(0,END)
   e14.delete(0,END)
   mydb.commit()

def query():
  t1= e15.get()
  crsr.execute("select * from customer2 where id=" +t1) 
  ans=crsr.fetchall() 
  res=""
  for i in ans:
    res+=str(i[0])+" "+i[1]+" "+i[2]+" "+i[3]+" "+i[4]
  l16=Label(screen, text=res)
  l16.grid(row=18, column=0)
  mydb.commit()

def edit():
  id=ea1.get()
  first_name=ea2.get()
  last_name=ea3.get()
  address1=ea4.get()
  address2=ea5.get()
  city=ea6.get()
  state=ea7.get()
  zip=ea8.get()
  country=ea9.get()
  phone=ea10.get()
  email=ea11.get()
  payment=ea12.get()
  discount=ea13.get()
  price=ea14.get()
  aid=e15.get()
  Update="Update customer2 set id='%s', first_name='%s', last_name='%s', address1='%s', address2='%s', city='%s', state='%s', zip='%s', country='%s', phone='%s', email='%s', payment='%s', discount='%s', price='%s' where id='%s'" %(id,first_name,last_name,address1,address2,city,state,zip,country,phone,email,payment,discount,price,aid)
  crsr.execute(Update)
  mydb.commit()
  screen2.destroy()

def update():
   global screen2
   screen2=Tk()
   la1=Label(screen2, text="Customer Database")
   la1.grid(row=0, column=0, columnspan=5)

   la20=Label(screen2, text="Enter your ID")
   la20.grid(row=1,column=0)
   global ea1
   ea1=Entry(screen2)
   ea1.grid(row=1, column=1, columnspan=3)

   la2=Label(screen2, text="First Name")
   la2.grid(row=2, column=0)
   global ea2
   ea2=Entry(screen2)
   ea2.grid(row=2, column=1, columnspan=3)

   la3=Label(screen2, text="Last Name")
   la3.grid(row=3, column=0)
   global ea3
   ea3=Entry(screen2)
   ea3.grid(row=3, column=1, columnspan=3)

   la4=Label(screen2, text="Address 1")
   la4.grid(row=4, column=0)
   global ea4
   ea4=Entry(screen2)
   ea4.grid(row=4, column=1, columnspan=3)

   la5=Label(screen2, text="Address 2")
   la5.grid(row=5, column=0)
   global ea5
   ea5=Entry(screen2)
   ea5.grid(row=5, column=1, columnspan=3)

   la6=Label(screen2, text="City")
   la6.grid(row=6, column=0)
   global ea6
   ea6=Entry(screen2)
   ea6.grid(row=6, column=1, columnspan=3)

   la7=Label(screen2, text="State")
   la7.grid(row=7, column=0)
   global ea7
   ea7=Entry(screen2)
   ea7.grid(row=7, column=1, columnspan=3)
 
   la8=Label(screen2, text="Zipcode")
   la8.grid(row=8, column=0)
   global ea8
   ea8=Entry(screen2)
   ea8.grid(row=8, column=1, columnspan=3)

   la9=Label(screen2, text="Country")
   la9.grid(row=9, column=0)
   global ea9
   ea9=Entry(screen2)
   ea9.grid(row=9, column=1, columnspan=3)

   la10=Label(screen2, text="Phone Number")
   la10.grid(row=10, column=0)
   global ea10
   ea10=Entry(screen2)
   ea10.grid(row=10, column=1, columnspan=3)

   la11=Label(screen2, text="Email Address")
   la11.grid(row=11, column=0)
   global ea11
   ea11=Entry(screen2)
   ea11.grid(row=11, column=1, columnspan=3)

   la12=Label(screen2, text="Payment Method")
   la12.grid(row=12, column=0)
   global ea12
   ea12=Entry(screen2)
   ea12.grid(row=12, column=1, columnspan=3)

   la13=Label(screen2, text="Discount Code")
   la13.grid(row=13, column=0)
   global ea13
   ea13=Entry(screen2)
   ea13.grid(row=13, column=1, columnspan=3)

   la14=Label(screen2, text="Price Paid")
   la14.grid(row=14, column=0)
   global ea14
   ea14=Entry(screen2)
   ea14.grid(row=14, column=1, columnspan=3) 

   t1= e15.get()
   crsr.execute("select * from customer2 where id="+t1)
   ans=crsr.fetchall()

   res=""
   for i in ans:
      ea1.insert(0,i[0])
      ea2.insert(0,i[1])
      ea3.insert(0,i[2])
      ea4.insert(0,i[3])
      ea5.insert(0,i[4])
      ea6.insert(0,i[5])
      ea7.insert(0,i[6])
      ea8.insert(0,i[7])
      ea9.insert(0,i[8])
      ea10.insert(0,i[9])
      ea11.insert(0,i[10])
      ea12.insert(0,i[11])
      ea13.insert(0,i[12])
      ea14.insert(0,i[13])
    
   mydb.commit()
   ba1=Button(screen2, text="Update Database", command= edit)
   ba1.grid(row=15,column=0, columnspan=2)
   
def delete():
   crsr.execute("delete from customer2 where id="+e15.get())
   mydb.commit()

l1=Label(screen, text="Customer Database")
l1.grid(row=0, column=0, columnspan=5)

l20=Label(screen, text="Enter your ID")
l20.grid(row=1,column=0)
e1=Entry(screen)
e1.grid(row=1, column=1, columnspan=3)

l2=Label(screen, text="First Name")
l2.grid(row=2, column=0)
e2=Entry(screen)
e2.grid(row=2, column=1, columnspan=3)

l3=Label(screen, text="Last Name")
l3.grid(row=3, column=0)
e3=Entry(screen)
e3.grid(row=3, column=1, columnspan=3)

l4=Label(screen, text="Address 1")
l4.grid(row=4, column=0)
e4=Entry(screen)
e4.grid(row=4, column=1, columnspan=3)

l5=Label(screen, text="Address 2")
l5.grid(row=5, column=0)
e5=Entry(screen)
e5.grid(row=5, column=1, columnspan=3)

l6=Label(screen, text="City")
l6.grid(row=6, column=0)
e6=Entry(screen)
e6.grid(row=6, column=1, columnspan=3)

l7=Label(screen, text="State")
l7.grid(row=7, column=0)
e7=Entry(screen)
e7.grid(row=7, column=1, columnspan=3)

l8=Label(screen, text="Zipcode")
l8.grid(row=8, column=0)
e8=Entry(screen)
e8.grid(row=8, column=1, columnspan=3)

l9=Label(screen, text="Country")
l9.grid(row=9, column=0)
e9=Entry(screen)
e9.grid(row=9, column=1, columnspan=3)

l10=Label(screen, text="Phone Number")
l10.grid(row=10, column=0)
e10=Entry(screen)
e10.grid(row=10, column=1, columnspan=3)

l11=Label(screen, text="Email Address")
l11.grid(row=11, column=0)
e11=Entry(screen)
e11.grid(row=11, column=1, columnspan=3)

l12=Label(screen, text="Payment Method")
l12.grid(row=12, column=0)
e12=Entry(screen)
e12.grid(row=12, column=1, columnspan=3)

l13=Label(screen, text="Discount Code")
l13.grid(row=13, column=0)
e13=Entry(screen)
e13.grid(row=13, column=1, columnspan=3)

l14=Label(screen, text="Price Paid")
l14.grid(row=14, column=0)
e14=Entry(screen)
e14.grid(row=14, column=1, columnspan=3)

b1=Button(screen, text="Add Customer to Database", command= add)
b1.grid(row=15,column=0, columnspan=2)

b2=Button(screen, text="Clear Fields")
b2.grid(row=15,column=2, columnspan=2)

b3=Button(screen,text="Delete Customer", command=delete)
b3.grid(row=15, column=4, columnspan=2)

b4=Button(screen, text="List Customer", command= query)
b4.grid(row=16,column=0, columnspan=2)

b5=Button(screen, text="Search/Edit Customers", command=update)
b5.grid(row=16,column=2, columnspan=2)

l15=Label(screen, text="Enter ID")
l15.grid(row=17,column=0)
e15=Entry(screen)
e15.grid(row=17, column=1, columnspan=3)



mainloop()