class Bank:
    def __init__(self,balance):
        self.balance = balance
        
    def display_bal(self):
        print("Current balance is :: ",self.balance)
        
b = Bank(50000)
b.display_bal()
    