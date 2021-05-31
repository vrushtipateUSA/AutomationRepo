#  Write a Python program to multiplies all the items in a list.
def multiply_list(items):
    total = 1
    for x in items:
        total *= x
    return total
print(multiply_list([3,5,4]))

list1 = [2, 5, 7,]
result = 1
for i in list1:
    result = result * i
print("multiplication of all element: ", result)


