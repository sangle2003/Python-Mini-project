class person:
    def __init__(self):
        self.name=input("Enter Name :: ")
        
class Student(person):
    def __init__(self):
        super().__init__()
        self.roll = int(input("Enter roll number :: "))
    
    def display(self):
        print("Name is :: ", self.name)
        print("Roll number is :: ", self.roll)
        
s = Student()
s.display()