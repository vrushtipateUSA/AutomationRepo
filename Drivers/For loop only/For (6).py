# find even number from range 0 to 25 and their sum.

sum = 0

for i in range(0,26):
    if i % 2 == 0 :
       print(i)
       sum = sum + i
print(sum)