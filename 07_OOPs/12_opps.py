class Person:
    def p(self):
        self.name=input("Enter Name :: ")

class Employee(Person):
    def e(self):
        self.id=int(input("Enter ID :: "))

class Manager(Employee):
    def m(self):
        print(self.name, self.id)

m=Manager()
m.p()
m.e()
m.m()