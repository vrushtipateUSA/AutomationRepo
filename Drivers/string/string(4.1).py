str = "vrushti and jigar are celebrating a party"
word = str.split()
largest = small = word[0]
for i in range (len(word)):
    if len(largest) < len(word[i]):
       largest = word[i]
    if len(small) > len(word[i]):
       small = word[i]


print("largest word in string", largest)
print("small word in string", small)


