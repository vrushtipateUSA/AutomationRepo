# create a string (print) only odd numbers from string.

str = input("enter a string:")
for i in range(len(str)):
    if i % 2 != 0:
        print(str[i])