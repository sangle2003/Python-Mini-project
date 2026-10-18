class student:
    def __init__(self,marks):
        self._marks = marks
        
    @property
    def marks (self):
        return self._marks 
    
s = student(90)
print(s.marks) 