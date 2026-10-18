#Write a function count_odd(numbers) to count how many odd numbers are present

def count_odd(number):
    count = 0
    for num in number:
        if num % 2 != 0:
            count = count + 1
            
    return count
number = [10,15,20,25,30,35]
    
print(count_odd(number))