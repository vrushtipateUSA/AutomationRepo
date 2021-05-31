# replace 'and' with 'or' & change the case of each character.

str ="We are going to india"
old_char = 'are'
new_char = 'or'
new_str = ' '
for i in range(len(old_char)):
    if str[i] == new_char:
        new_str = new_str + new_char
    else:
        new_str = new_str + str[i]


print("\nOriginal String :  ", str)
print("Modified String :  ", new_str)