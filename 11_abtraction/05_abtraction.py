from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def salary(self):
        pass


class Developer(Employee):

    def __init__(self, sal):
        self.sal = sal

    def salary(self):
        return self.sal


class Accountant(Employee):

    def __init__(self, sal):
        self.sal = sal

    def salary(self):
        return self.sal


class Manager(Employee):

    def __init__(self, sal):
        self.sal = sal

    def salary(self):
        return self.sal


class Tester(Employee):

    def __init__(self, sal):
        self.sal = sal

    def salary(self):
        return self.sal


# Developer
basesal = int(input("Enter Developer Salary :: "))
d = Developer(basesal)
print("Salary Of Developer is :: ", d.salary())


# Accountant
basesal = int(input("Enter Accountant Salary :: "))
acc = Accountant(basesal)
print("Salary Of Accountant is :: ", acc.salary())


# Manager
basesal = int(input("Enter Manager Salary :: "))
m = Manager(basesal)
print("Salary Of Manager is :: ", m.salary())


# Tester
basesal = int(input("Enter Tester Salary :: "))
t = Tester(basesal)
print("Salary Of Tester is :: ", t.salary())