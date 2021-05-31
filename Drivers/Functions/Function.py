# Write a Python function to sum all the numbers in a list.

def sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
print(sum((5,6,7,8)))


