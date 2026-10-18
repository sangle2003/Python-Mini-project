#private

class student:
    def __init__(self):
        self.__marks = 90
        
    #getter method
    def get__marks(self):
        return self.__marks
    
s = student()
#print(s.marks)
#print(s.__marks) #error

print("marks value is :: ",s.get__marks())