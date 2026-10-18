#factorial using function.
def factorial(n):
    for i in range(1,n+1):
        if n == 0 or n == 1:
            return 1
        else:
             return n*factorial(n-1)

        num = int(input("Enter your number :: "))
    
print(factorial())
