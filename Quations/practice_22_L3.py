#Write a function count_digits(n) to count the number of digits.
def digit(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count
print(digit(9234))