#write a function print_even(n) that prints all even numbers from 1 to n when called.
def even(n):
    for i in range (1,n+1):
        if i % 2 == 0:
            print(i)
            
even(10)