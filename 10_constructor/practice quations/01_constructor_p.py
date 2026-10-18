#Create a Student class. Use a constructor to initialize name and age. Print both values.
class student:
    def __init__(self,name,age ):
        
        self.name = name 
        self.age = age
        
name = input ("ENter your name :: ")
age = int(input("Enter your age :: "))

s1 = student (name,age )

print("Student name :: ",s1.name )
print("student age :: ",s1.age )
        
        
            