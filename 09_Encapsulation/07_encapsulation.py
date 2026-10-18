class User:
    def __init__(self,username, password):
        self.__username=username 
        self.__password=password
        
    def login(self,pwd):
        return pwd==self.__password
    
u=User("admin","1234")
print(u.login"admin")
print(u.__username"admin")
        