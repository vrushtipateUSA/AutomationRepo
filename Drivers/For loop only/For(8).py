# Write a Python program to get the Fibonacci series between 0 to 50.
# ( 0, 1, 1, 2, 3, 5, 8, 13)

first = 0
second = 1

for i in range(0,51):
    print(first)
    v = first
    first = second
    second = v + second


