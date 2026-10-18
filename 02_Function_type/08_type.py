def even_odd():
    num = int(input("Enter your number :: "))
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
print(even_odd())