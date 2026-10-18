#Create an Employee class. Use a constructor to initialize name, salary, and department. Display the employee details.
class Employee:
    def __init__(self,name,salary,deparment):
        self.name = name 
        self.salary = salary
        self.department = deparment
        
    def dispaly(self):
        print("Name :: ",self.name )
        print("salary :: ",self.salary)
        print("department :: ",self.department)
        
e1 = Employee("pradip",10000,"markating")

print(e1.dispaly())
        