str1 =("This is sunday and we are enjoying party")
old_char = 'are'
new_char = 'or'

str2 = ''
for i in range(len(str1)):
    if(str1[i] == new_char):
        str2 = str2 + new_char
    else:
        str2 = str2 + str1[i]


print("Original String :  ", str1)
print("Modified String :  ", str2)
