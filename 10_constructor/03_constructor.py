class student:
    def __init__(self,name,course):
        
        self.name = name
        self.course = course
        
    def display(self):
        print("======== student detail ==========")
        print("student name :: ",self.name)
        print("student course :: ",self.course)
        
n1 = input("Enter your name :: ")
c1 = input("Enter your course :: ")
s1 = student(n1,c1)
s1.display()

n2 = input("Enter your name :: ")
c2 = input ("Enter your course :: ")
s2 = student(n2,c2)
s2.display()
        