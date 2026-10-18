#with return ,with parameter 
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

n = int (input("Enter number :: "))
print("Factorial of number is :: ",factorial(n))