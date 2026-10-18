from abc import ABC, abstractmethod

class Login(ABC):
    @abstractmethod
    def authenticate(self):
        pass
    
class GoogleLogin():
    def authenticate(self):
        print("Logged in using google")
        
class FecebookLogin(Login):
    def authenticate(self):
        print("Logged in using fece books")
        
