str1 = " My name is Vrushti Patel"
word_list = str1.split(" ")
print(word_list)

list2 = []
for word in word_list:
    output = word.swapcase()
    list2.append(output)

print(list2)
