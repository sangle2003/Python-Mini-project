# The Universal Translator
# Goal: Create a system that "translates" a message into different formats without the user knowing 
# the formatting logic.

# Task:
# Create an abstract class Translator with an abstract method display_message(text).
# Implement two subclasses:
# ShoutingTranslator: Converts the input text to ALL CAPS.
# WhisperingTranslator: Converts the input text to lowercase.
# User Input: Ask the user to type a sentence.
# Action: Create instances of both subclasses and pass the user's sentence into .display_message() 
# for each to see the different results.

from abc import ABC, abstractmethod

class Translator(ABC):
    @abstractmethod
    def display_message(self, text):
        pass

# 2. Implement the Subclasses
class ShoutingTranslator(Translator):
    def display_message(self, text):
        print(f"Shouting: {text.upper()}")

class WhisperingTranslator(Translator):
    def display_message(self, text):
        print(f"Whispering: {text.lower()}")
        
# 3. User Input
user_text = input("Enter a sentence to translate: ")

# 4. Action (Using Abstraction)
shouter = ShoutingTranslator()
whisperer = WhisperingTranslator()

shouter.display_message(user_text)
whisperer.display_message(user_text)