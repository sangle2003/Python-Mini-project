class Student:
    school_name = "ABC school"
    
    @classmethod 
    def change_school(cls,name):
        cls.school_name = name 
        
Student.change_school("XYZ school")
print(Student.school_name)