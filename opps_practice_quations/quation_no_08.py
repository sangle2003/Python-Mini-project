class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department =department
        
    def display(self):
        print("name :: ",self.name)
        print("salary :: ",self.salary)
        print("department :: ",self.department)
        
e1 = Employee("pradip",2000,"computer")
e1.display()
        