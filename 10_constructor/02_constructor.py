#parametrize constructor

class Student:
    def __init__(self,rollno,name,course):
        self.rollno = rollno
        self.name = name
        self.course = course
        
s1 = Student(22,"pradip","datascience")
s2 = Student(3,"ved","cloud")

print(s1.rollno, s1.name, s1.course)
print(s2.rollno, s2.name, s2.course)