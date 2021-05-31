# Write a Python program to find the list of words
# that are longer than n from a given list of words

str=input("enter strings : ")
n=int(input("enter value of n "))
a= str.split(" ")
print(a)

b=[]

for i in a:

    if (len(i)> n) :

        b.append(i)

print("list of words : ",b)