#Create a Student class. Use a constructor to initialize name, maths, science, and english. Create methods to calculate:
class Student:
    def __init__(self,name,maths,science,english):
        self.name = name 
        self.maths = maths
        self.science = science
        self.english = english
        
    def TotalMarks(self):
        total_marks = self.maths + self.science + self.english
        print("Total marks :: ",total_marks)
        
    def percentage(self):
        percentage = (self.maths + self.science + self.english ) / 3
        print("persentage :: ",percentage)

name = input("Enter your name :: ")
maths = int(input("Enter your maths marks :: "))        
science = int (input("Enter your science marks :: "))
english = int (input("Enter your english marks :: "))

s1 = Student(name,maths,science,english)
print("name :: ",s1.name)
print("total marks :: ",s1.TotalMarks())
print("percentage :: ",s1.percentage())

        