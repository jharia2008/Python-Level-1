#method overriding: in this 2 functions have the same function name and variable name, one in parent and one in child, so the newer function in the child class replaces the one in the parent
class Employee:
    def __init__(self, name, age, salary, job):
        self.name= name 
        self.age= age
        self.salary= salary
        self.job= job
    def yearlySalary(self):
        a=str(input("Enter the name of your job"))
        print("Your job is " + a)
    def yearlySalary(self):
        b=int(input("Enter your yearly salary."))
        c=int(input("Enter any bonuses or advances."))
        self.salary= str(b + c)
        print("Your yearly salary is " + self.salary)
employee1=Employee("Jaini", "14", "14,000", "cashier")
print(employee1.yearlySalary())