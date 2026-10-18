class abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send (self,msg):
        pass
    
class Email (Notification):
    def send(self, msg):
        print("Email sent:", msg)

class SMS(Notification):
    def send(self, msg):
        print("SMS sent:", msg)

text = input("Enter message: ")

Email().send(text)
SMS().send(text)
    
