# sum of even numbers

from functools import reduce

def sum_even(total, num):
    if num % 2 == 0:
        return total + num
    else:
        return total

numbers = [10, 15, 20, 25, 30, 35, 40]

res = reduce(sum_even, numbers, 0)

print("Sum of even numbers is ::", res)