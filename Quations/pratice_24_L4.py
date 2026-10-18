#Write a function count_even(numbers) to count how many even numbers are present.

def count_even(numbers):
    count = 0

    for num in numbers:
        if num % 2 == 0:
            count = count + 1

    return count


numbers = [10, 15, 20, 25, 30, 35, 40]

result = count_even(numbers)

print("Total even numbers =", result)
    