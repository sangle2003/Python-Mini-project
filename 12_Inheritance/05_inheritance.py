class Bank:
    def get_details(self):
        self.bankname = input("Enter Bank name :: ")
        
class Account(Bank):
    def get_account(self):
        self.balance = int(input("Enter balance :: "))
        print(self.bankname," bank has balance of Rs. ",self.balance)
        
a = Account()
a.get_details()
a.get_account()