class Employee:
    def accept(self,name,salary):
        self.name = name 
        self.salary = salary
        
        def display(self):
            print("Name is :: ",self.name)
            print("salary is :: ",self.salary)
            
e1=Employee()
e2=Employee()

e1.accept("Ram",5000)
e2.accept("Raj",3000)  
e1.display()
e2.display()
 