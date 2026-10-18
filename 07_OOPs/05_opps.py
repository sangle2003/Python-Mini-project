class Employee:
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal
        
    def display(self):
        print("Name is :: ",self.name)
        print("sal is :: ",self.sal)
        
e1=Employee("Ram",5000)
e2=Employee("Pradip",2000)

e1.display()
e2.display()
        