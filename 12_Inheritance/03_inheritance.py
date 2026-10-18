class person:
    def get_name(self):
        self.name = input("Enter your name :: ")
        
class Student(person):
    def get_student(self):
        self.marks = int(input("Enter your marks :: "))
        print(self.name," has marks ",self.marks)
        
s1 = Student()
s1.get_name()
s1.get_student()

s2 = Student()
s2.get_name()
s2.get_student()
