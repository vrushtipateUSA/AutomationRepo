# Write a Python program to detect
# the number of local variables declared in a function.

def abc():
    x = 1
    y = 2
    z = 6
    print("Python")


print(abc.__code__.co_nlocals)





