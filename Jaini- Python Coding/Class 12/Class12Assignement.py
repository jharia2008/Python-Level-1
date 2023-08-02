class Student: 
    def __init__(self, name, school, grades):
        self.name= name
        self.school= school
        self.grades= grades
    def grades(self):
        recent= int(input("Enter your recent grades"))
        self.grades= recent
        print("Your grades are " + self.grades)
    def school(self):
        b= int(input("Enter the name of your school."))
        self.school = b
        print("Your school is " + self.school)
class WorkingStudent:
    def __init__(self, name, school, grades, salary):
        self.name= name
        self.school= school
        self.grades= grades
        self.salary= salary
    Student.grades
    Student.school
    def salary(self):
        c=int(input("Enter your current salary."))
        self.salary= c
        print("Your salary is " + self.salary)
student1= WorkingStudent("Jaini", "Stem Academy", "A", "$12")
print(student1.grades())
print(student1.school())
print(student1.salary())