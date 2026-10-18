#Create a Student class with name and marks. Display the grade:
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        if self.marks > 90:
            print("Gread A")
        elif self.marks > 75:
            print("Gread B")
        elif self.marks > 60:
            print("Gread C")
        elif self.marks>50:
            print("Gread D")
        else:
            print("Fail")
            
name = input("Enter your name :: ")
marks = int (input("Enter your marks :: "))

s1 = Student(name,marks)
print("name :: ",s1.name)
print(s1.display())