class bank:
    def __init__(self,bank_holder,balance):
        self.bank_holder = bank_holder
        self.balance = balance
        
    def display(self):
        print("holde name :: ",self.bank_holder)
        print("balance :: ",self.balance)
        
b1 = bank("Pradip",2000)
b1.display()
        