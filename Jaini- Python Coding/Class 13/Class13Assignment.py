#create a class which will have all the student details and functions that students do in school
#and from there create the multiple student objects
#student properties: names, age, class
#student functions: grades, extracurricular activities(clubs, sports, etc.)
class Student:
    def __init__(self, name, age, standard, grades, activities):
        self.name=name 
        self.age=age
        self.standard= standard
        self.grades= grades
        self.activities=activities
    def SchoolGrade(self):
        GRADE=str(input("Enter your average grade."))
        self.grades= GRADE
        print("Your average grades are " + self.grades)
    def SchoolActivity(self):
        ACTIVITY=str(input("Enter any clubs or sports you are taking part in this year."))
        self.activities= ACTIVITY
        print("You are participating in " + self.activities)
student1= Student("Jaini", "14", "9", "95%", "volleyball")
print(student1.SchoolGrade())
print(student1.SchoolActivity())