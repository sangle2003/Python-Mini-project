
# Single Inheritance

class Employee:
    def show(self):
        print("Employee details")

# Child class
class Developer(Employee):
    def code(self):
        print("Developer is writing the code!")

d = Developer()
d.code()
d.show()
