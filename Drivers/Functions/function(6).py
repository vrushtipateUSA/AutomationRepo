# Write a Python function that takes a number
# as a parameter and check the number is prime or not.

def prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            print(" no prime")
        else:
            print("it is prime num")
        print(i)
