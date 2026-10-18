#Create an Employee class with name and salary. If salary is greater than ₹50,000, print "High Salary", otherwise print "Normal Salary".
class Employee:
    def __init__(self,name,salary):
        
        self.name = name 
        self.salary = salary
        
    def greater(self):
        if self.salary > 50000:
            print("High salary")
        else:
            print("Normal salary")
            
name = input("Enter your name :: ")
salary = float(input("Enter your salary :: "))

e1 = Employee(name,salary)
e1.greater()
        