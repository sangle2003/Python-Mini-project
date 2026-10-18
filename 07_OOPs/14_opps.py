class Bank:
    def b(self):
        self.name=input("Enter Bank Name :: ")

class Account(Bank):
    def a(self):
        self.acc=int(input("Enter Account Number :: "))

class Savings (Account):
    def sa(self):
        print("Bank name is :: ", self.name)
        print("Account No :: ", self.acc)
        print("Saving Account has 6 % of Interest ")

class FixedDeposit(Account):
    def fa(self):
        print("Bank name is :: ", self.name)
        print("Account No :: ", self.acc)
        print("Fixed Deposit has 10 % of Interest ")
        
    s=Savings()
    s.b()
    s.a()
    s.sa()
    
    f=FixedDeposit()
    f.b()
    f.a()
    f.fa()