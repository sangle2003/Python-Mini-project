def factorial():
    num = int (input("Enter your number :: "))
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
        i += 1
        
    print("Factorial is :: ",fact)
    
factorial()
factorial()