class Card:
    def __init__(self):
        self.__item=[]
        
    def add_item(self,item):
        self.__item.append(item)
        
    def remove_item(self,item):
        if item in self.__item:
            self.__item.remove(item)
            
    def view_card(self):
        return self.__item
    
s = Card()
s.add_item("laptop")
s.add_item("mouse")
s.add_item("chargeer")

s.remove_item("mouse")
print(s.view_card())