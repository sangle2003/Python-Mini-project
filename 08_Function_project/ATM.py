def check_balance(balance):
    print("currenr balance is :: ",balance)
    
def deposit(balance):
    amt = float(input("Enter amount to deposite :: "))
    balance += amt
    print("amount deposite succesfully !!!!!")
    print("Current balance is ::",balance)
    return balance

def withdraw(balance):
    amt = float(input("Enter amount to be withdrew :: "))
    if amt > balance:
        print("Insufficient balance to withdraw !!!!")
    else:
        balance = balance - amt
        print("amount withdraw successfully !!!!")
        return balance
    
balance = 1000
while True:
    print("1.check balance \n 2.deposite amount \n 3.withdraw amount \n 4.exit ")
    choice = int(input("Enter your choice :: "))
    
    if choice == 1:
        check_balance(balance)
    elif choice == 2:
        balance= deposit(balance)
    elif choice == 3:
        balance = withdraw(balance)
    elif choice == 4:
        print("Thank you for using our atm ")
    else:
        print("Invalid choice ")