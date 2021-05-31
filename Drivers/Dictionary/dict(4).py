# Write a Python program to iterate over dictionaries using for loops.

d = {'x': 10, 'y': 20, 'z': 30}
for key, value in d.items():
    print(key,'=',value)

# one more example

dict1 = {'vrushti': 'jigar','abhi': 'tiku','anil': 'maya','radhe': 'krishna'}
for key,value in dict1.items():
    print(key,'=',value)

#  Write a Python script to generate and
#  print a dictionary that contains a number
#  (between 1 and n) in the form (x, x*x).

n = int(input("enter a number"))
d = dict()

for i in range(1,n+1):
    d[i] = i*i
print(d)





