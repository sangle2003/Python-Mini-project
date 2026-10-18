#Write a function list_sum(numbers) to find the sum of all elements in a list.
def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(list_sum([1, 2, 3, 4, 5]))