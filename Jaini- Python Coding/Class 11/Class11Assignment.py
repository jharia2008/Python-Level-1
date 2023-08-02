class Employee: 
    def __init__(self, name, age, IDdetails, salesMan):
        self.name= name
        self.age= age
        self.IDdetails= IDdetails
        self.salary= 60,000
        self.position= salesMan
    def bonus(self):
        increase= int(input("Enter your salary increase"))
        self.salary=self.salary + increase
        print("Your salary is " + self.salary)
    def timing(self):
        b= int(input("Enter the extra hours you have worked."))
        self.salary = self.salary + (20*b)
        print("Your salary is " + self.salary)
    def position(self):
        newPosition=input("Enter your new position.")
        self.position= newPosition
        print("Your new position is " + self.position)
employee1= Employee("Jaini", 14, 37291)
print(employee1.bonus())
print(employee1.timing())
print(employee1.position())