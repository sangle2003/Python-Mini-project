from abc import ABC, abstractmethod

# Abstract Class
class Employee (ABC):

    def _init_(self, name, salary):
        self. name = name
        self. salary = salary

# Concrete Method
    def display_details(self):
        print("Employee Name:", self.name)
        print("Salary:", self. salary)

# Abstract Method
@abstractmethod
def calculate_bonus(self):
    pass

# Single Inheritance
class Developer(Employee):

    def calculate_bonus(self):
        return self.salary * 0.10

# Hierarchical Inheritance
class Tester(Employee):

    def calculate_bonus(self):
        return self.salary * 0.08


class Manager(Employee):

    def calculate_bonus(self):
        return self.salary * 0.10
    
# Hierarchical Inheritance
class Tester(Employee):

    def calculate_bonus(self):
        return self.salary * 0.08

class Manager(Employee):

    def calculate_bonus(self):
        return self.salary * 0.15
    
# Multilevel Inheritance
class TeamLead(Developer):

    def team_management(self):
        print("Team Lead manages development team")

class SeniorTeamLead(TeamLead):

    def project_management(self):
        print("Senior Team Lead manages multiple projects")
        
#object 

d = Developer("Rahul",60000)
d.display_details()
print("Bonus:", d.calculate_bonus())


t = Tester("Priya", 50000)
t.display_details()
print("Bonus:", t.calculate_bonus())

print("------------------------")       

m = Manager("Amit", 80000)
m.display_details()
print("Bonus:", m.calculate_bonus())

print("---------------------")

st = SeniorTeamLead("Neha", 100000)
st.display_details()
print("Bonus:", st.calculate_bonus())
st. team_management()