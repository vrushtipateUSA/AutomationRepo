# Find out the longest and smallest word in the input string.

Str = input("enter a line of string")
word = Str.split()
print(word)
largest = small = word[0]
for i in range(0, len(word)):
    if len(largest) < len(word[i]):
        largest = word[i]
    if len(small) > len(word[i]):
        small = word[i]
print("longest word in str", largest)
print("small word in str", small)
