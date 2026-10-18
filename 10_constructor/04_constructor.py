class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        
    def deposit(self,damt):
        self.balance += damt
        print("deposited amount is :: ",damt)
        print("balance amount :: ",self.balance)
        
    def withdraw(self,wamt):
        self.balance -= wamt
        print("withdraw amount :: ",wamt)
        print("balance amount :: ",self.balance)
            
name = input("Enter Account holder name :: ")
balance = float(input("Enter balance :: "))

acc = Bank(name,balance)

damt = float (input("Enter deposite amount :: "))
wamt = float(input("Enter withdraw Amount :: "))

print("deposite :: ",acc.damt)
print("withdraw :: ",acc.damt)
