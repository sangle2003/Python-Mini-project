#check a positive and negative number.
def pos_neg():
    n = int (input("Enter your number :: "))
    if n > 0:
        print("Number is positive")
    elif n < 0:
        print("Numbeer is negative")
    else:
        print("number is zero")
        
pos_neg()