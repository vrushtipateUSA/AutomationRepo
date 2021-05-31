#Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n. E.g.-
# 4! = 1*2*3*4 = 24
# 3! = 3*2*1 = 6
# 2! = 2*1 = 2

num = int(input("enter a number: "))

fac = 1
i = 1

while i <= num:
    fac = fac * i
    i = i + 1

print("factorial of ", num, " is ", fac)

