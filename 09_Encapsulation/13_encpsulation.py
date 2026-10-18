class Subscription:
    def __init__(self):
        self.__active = False
        
    def activate(self):
        self.__active=True
        
    def access_content(self):
        if self.__active:
            print("Access gareted")
        else:
            print("acess denied")
            
s = Subscription()
s.access_content()
s.activate
s.activate