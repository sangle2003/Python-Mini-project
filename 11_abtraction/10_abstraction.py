from abc import ABC, abstractmethod

class Restarant(ABC):
    @abstractmethod
    def show_menu(self):
        pass
    
class PizzaPlace(Restarant):
    def show_menu(self):
        print("pizza menu : marghrita ,farmhouse")
        
class BurgerPlace(Restarant):
    def show_menu(self):
        print("burger menu : veg burger ,chees berger ")
        
choice = input("Choose Restaurant (Pizza/Burger): ").lower()

if choice == "pizza":
    obj = PizzaPlace()
elif choice == "burger":
    obj = BurgerPlace()
else:
    print("Invalid choice")
    obj = None
    
if obj:
    obj.show_menu()