class Student:
    def __init__(self):
        self._marks = 0
        
    @property
    def marks(self):
        return self._marks 
    
    @marks.setter
    def marks(self,value):
        if value < 0:
            print("Invalid marks ")
            
        else:
            self._marks = value
            
s = Student()
s.marks = 85
print(s.marks)