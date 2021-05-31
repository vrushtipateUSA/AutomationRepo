# Write a Python function to multiply all the numbers in a list.

def multiplication(numbers):
    multi = 1
    for i in numbers:
        multi *= i
    return(multi)
print(multiplication((20,10,3)))