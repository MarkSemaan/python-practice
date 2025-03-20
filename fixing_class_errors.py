#First, Class Student did not inherit name (add super)
#Second, dsplay grade won't output format since there's no f in the print
#Third, in display grade, it's self.name and not name
#Fourth, in display grade, it's self.grade and not grade
#Fith, we should create a student object, not a person object.

class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
    def displayGrade(self):
        print(f"{self.name} : {self.grade}")

p = Student("Nabiha", 10)
p.displayGrade()