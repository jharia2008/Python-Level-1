#objects are the things in java
#classes are the blueprints of the objects
#init functions is inbuilt function ALWAYS used inside the class and they hold properties
#self. is always used whenever you give the properties
class Bank: 
    def __init__(self, name, accountNumber):
        self.name= name
        self.accountnumber= accountNumber
        self.balance= 4000
    def deposit(self):
        a= int(input("Enter your amount"))
        self.balance=self.balance + a
        print(self.balance)
    def withdraw(self):
        b= int(input("How much money would you like to withdraw."))
        self.balance = self.balance - b
        print(self.balance)
#syntax to create an object is first the object name and then the object
customer1= Bank("Jaini", 3456)
print(customer1.deposit())
print(customer1.withdraw())