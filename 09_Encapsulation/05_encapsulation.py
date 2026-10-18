#getter and setter method 
class Employee:
    def __init__(self):
        self.__salary = 0
        
    def set_salary(self,s):
        if s > 0:
            self.__salary = s
            
    def get_salary(self):
        return self.__salary
    
e = Employee()
e.set_salary(10000)
print("Salary is :: ",e.get_salary())