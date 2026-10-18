class Employee:
    def emp(self):
        self.name=input("Enter Name :: ")

class Developer(Employee):
    def dev(self):
        print(self.name , "is a Developer ")

class Tester(Employee):
    def test(self):
        print(self.name," is a tester ")

class SQLManager(Employee):
    def sql(self):
        print(self.name, " is a SQL Manager ")
        
d = Developer()
d.emp()
d.dev()

t = Tester()
t.emp()
t.test()

s = SQLManager()
s.emp()
s.sql()

