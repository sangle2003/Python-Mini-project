# Assignment 4: Simple Appliance Controller
# Goal: Use abstraction to turn different home appliances on and off using a single command structure.

# Task:
# Create an abstract class Appliance with an abstract method turn_on().
# Implement two subclasses:
# Toaster: turn_on() should print: "Heating up the coils..."
# Lamp: turn_on() should print: "Illuminating the bulb..."
# User Input: Ask the user: "Which appliance would you like to use? (Toaster/Lamp): ".
# Action: Use an if/else statement to create the object chosen by the user, then call the .turn_on() 
# method.
from abc import ABC, abstractmethod

# 1. Create the Abstract Base Class
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

# 2. Implement the Subclasses
class Toaster(Appliance):
    def turn_on(self):
        print("Toaster: Heating up the coils ... Watch your toast!")

class Lamp(Appliance):
    def turn_on(self):
        print("Lamp: Illuminating the bulb ... The room is bright!")

# 3. User Input
choice = input("Which appliance would you like to use? (Toaster/Lamp): ").strip().capitalize()

# 4. Action (Selection and Execution)
if choice == "Toaster":
    device = Toaster()
elif choice == "Lamp":
    device = Lamp()
    
else:
    print("Unknow appliance! ")
    
# If a valid device was created, call the abstract method
if device:
    device.turn_on()