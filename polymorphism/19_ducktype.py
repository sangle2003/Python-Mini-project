class Swigy:
    def deliver(self):
        print("Food delivered by swigy")
        
class Zomato:
    def deliver(self):
        print("Food delivered by zomato")
        
def order(app):
    app.deliver()
    
order(Swigy())
order(Zomato())