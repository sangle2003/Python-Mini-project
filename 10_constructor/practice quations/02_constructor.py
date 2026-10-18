#Create a Person class. Use a constructor to initialize name and city. Create an object and display the details
class Person:
    def __init__(self,name,city):
        
        self.name = name
        self.city = city
        
name = input("Enter your name :: ") 
city = input ("Enter your city :: ")

p1 = Person(name , city )

print ("name is :: ",p1.name)
print("city is :: ",p1.city )