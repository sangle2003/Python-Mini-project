from functools import reduce

# find largest digit
numbers = [12, 45, 8, 23, 84, 19, 3]

def get_larger(digit_a, digit_b):
    if digit_a > digit_b:
        return digit_a
    return digit_b

# Convert all numbers into individual digits
all_digits = "".join(str(n) for n in numbers)

# Find largest digit
largest_digit = int(reduce(get_larger, all_digits))

print("Largest digit is ::", largest_digit)