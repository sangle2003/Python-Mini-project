#Write a function multiplication_table(n) to print the table of a number.
def multiplication(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i}")
        
multiplication(5)