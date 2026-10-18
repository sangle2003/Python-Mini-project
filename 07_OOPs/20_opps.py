class person:
    def display(self):
        print("I am person")
        
class Student(person):
    def show(self):
        super().display()
        print("I am student")
        
s = Student()
s.show()