class student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        
    def display(self):
        print("name :: ",self.name)
        print("marks1 :: ",self.marks1)
        print("marks2 :: ",self.marks2)
        print("marks 3 :: ",self.marks3)
        
s1 = student("pradip",22,23,25)
s1.display()
        