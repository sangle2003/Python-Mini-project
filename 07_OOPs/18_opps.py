class person:
    def p(self):
        self.name=input("Enter Name :: ")
        
class Employee(person):
    def e(self):
        self.id=int(input("Enter ID :: "))
        
class Student(person):
    def s(self):
        self.course=input("Enter Course :: ")
        
class Intern(Employee,Student):
    def i(self):
        print(self.name, self.id, self.course)
        
bj =Intern()
bj.p()
bj.e()
bj.s()
bj.i()