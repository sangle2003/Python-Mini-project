class Person:
    def __add__(self, age):
        self.age = age
        
    def __gt__ (self,other):
        return self.age > other.age
    
p1 = Person(25)
p2 = Person (10)
print
        