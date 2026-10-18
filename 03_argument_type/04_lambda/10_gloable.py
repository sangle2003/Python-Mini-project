balance = 5000
print(balance)

def deposit():
    global balance
    balance += 2000
    
deposit()
print(balance)