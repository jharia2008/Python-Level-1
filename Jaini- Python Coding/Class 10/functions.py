#there are 2 types of functions: one is inbuilt and second one is user define
#inbuilt functions are those function which are given to us by python and they do some specific task
#user define functions are like a group where a code is being stored for reusing the code, and to make it more organized 
name= input("enter your name")
def greet():
    print("hey, " + name)
greet()

a=int(input("enter a number"))
b=int(input("enter another number"))
def product():
    print(a*b)
product()