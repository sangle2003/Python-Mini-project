from abc import ABC, abstractmethod

class Delivary(ABC):
    @abstractmethod
    def delivary(self):
        pass
    
class Standard(Delivary):
    def Delivary(self):
        print("Stander delivary ")
        
class Express(Delivary):
    def Delivary(self):
        print("Express delivary")
        
choice = input ("Enter delivary ")

if choice == "express":
    Express().deliver()
else:
    Standard().deliver()