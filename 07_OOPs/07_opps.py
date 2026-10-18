class Student:
    def __init__(self,name ):
        self.name = name
        
s = Student("pradip")
print("Current name :: ",s.name)

s.name = "ved"
print("Updated name :: ",s.name )