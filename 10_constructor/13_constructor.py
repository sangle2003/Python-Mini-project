#Create a BankAccount class with:- account_holder,- balance
class Bank:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposite(self,amount):
        self.balance = self.balance + amount
        print("Amount deposite :: ",amount)
        
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdraw :: ",amount)
        else:
            print("insufficient balance !!!")
            
    def display_balance(self):
        print("account Holder : ",self.account_holder)
        print("Balance : ",self.balance)
        
account_holder = input("Enter your name :: ")
balance = int(input("Enter your balance :: "))
account = Bank(account_holder,balance)

print("-------------------------------------")
deposites = int(input("Enter your deposite amount :: "))
account.deposite(deposites)

print("---------------------------------------")
withdrows = int (input("enter a  withdraw amount "))
account.withdraw(withdrows)

print("----------------------------------------")
account.display_balance()

        
        
        