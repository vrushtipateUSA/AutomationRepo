# Write a Python program to reverses a string if it's length is a multiple of 4.

str3 = "jay shri krishna radhe krishn jay yogeshwarq"
x = len(str3)
print(x)
if x % 4 == 0:
    print(str3[::-2])
else:
    print("length is not divisible of 4")

print(str3[::-2])
print(reversed(str3))