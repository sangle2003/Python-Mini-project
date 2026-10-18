# protection

class Employee:
    def __init__(self):
        self._salary = 10000
        
class Child(Employee):
    def show(self):
        print("Salary is :: ",self._salary)
        
c = Child()
c.show()