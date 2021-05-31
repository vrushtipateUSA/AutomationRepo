# Using while loop, if statement and str() function; iterate through the list and if there is a 100, print it with its index number.

lst = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
i = 0
while i < len(lst):
    if lst[i] == 100:
        print("There is a 100 at index no: ", i)
    i = i+1
print(i)
